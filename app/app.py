from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.form["text"]
    summarized_text = text
    return render_template("result.html", summarized_text=summarized_text)


if __name__ == "__main__":
    app.run(debug=False)
