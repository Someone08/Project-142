from flask import Flask, jsonify
from storage import all_articles, liked_articles, not_liked_articles
from demographic_flitering import output_demographic
from content_filtering import get_recommendation

app = Flask(__name__)

@app.route('/popular_articles', methods=['GET'])
def get_popular_articles():
    return jsonify(output_demographic.to_dict(orient='records'))

@app.route('/recommended_articles', methods=['GET'])
def get_recommended_articles():
    if all_articles:
        recommended_article = get_recommendation(all_articles[0][0])
        return jsonify(recommended_article)
    else:
        return jsonify({"message": "No more articles to recommend."})

if __name__ == '__main__':
    app.run(debug=True)