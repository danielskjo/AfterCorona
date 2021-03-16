from flask import Flask, render_template, url_for
app = Flask(__name__)

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


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
