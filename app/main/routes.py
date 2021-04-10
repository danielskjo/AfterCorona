from flask import Blueprint, render_template, request, flash, redirect, abort, url_for
from flask_login import current_user
from app import db
from app.models import Post
from app.posts.forms import PostForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.created.desc()).paginate(page=page, per_page=5)

    form = PostForm()
    if form.validate_on_submit():
        post = Post(place=form.place.data,
                    location=form.location.data, desc=form.desc.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created', 'success')
        return redirect(url_for('main.home'))

    if current_user.is_authenticated:
        username = current_user.username
        image = url_for(
            'static', filename='profile_pictures/' + current_user.image)
    else:
        username = ''
        image = ''

    return render_template('home.html', posts=posts, form=form, username=username, image=image)


