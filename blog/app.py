from pathlib import Path

from flask import Flask, render_template, request
import yaml

from .posts import slugify

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent


@app.route("/", methods=["GET"])
def index():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    posts = config["posts"]
    return render_template("index.html", posts=posts)


# TODO: Use a temporary directory for testing
def content_dir():
    return BASE_DIR / Path("content")


def site_dir():
    return BASE_DIR / Path("site")


def save_metadata(metadata):
    content_dir().mkdir(parents=True, exist_ok=True)
    with open(content_dir() / Path("metadata.yml"), "w") as f:
        yaml.dump(metadata, f)


def save_post(filename, content):
    content_dir().mkdir(parents=True, exist_ok=True)
    with open(content_dir() / Path(filename), "w") as f:
        f.write(content)


def get_metadata():
    path = content_dir() / Path("metadata.yml")
    if not path.exists():
        return {"posts": []}
    with open(path, "r") as f:
        return yaml.load(f, yaml.Loader)


@app.route("/admin/posts", methods=["POST"])
def create_post():
    form = request.form
    # TODO: Validation
    post = {
        "title": form["title"],
        "slug": form["slug"] or slugify(form["title"]),
        "tags": form["tags"].split(),
        # TODO: Validate valid Markdown
        "content": form["content"],
    }
    content = post.pop("content")
    save_post(post["slug"] + ".md", content)
    # TODO: Raise if slug already exists
    metadata = get_metadata()
    metadata["posts"].append(post)
    # TODO: Redirect back to editor
    return ""
