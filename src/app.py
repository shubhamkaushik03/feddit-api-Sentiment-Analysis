from flask import Flask, jsonify, request
from textblob import TextBlob
from datetime import datetime
import requests

app = Flask(__name__)

# Define some sample data to simulate comments for different subfeddits
comments_data = {
    "gaming": [
        {"id": 1, "text": "Great game!", "timestamp": "2024-05-15T12:00:00Z"},
        {"id": 2, "text": "I love this game!", "timestamp": "2024-05-15T12:30:00Z"},
        # Add more comments for the gaming subfeddit
    ],
    "science": [
        {"id": 1, "text": "Fascinating discovery!", "timestamp": "2024-05-15T13:00:00Z"},
        {"id": 2, "text": "Amazing research!", "timestamp": "2024-05-15T13:30:00Z"},
        # Add more comments for the science subfeddit
    ],
    # Add more sample data for other subfeddits
}

# Define an endpoint to fetch comments for a given subfeddit
@app.route('/api/v1/comments', methods=['GET'])
def get_comments():
    subfeddit_name = request.args.get('subfeddit')
    time_range = request.args.get('time_range')
    sort_by_polarity = request.args.get('sort_by_polarity')
    data_source_api = request.args.get('data_source_api')

    if data_source_api:
        # Fetch comments from the provided data source API
        comments = fetch_comments_from_api(data_source_api)
    elif subfeddit_name in comments_data:
        comments = comments_data[subfeddit_name]
    else:
        return jsonify({"error": "Subfeddit not found"}), 404

    # Filter by time range if specified
    if time_range:
        comments = filter_comments_by_time_range(comments, time_range)

    # Perform sentiment analysis for each comment
    analyzed_comments = []
    for comment in comments:
        text = comment['text']
        polarity = TextBlob(text).sentiment.polarity
        classification = "positive" if polarity > 0 else "negative"

        analyzed_comment = {
            "id": comment['id'],
            "text": text,
            "polarity": polarity,
            "classification": classification
        }
        analyzed_comments.append(analyzed_comment)

    # Sort by polarity score if specified
    if sort_by_polarity:
        analyzed_comments = sorted(analyzed_comments, key=lambda x: x['polarity'], reverse=True)

    # Limit to 25 most recent comments
    analyzed_comments = analyzed_comments[:25]

    return jsonify(analyzed_comments)

def fetch_comments_from_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        print("Error fetching comments from API:", e)
        return []

def filter_comments_by_time_range(comments, time_range):
    # Parse time range (assuming format is "start_time,end_time")
    start_time, end_time = time_range.split(',')
    start_time = datetime.fromisoformat(start_time)
    end_time = datetime.fromisoformat(end_time)

    # Filter comments within the specified time range
    filtered_comments = []
    for comment in comments:
        comment_time = datetime.fromisoformat(comment['timestamp'])
        if start_time <= comment_time <= end_time:
            filtered_comments.append(comment)

    return filtered_comments

if __name__ == '__main__':
    app.run(debug=True)
