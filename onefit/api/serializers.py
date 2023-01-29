from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        fields = ('name', 'type', 'img', 'created_at')


class ReviewSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='email'
    )
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('rate', 'comment', 'created_at', 'creator', 'company')


class CreateReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('rate', 'comment', 'created_at', 'creator', 'company')
