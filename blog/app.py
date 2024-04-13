from flask import Flask, render_template, request
import yaml

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    posts = config["posts"]
    return render_template("index.html", posts=posts)


@app.route("/admin/posts", methods=["POST"])
def create_post():
    pass
