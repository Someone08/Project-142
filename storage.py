from flask import Flask, jsonify, request
import pandas as pd
import csv 

app = Flask(__name__)

articles = pd.read_csv('articles.csv')

articles.columns = ['id'] + articles.columns[1:].tolist()

all_articles = articles.values.tolist()
liked_articles = []
not_liked_articles = []

@app.route('/get_article', methods=['GET'])
def get_article():
    if all_articles:
        return jsonify(all_articles[0])
    else:
        return jsonify({"message": "No more articles to show."})

@app.route('/like_article', methods=['POST'])
def like_article():
    if all_articles:
        liked_articles.append(all_articles.pop(0))
        return jsonify({"message": "Article liked successfully."})
    else:
        return jsonify({"message": "No more articles to like."})

@app.route('/dislike_article', methods=['POST'])
def dislike_article():
    if all_articles:
        not_liked_articles.append(all_articles.pop(0))
        return jsonify({"message": "Article disliked successfully."})
    else:
        return jsonify({"message": "No more articles to dislike."})

if __name__ == '__main__':
    app.run(debug=True)