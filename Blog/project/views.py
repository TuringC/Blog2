from flask import flash, redirect, url_for, render_template, session, request, current_app, abort
from flask_login import login_user, logout_user, current_user
from flask_sqlalchemy import Pagination
# import timedelta

from project import app, db, bootstrap
from project.models import Article, User, Comment
from project.forms import ArticleInput, LoginForm, DeleteNoteForm, CommentInput


@app.route('/', methods=['GET', 'POST'])
def index(logged_in=False, user=None):
    # page = request.args.get('page', 1, type=int)
    # pagination = Article.query.order_by(Article.id.desc()).paginate(page=page, per_page=5, error_out = False)
    # articles = pagination.items
    articles = Article.query.order_by(Article.id.desc()).all()
    comments = Comment.query.order_by(Comment.id.desc()).all()
    form = DeleteNoteForm()
    # return render_template('blog.html', bootstrap=bootstrap, pagination=pagination, articles=articles)
    return render_template('blog.html', personal_page=False, articles=articles, form=form, comments=comments)


@app.route('/blog-detail/<id>', methods=['GET', 'POST'])
def blog_detail(id):
    article = Article.query.get(id)
    comments = Comment.query.filter_by(blog_id=id).order_by(Comment.id.desc()).all()
    # comments = Comment.query.all()
    form = CommentInput()
    if form.validate_on_submit():
        blog_id = id
        body = form.body.data
        blog_author = Article.query.get(blog_id).author
        comment = Comment(blog_id=blog_id, blog_author=blog_author, body=body)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('personal_page'))
    return render_template('blog-detail.html', article=article, form=form, comments=comments)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user, remember=True)
            # 设置session过期时间 过期时间一天
            # session.permanent = True
            # app = current_app._get_current_object()
            # app.permanent_session_lifetime = timedelta(days=1)
            return redirect(url_for('index'))
        elif not user:
            return redirect(url_for('error', type='User Not Found!'))
        else:
            return redirect(url_for('error', type='Password Error!'))
        # return redirect(url_for('login'))
    form.password.data = ''
    return render_template('login.html', form=form)


@app.route('/personal_page', methods=['GET', 'POST'])
def personal_page():
    form = DeleteNoteForm()
    # page = request.args.get('page', 1, type=int)
    # pagination = Article.query.order_by(Article.id.desc()).paginate(page=page, per_page=1000, error_out=False)
    # articles = pagination.items
    # return render_template('blog.html', personal_page=True, bootstrap=bootstrap, pagination=pagination, articles=articles, form=form)
    articles = Article.query.order_by(Article.id.desc()).all()
    # comments = Comment.query.filter( == )
    # query5 = db.session.query(Article, Comment).from_statement(text("select * from user where id>:value")).params(value=2).all()
    # comments = db.session().query(Article, Comment).join(Article.id == Comment.blog_id).filter(Article.author == current_user.username).all()
    if current_user.is_authenticated:
        comments = Comment.query.filter(Comment.blog_author == current_user.username).order_by(Comment.id.desc()).all()
    else:
        comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template('blog.html', personal_page=True, articles=articles, form=form, comments=comments)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/new_blog', methods=['GET','POST'])
def new():
    form = ArticleInput()
    if form.validate_on_submit():
        title = form.title.data
        author = current_user.username
        body = form.body.data
        article = Article(title=title, author=author, body=body)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_blog.html', form=form)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        flash('Your blog is deleted.')
    else:
        abort(400)
    return redirect(url_for('personal_page'))

@app.route('/error/<type>')
def error(type='404'):
    return render_template('404.html', type=type)