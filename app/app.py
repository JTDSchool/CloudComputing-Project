"""
Flask Application for Text Summarization

This Flask application provides endpoints for summarizing text using a pre-trained model.

Endpoints:
- GET '/': Renders the index.html template with a form to input text.
- POST '/summarize': Handles the form submission, validates API key, and summarizes the input text.

Constants:
- API_KEY: A constant representing the API key required for accessing the summarization service.

Example Usage:
    $ python app.py
    * Running on http://127.0.0.1:5000/

    Open a web browser and navigate to http://127.0.0.1:5000/ to access the application.
"""

from flask import Flask, render_template, request
from .constants import API_KEY
from .summarize import Summarizer

app = Flask(__name__)

# Initialize Summarizer with HDF5 model and tokenizer paths

model_path = "model/build/t5_model/"
model_file = "model/build/t5_model/t5_model.pth"
tokenizer_path = "t5-small"
summarizer = Summarizer(model_path, model_file, tokenizer_path)


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
