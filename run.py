from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9d53e6ab36c41ded18dae7e637876159'

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
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
