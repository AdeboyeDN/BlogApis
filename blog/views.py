from django.shortcuts import render
from .serializers import postlist
from .models import blog
from rest_framework import generics

class postlistview(generics.ListAPIView):
     queryset = blog.objects.all()
     serializer_class = postlist
