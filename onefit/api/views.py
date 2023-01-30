from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .forms import *
from .serializers import *


class CompanyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = Company.objects.values('name', 'type', 'img')  # спросить как адаптировать сериалайзер под запрос
        serializer = CompanySerializer(content, many=True)
        return Response({"companies": serializer.data})


class CompanyDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        content = Company.objects.filter(pk=pk).values('name', 'type', 'img', 'created_at')
        serializer = CompanySerializer(content, many=True)
        return Response({"company": serializer.data})


class CompanyListByTypeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tp):
        content = Company.objects.filter(type=tp.upper()).values('name', 'type', 'img')
        serializer = CompanySerializer(content, many=True)
        return Response({"companies by type": serializer.data})


class ReviewList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = Review.objects.all()
        serializer = ReviewSerializer(content, many=True)
        return Response({"reviews": serializer.data})

    def post(self, request):
        serializer = CreateReviewSerializer(data=request.data)
        creator_id = request.data['creator']
        company_id = request.data['company']
        is_there_review = Review.objects.filter(creator=creator_id, company=company_id).exists()
        if is_there_review:
            return Response({"error": "You have already left a review for this company"})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ReviewListByRate(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, rate):
        content = Review.objects.filter(rate=rate)
        serializer = ReviewSerializer(content, many=True)
        return Response({"reviews": serializer.data})


class UserReviews(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        content = Review.objects.filter(creator_id=pk)
        serializer = ReviewSerializer(content, many=True)
        return Response({"reviews": serializer.data})
