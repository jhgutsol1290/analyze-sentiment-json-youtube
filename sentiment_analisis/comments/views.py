from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.youtube_client import SentimentAnalyzer

# Create your views here.

class SentimentAnalyzerList(APIView):
	"""
	This class obtains the sentiment score of some 
	Youtube comments.
	"""

	def post(self, request):
		"""
		This method obtains the sentiment score based on 
		the comments entered.
		"""

		
		client = SentimentAnalyzer(client_api_key = request.data["api_key"], 
			                       client_version = request.data["client_version"])

		print(request.data["api_key"])
		print(request.data["client_version"])
		sentiment_score = client.get_sentiment_score(comments = request.data["data"])
		neutral_sentiment_score = client.get_neutral_sentiment_percentage()
		positive_score, negative_score = client.get_positive_negative_sentiment_percentage()
		

		return Response(
			data = {
				"sentiment_score": sentiment_score,
				"neutral_sentiment_score": neutral_sentiment_score,
				"positive_score": positive_score,
				"negative_score": negative_score,
			},
			status = status.HTTP_202_ACCEPTED,
		)
