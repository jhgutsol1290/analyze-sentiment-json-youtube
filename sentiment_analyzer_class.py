import json
import numpy as np
from matplotlib import pyplot as plt 
import seaborn as sns
from textblob import TextBlob
from repustate import Client

class YoutubeClient:
  """
  This cass initializes a Youtube client 
  with an specific `api_key`.
  """

  def __init__(self, client_api_key, client_version):
    """
    Creating a Youtube client. 
    """
    self.api_client = Client(api_key = client_api_key, version = client_version)


class SentimentAnalyzer(YoutubeClient):
  """
  This class inherits the data and methods 
  from the class `YoutubeClient`.
  """
  
  '''
  def get_scores_list(self, comments):
    """
    This method obtains
    """

    listaNueva = [element["commentText"] for element in comments]
    scores = []
    new_scores_list = []
    
    for comment in listaNueva:
      score = self.api_client.sentiment(comment, lang='es')
      scores.append(score)

    print("scores: {}".format(scores))
    self.scores_list = [score['score'] for score in scores]
    for score in self.scores_list:
      if score == 0:
        pass
      else:
        new_scores_list.append(score)
    return new_scores_list
  '''

  def get_sentiment_score(self, comments):
    """
    This method obtains the sentiment score
    of various comments of many users.
    """

    # Obtaining the comments of the users.
    comments_list = [element["commentText"] for element in comments]

    # Obtaining the sentiment score for each comment.
    sentiment_score = [self.api_client.sentiment(comment, lang = "es")["score"] 
                       for comment in comments_list
                       if self.api_client.sentiment(comment, lang = "es")["score"] != 0]
    
    return sentiment_score

  def calculate_percentage_neutral(self):
    total = len(self.scores_list)
    neutral = []
    for score in self.scores_list:
      if score == 0:
        neutral.append(score)
    neutral_result = len(neutral) * 100 / total
    return neutral_result
    
  def calculate_percentage_positive(self):
    total = len(self.scores_list)
    positive = []
    for score in self.scores_list:
      if score > 0:
        positive.append(score)
    positive_result = len(positive) * 100 / total
    return positive_result
  
  def calculate_percentage_negative(self):
    total = len(self.scores_list)
    negative = []
    for score in self.scores_list:
      if score < 0:
        negative.append(score)
    negative_result = len(negative) * 100 / total
    return negative_result