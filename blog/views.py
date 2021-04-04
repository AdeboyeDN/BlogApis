from django.shortcuts import render
from .serializers import postlist,detaillist
from .models import blog
from rest_framework import generics


class createview(generics.CreateAPIView):
     queryset = blog.objects.all()
     serializer_class = postlist



class postlistview(generics.ListAPIView):
     queryset = blog.objects.all()
     serializer_class = postlist

class detailview(generics.RetrieveUpdateDestroyAPIView):
     queryset = blog.objects.all()
     serializer_class = detaillist