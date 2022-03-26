from flask import Blueprint, render_template

colinf = Blueprint("colinf", __name__)


@colinf.route("/")
def home():
    return render_template("index.html")

@colinf.route("/messages")
def messages():
    return render_template("messages.html")