import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurant, FoodItem
from restaurants.serializers import RestaurantSerializer, FoodItemSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all().order_by('-created_on')
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all().order_by('-created_on')
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
