from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv('articles.csv')
df = df[df['title'].notna()]

count = CountVectorizer(stop_words='english')
countMatrix = count.fit_transform(df['title'])

cosinesim = cosine_similarity(countMatrix, countMatrix)

df = df.reset_index()
indices = pd.Series(df.index, index=df['contentId'])

def get_recommendations(contentId):
    index = indices[int(contentId)]
    simscores = list(enumerate(cosinesim[index]))
    simscores = sorted(simscores, key=lambda x: x[1], reverse=True)
    simscores = simscores[1:11]
    articleindices = [i[0] for i in simscores]
    return df[["url", "title", "text", "lang", "total_events"]].iloc[articleindices].values.tolist()