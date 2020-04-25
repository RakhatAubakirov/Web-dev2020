from django.shortcuts import render
from rest_framework import generics
from api.models import Category, Product, Comment, User
from rest_framework.permissions import IsAuthenticated
from api.serializers import CategorySerializer, ProductSerializer, CommentSerializer, UserSerializer, CategoryWithProductsSerializer
from rest_framework import mixins


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTopAPIView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-salary')[:10]
    serializer_class = ProductSerializer

class CategoryWithProducts(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithProductsSerializer






# Create your views here.
