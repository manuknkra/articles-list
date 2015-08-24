from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


# Create your views here.
from rest_framework import generics, permissions


from .serializers import ArticleSerializer
from .models import Article

class ArticleList(generics.ListCreateAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
       return super(IndexView, self).dispatch(*args, **kwargs)

