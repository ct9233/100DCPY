from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_posts():
    blog_api_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_api_url)
    return response.json()


@app.route("/")
def home():
    all_posts = get_posts()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    all_posts = get_posts()
    selected_post = None
    for post in all_posts:
        if post["id"] == index:
            selected_post = post
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run(debug=True)
