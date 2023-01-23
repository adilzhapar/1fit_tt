from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, world!'}
        return Response(content)

