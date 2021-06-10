from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()
EMAIL = "email@server.com"
PASSWORD = "1234PASS"

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    selected_post = None
    for post in posts:
        if post["id"] == index:
            selected_post = post
    return render_template("post.html", post=selected_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.server.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_msg)


if __name__ == "__main__":
    app.run(debug=True)
