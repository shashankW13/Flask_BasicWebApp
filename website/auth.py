from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email + password)

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!!', category='success')
            else:
                flash('Incorrect Password!', category='error')
        else:
            flash('User does not exist!', category='error')

    return render_template('login.html', boolean=True)


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 chars', category='error')
        elif len(firstname) < 2:
            flash('First Name must be greater than 2 chars', category='error')
        elif len(password1) < 4:
            flash('Password must be greater than 4 chars', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        else:
            new_user = User(email=email,
                            firstname=firstname,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created Successfully!!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html')
