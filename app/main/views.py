from flask import render_template
from flask_login import login_required
from . import main
from ..models import User


@main.route('/')
@login_required
def index():
    users = User.query.order_by(User.username.asc()).all()
    return render_template('index.html', users=users)

