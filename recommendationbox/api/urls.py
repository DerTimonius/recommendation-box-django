from django.urls import path
from .views import RecommendaionView, SearchView

urlpatterns = [
  path("movie/recommend", RecommendaionView.as_view()),
  path("movie/search", SearchView.as_view())
]