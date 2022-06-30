from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    pass


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 chars', category='error')
        elif len(firstname) < 2:
            flash('First Name must be greater than 2 chars', category='error')
        elif len(password1) < 4:
            flash('Password must be greater than 4 chars', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        else:
            flash('Account created Successfully!!', category='success')
    return render_template('signup.html')
