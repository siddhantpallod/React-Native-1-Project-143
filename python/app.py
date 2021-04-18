from flask import Flask, request, jsonify
import csv
import pandas as pd

from storage import all_articles, liked_articles, not_liked_articles
from demographic import output
from content import get_recommendations


app = Flask(__name__)

@app.route('/get-article')

def getArticle():

    data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15]
    }

    return jsonify({
        'data': data,
        'message': 'success'
    })

@app.route('/liked-articles', methods = ['POST'])

def likedArtilce():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)

    return jsonify({
        'message': 'success'
    }), 201

@app.route('/unliked-articles', methods = ['POST'])

def unlikedArticle():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)

    return jsonify({
        'message': 'success'
    }), 201

@app.route('/popular-articles')

def popularArticle():
    articleData = []

    for article in output:
        data = {
             "url": article[0],
            "title": article[1],
            "text": article[2],
            "lang": article[3],
            "total_events": article[4]
        }

        articleData.append(data)

    return jsonify({
        'data': articleData,
        'message': "success"
    }), 200

@app.route("/recommended-articles")

def recommended_articles():
    allRecommended = []

    for article in liked_articles:
        output = get_recommendations(article[4])
        for data in output:
            allRecommended.append(data)
    
    import itertools

    allRecommended.sort()
    allRecommended = list(allRecommended for allRecommended, _ in itertools.groupby(allRecommended))
    articleData = []

    for a in allRecommended:
        data = {
            "url": a[0],
            "title": a[1],
            "text": a[2],
            "lang": a[3],
            "total_events": a[4]
        }
        articleData.append(data)

    return jsonify({
        'data': articleData,
        'message': 'success'
    }), 200


if(__name__ == '__main__'):
    app.run()
