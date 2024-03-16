"""
Flask Application for Text Summarization

This Flask application provides endpoints for summarizing text 
using a pre-trained model.

Endpoints:
- GET '/': Renders the index.html template with a form to input text.
- POST '/summarize': Handles the form submission, validates API key, 
                    and summarizes the input text.

Example Usage:
    $ python app.py
    * Running on http://127.0.0.1:5000/

    Open a web browser and navigate to http://127.0.0.1:5000/ to access the application.
"""

import os
from flask import Flask, render_template, request
from .constants import API_KEY
from .summarize import Summarizer

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model/build/t5_model/")
MODEL_FILE = os.path.join(MODEL_PATH, "t5_model.pth")
TOKENIZER_PATH = "t5-small"

summarizer = Summarizer(MODEL_PATH, MODEL_FILE, TOKENIZER_PATH)


@app.route("/")
def index():
    """Renders the index.html template with a form to input text."""
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    """Handles the form submission, validates API key, and summarizes the input text."""
    api_key = request.form.get("api_key")
    text = request.form.get("text")

    if not api_key or api_key != API_KEY:
        error_message = "Invalid API key. Please enter a valid API key."
        return render_template("index.html", error_message=error_message)

    if not text:
        error_message = "Text field is required."
        return render_template("index.html", error_message=error_message)

    summarized_text = summarizer.call_model(text)

    return render_template("result.html", summarized_text=summarized_text)


if __name__ == "__main__":
    app.run(debug=False)
