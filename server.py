from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze') or request.form.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Invalid text! Please try again!"
    
    result = emotion_detector(text_to_analyze)
    
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
