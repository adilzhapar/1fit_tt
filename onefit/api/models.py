from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_birthday(value):

    if value.year >= date.today().year:
        raise ValidationError(
            _('You are under 16 years old'),
            params={'value': value},
        )


class MyUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, password=None):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, password):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(validators=[validate_birthday])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Company(models.Model):
    IP = 'IP'
    TOO = 'TOO'
    AO = 'AO'
    TYPES = (
        (IP, 'IP'),
        (TOO, 'TOO'),
        (AO, 'AO'),
    )
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=3, choices=TYPES, default=TOO)
    img = models.ImageField(upload_to='company', blank=True, null=True)
    owner = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    rate = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    created_at = models.DateField(auto_now_add=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return f'Review {self.creator}'
