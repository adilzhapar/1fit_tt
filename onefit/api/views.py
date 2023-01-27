from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from .models import *


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, world!'}
        return Response(content)


class CompanyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = Company.objects.values('name', 'type', 'img')
        return Response(content)



class CompanyDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        content = Company.objects.filter(pk=pk).values('name', 'type', 'img', 'created_at')
        return Response(content)


class CompanyListByTypeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, tp):
        content = Company.objects.filter(type=tp.upper()).values('name', 'type', 'img')
        return Response(content)
