from sentiment_analyzer_class import SentimentAnalyzer
import json 
import numpy as np

# Loading the comments of some users.
user_comments = json.loads(open('comentarios1.json', encoding="utf8").read())

# Creating a sentiment_analyzer object.
sentiment_analyzer = SentimentAnalyzer(client_api_key = 'c53d0c7b21b8afb62c4c112a9f4f1070ee6ff308', 
	                                   client_version = 'v4')

print(sentiment_analyzer.get_scores_list(comments = user_comments))
'''

analyzer = sentiment_analyzer.get_scores_list(user_comments)
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


scores_array = np.array(analyzer)
sns.set()
ax = sns.distplot(scores_array)
print(scores_array)
plt.show()
'''

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




