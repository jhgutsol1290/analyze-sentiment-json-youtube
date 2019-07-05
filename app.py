import json
from textblob import TextBlob
import numpy as np
from repustate import Client
import seaborn as sns
from numpy import array
import matplotlib.pyplot as plt
import sentiment_analyzer_class


arreglo = json.loads(open('comentarios1.json', encoding="utf8").read())


sentiment_analyzer = sentiment_analyzer_class.Sentiment_Analyzer()
analyzer = sentiment_analyzer.get_scores_list(arreglo)
percentage_neutral = sentiment_analyzer.calculate_percentage_neutral()
percentage_positive = sentiment_analyzer.calculate_percentage_positive()
percentage_negative = sentiment_analyzer.calculate_percentage_negative()

print('-----------------------------')
print('Neutral:', percentage_neutral)
print('-----------------------------')
print('Positivo:', percentage_positive)
print('-----------------------------')
print('Negativo:', percentage_negative)
print('-----------------------------')
print('Total:', percentage_positive + percentage_negative + percentage_neutral)


scores_array = array(analyzer)
sns.set()
ax = sns.distplot(scores_array)
print(scores_array)
plt.show()


""" info = json.dumps(arreglo1)
listaNueva = []
for elemento in arreglo1:
    listaNueva.append(elemento['commentText'])

print(listaNueva)
scores = []
for comment in listaNueva:
  score = client.sentiment(comment, lang='es')
  scores.append(score)

scores_list = [score['score'] for score in scores]

new_scores_list = []
for score in scores_list:
  if score == 0:
    pass
  else:
    new_scores_list.append(score)
    
scores_array = array(new_scores_list)
sns.set()
ax = sns.distplot(scores_array)
print(scores)
plt.show() """




