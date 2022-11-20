from rest_framework import serializers
from .models import RecommendedMovie, SearchMovie

class RecommendationSerializer(serializers.ModelSerializer):
  class Meta:
    model = RecommendedMovie
    fields = ("title", "release_year", "cast", "director", "listed_in", "description", "type")

class SearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = SearchMovie
    fields = ("title", "release_year", "cast", "index")