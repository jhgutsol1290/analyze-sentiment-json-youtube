from django.urls import path
from .views import SentimentAnalyzerList

urlpatterns = [
	path('sentiment_analisis/', SentimentAnalyzerList.as_view()),
]