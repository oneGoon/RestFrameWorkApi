from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from rest_framework.settings import APISettings
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

class Book(APIView):
     def get(self, request, *args, **kwargs):
         return Response('get drf rest ok')
     def post(self, request, *args, **kwargs):
         return Response('post drf rest ok')