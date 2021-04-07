from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.place = form.place.data
        post.location = form.location.data
        post.desc = form.desc.data
        db.session.commit()
        flash('Post updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.place.data = post.place
        form.location.data = post.location
        form.desc.data = post.desc
    return render_template('new_post.html', form=form)


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'success')
    return redirect(url_for('main.home'))
