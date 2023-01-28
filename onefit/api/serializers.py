from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('rate', 'comment', 'created_at', 'creator', 'company')
