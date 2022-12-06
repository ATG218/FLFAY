from flask import Blueprint, render_template, request
from flask_login import  login_required, current_user

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

@views.route('/admin')
@login_required
def admin():
    return render_template("admin.html")