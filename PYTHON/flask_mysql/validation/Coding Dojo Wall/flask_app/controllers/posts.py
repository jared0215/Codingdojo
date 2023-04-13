from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.posts import Post
from flask_app.models.comment import Comment


# Route to render the wall page
@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect("/")

    all_posts = Post.get_all_posts_with_creator()

    for post in all_posts:
        post.comments = Comment.get_all_comments(
            {'posts_id': post.id})

    return render_template('wall.html', all_posts=all_posts)


# Route for adding a post
@app.route('/makepost', methods=['POST'])
def makepost():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        'content': request.form['content'],
        'user_id': session['user_id']
    }

    Post.save(data)
    return redirect('/wall')


# Route for deleting a post
@app.route('/deletepost/<int:posts_id>', methods=['POST'])
def deletepost(posts_id):
    if 'user_id' not in session:
        return redirect("/")

    data = {'id': posts_id}
    post = Post.get_post_by_id(data)

    if post and session['user_id'] == post.users_id:
        Post.delete(data)

    return redirect('/wall')


# Route that allows the user to comment on a post
@app.route('/addcomment/<int:posts_id>', methods=['POST'])
def add_comment(posts_id):
    if 'user_id' not in session:
        return redirect("/")

    data = {
        'content': request.form['content'],
        'users_id': session['user_id'],
        'posts_id': posts_id
    }

    Comment.save_comment(data)
    return redirect('/wall')
