from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecommendationSerializer
from .models import RecommendedMovie
import json
from .utils import recommendations, search

# Create your views here.
class RecommendaionView(generics.ListCreateAPIView):
  def post(self, request, Format=None):
    body = json.loads(request.body)
    movie_list = body["movieList"]
    options = body["options"]
    preferences = body["preferences"]
    movie_count = body["movieCount"]

    data = recommendations.get_best_movie_rec(movie_list, movie_count, options, preferences)
    return Response(data, status=status.HTTP_200_OK)

  def put(self, Format=None):
    error_message = {"error": {"message": "method not allowed"}}
    return Response(error_message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def get(self, Format=None):
    error_message = {"error": {"message": "method not allowed"}}
    return Response(error_message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def delete(self, Format=None):
    error_message = {"error": {"message": "method not allowed"}}
    return Response(error_message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SearchView(generics.ListCreateAPIView):
  def post(self, request, Format=None):
    body = json.loads(request.body)
    movie = body["searchItem"]
    data = search.search(movie)
    return Response(data, status=status.HTTP_200_OK)

  def put(self, Format=None):
    error_message = {"error": {"message": "method not allowed"}}
    return Response(error_message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def get(self, Format=None):
    error_message = {"error": {"message": "method not allowed"}}
    return Response(error_message, status=status.HTTP_405_METHOD_NOT_ALLOWED)

  def delete(self, Format=None):
    error_message = {"error": {"message": "method not allowed"}}
    return Response(error_message, status=status.HTTP_405_METHOD_NOT_ALLOWED)