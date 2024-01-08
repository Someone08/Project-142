from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df1 = pd.read_csv('path/to/articles.csv').dropna(subset=['title'])

vectorizer = CountVectorizer(stop_words='english')
count_matrix = vectorizer.fit_transform(df1['title'])
cosine_sim = cosine_similarity(count_matrix, count_matrix)

df1 = df1.set_index('title')

def get_recommendations(contentId, cosine_sim=cosine_sim):
    idx = df1.index.get_loc(contentId)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [x[0] for x in sim_scores]
    return df1.index[article_indices].tolist()

recommend = 9222265156747237864
recommendations = get_recommendations(recommend, cosine_sim)
print("Recommendations for Article {}: {}".format(recommend, recommendations))