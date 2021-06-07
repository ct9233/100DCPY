from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()

app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"

@app.route("/post/<int:index>")
def show_post(index):
    selected_post = None
    for post in posts:
        if post["id"] == index:
            selected_post = post
    return render_template("post.html", post=selected_post)

if __name__ == "__main__":
    app.run(debug=True)

