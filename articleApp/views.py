from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions


from .serializers import ArticleSerializer
from .models import Article

class ArticleList(generics.ListCreateAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

