"""
Flask server application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the index.html page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """
    Detects emotions in the provided text and returns formatted output.
    Handles blank entries with appropriate error messages.
    """
    text_to_analyze = request.args.get('textToAnalyze') or request.form.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (f"For the given statement, the system response is "
                     f"'anger': {result['anger']}, "
                     f"'disgust': {result['disgust']}, "
                     f"'fear': {result['fear']}, "
                     f"'joy': {result['joy']} and "
                     f"'sadness': {result['sadness']}. "
                     f"The dominant emotion is {result['dominant_emotion']}.")

    return response_text

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
