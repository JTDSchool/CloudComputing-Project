import sys
from flask import Flask, render_template, request
from transformers import T5Tokenizer, T5ForConditionalGeneration
import tensorflow as tf

#from Notebooks.SummerizationModel import generate_summary
#from Notebooks.SummerizationModel import tokenizer

app = Flask(__name__)

tokenizer = T5Tokenizer.from_pretrained('t5-small')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    summarized_text = generate_summary(text)
    return render_template('result.html', summarized_text=summarized_text)

def generate_summary(text):
    model_save_path = "/Users/saddhat/Desktop/CloudComputing-Project/Notebooks"
    model = T5ForConditionalGeneration.from_pretrained(model_save_path)
    inputs = tokenizer.encode("summarize:" + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == '__main__':
    app.run(debug=True)
    