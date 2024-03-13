# pylint: disable=consider-using-from-import
from flask import Flask, render_template, request
import pip._vendor.requests as requests
from .constants import API_KEY

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    api_url = "https://call-model-gateway-58u11f9h.uc.gateway.dev/call_model"
    api_key = API_KEY
    data = {"text": request.form["text"]}

    response = requests.post(f"{api_url}?key={api_key}", json=data)

    if response.status_code == 200:
        response_json = response.json()

        summarized_text = response_json.get("text", "")

    else:
        summarized_text = (
            f"There was an error -> {response.status_code}: {response.text}"
        )

    return render_template("result.html", summarized_text=summarized_text)


if __name__ == "__main__":
    app.run(debug=False)
