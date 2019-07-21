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
  
  def get_sentiment_score(self, comments):
    """
    This method obtains the sentiment score
    of various comments of many users.
    """

    # Obtaining the comments of the users.
    comments_list = [element["commentText"] for element in comments]

    self.score_data = [self.api_client.sentiment(comment, lang = "es")["score"]
                       for comment in comments_list]
    
    # Obtaining the sentiment score for each comment.
    sentiment_score = [score for score in self.score_data if score != 0]
    
    return sentiment_score

  def get_neutral_sentiment_percentage(self):
    """
    This method obtains the percentage of the
    neutral score of the comments.
    """
    
    # Doing the following if the attribute "score_data" is defined.
    if 'score_data' in self.__dict__:
      # Defining  the total number of scores.
      total_scores = len(self.score_data)

      # Defining the neutral scores list.
      neutral_scores = [score for score in self.score_data if score == 0]

      # Returning the neutral score percentage.
      return ((len(neutral_scores) * 100) / total_scores)

    # Doing the following if the attribute "score_data isn't defined."
    else:
      return print("You must have to calculate first the sentiment score of each comment")

  def get_positive_negative_sentiment_percentage(self):
    """
    This method obtains the positive and negative
    sentiment percentage.
    """

    # Obtaining the total number of scores.
    total_scores = len(self.score_data)

    positive_scores = [score for score in self.score_data if score > 0]
    negative_scores = [score for score in self.score_data if score < 0]

    positive_percentage = (len(positive_scores) * 100) / total_scores
    negative_percentage = (len(negative_scores) * 100) / total_scores

    return positive_percentage, negative_percentage 

"""
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
  """