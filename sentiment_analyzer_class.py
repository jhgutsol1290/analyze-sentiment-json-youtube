import json
from textblob import TextBlob
import numpy as np
from repustate import Client
import seaborn as sns
from numpy import array
import matplotlib.pyplot as plt

client = Client(api_key='c53d0c7b21b8afb62c4c112a9f4f1070ee6ff308', version='v4')

class Sentiment_Analyzer():
  def __init__(self, scores_list = []):
    self.scores_list = scores_list

  def get_scores_list(self, comments):
    listaNueva = []
    scores = []
    new_scores_list = []
    for elemento in comments:
      listaNueva.append(elemento['commentText'])
    for comment in listaNueva:
      score = client.sentiment(comment, lang='es')
      scores.append(score)
    self.scores_list = [score['score'] for score in scores]
    for score in self.scores_list:
      if score == 0:
        pass
      else:
        new_scores_list.append(score)
    return new_scores_list

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