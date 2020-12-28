from flask import Flask
from flask.templating import render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    return render_template_string("Hello World")


@app.route("/contact")
def contact():
    return render_template_string("This might be a contact page in the future.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
