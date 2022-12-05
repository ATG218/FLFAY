from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")


@views.route('/team')
def team():
    return render_template("team.html")


@views.route('/contact')
def contact():
    return render_template("contact.html")