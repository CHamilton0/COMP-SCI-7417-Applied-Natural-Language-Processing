# Load libraries
import numpy as np
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree

import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Create text
text_data = np.array(['I love Brazil. Brazil is best',
                      'I like Italy, because Italy is beautiful',
                      'Malaysia is ok, but I do not like spicy food',
                      'I like Germany more, Germany beats all',
                      'I do not like hot weather in Singapore'])
X = text_data
# Create target vector
y = ['positive','positive','negative','positive','negative']

# analyse with VADER
analyser = SentimentIntensityAnalyzer()
for text in text_data:
    score = analyser.polarity_scores(text)
    print(score)