from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegisterForm, LoginForm
from app.models import User, Post

posts = [
    {
        'author': 'Daniel Jo',
        'place': 'Grand Canyon',
        'location': 'Arizona',
        'desc': 'I want to see the Grand Canyon',
        'created': 'March 16, 2021'
    },
    {
        'author': 'DJ',
        'place': '63 Building',
        'location': 'Seoul, Korea',
        'desc': 'I want to fly and go to Korea',
        'created': 'March 18, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))

    return render_template('login.html', form=form)
