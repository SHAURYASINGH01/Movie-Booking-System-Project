from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Movie, Booking
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your username and password.')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/book/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def book(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        seats_booked = int(request.form['seats'])
        if seats_booked <= movie.seats:
            booking = Booking(movie_id=movie.id, user_id=current_user.id, seats_booked=seats_booked)
            movie.seats -= seats_booked
            db.session.add(booking)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('Not enough seats available.')
    return render_template('book.html', movie=movie)
