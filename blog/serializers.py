from rest_framework import serializers
from .models import blog


class postlist(serializers.ModelSerializer):
     class Meta:
          model = blog
          fields = ['author','title','date']


class detaillist(serializers.ModelSerializer):
     class Meta:
          model = blog
          fields = ['title','image','description']


