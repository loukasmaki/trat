import os
import functools

from flask import Flask, render_template, redirect, url_for, request, flash, session, g
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )
    # SECRET_KEY and dev is worrying me

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .models import db, Attendee, Training_day, User

    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    migrate = Migrate(app, db)


    def require_login(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if not g.user:
                return redirect(url_for('log_in'))
            return view(**kwargs)
        return wrapped_view

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.before_request
    def load_user():
        user_id = session.get('user_id')
        if user_id:
            g.user = User.query.get(user_id)
        else:
            g.user = None

    @app.route('/')
    @require_login
    def index():
        return redirect(url_for('register'))


    @app.route('/register', methods=('GET', 'POST'))
    @require_login
    def register():
        if request.method == 'POST':
            name = request.form['name']
            date = request.form['date']
            weapon = request.form['weapon']
            error = None

            if not name:
                error = 'Namn saknas'

            if error is None:
                print(f"I got this: {Attendee.query.filter_by(name=name).first() }")
                test = Attendee.query.filter_by(name=name).first()
                if test is None:
                    attendee = Attendee(name=name)
                else:
                    attendee = Attendee.query.filter_by(name=name).first()

                training_session = Training_day(date=date, weapon=weapon)
                training_session.attendees.append(attendee)
                db.session.add(training_session)
                db.session.commit()
                flash(f"Successfully registered { name } attendance. Welcome!")
                return redirect(url_for('register'))

            flash(error, 'error')

        return render_template('register.html')

    @app.route('/admin', methods=('GET','POST'))
    @require_login
    def admin():
        role = []
        print(request.form)
        if request.method == 'POST':

            role.append(request.form['role'])

            if error is None:
                print(role)


        return render_template('admin.html', users = User.query.all())

    @app.route('/log_in', methods=('GET', 'POST'))
    def log_in():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            user = User.query.filter_by(username=username).first()

            if not user or not check_password_hash(user.password, password):
                error = 'Username or password is incorrect'

            if error is None:
                session.clear()
                session['user_id'] = user.id
                return redirect (url_for('register'))

            flash(error, 'error')

        return render_template('log_in.html')

    @app.route('/log_out', methods=('GET', 'DELETE'))
    def log_out():
        session.clear()
        flash('Successfully logged out', 'success')
        return redirect(url_for('log_in'))

    @app.route('/sign_up', methods=('GET', 'POST'))
    def sign_up():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            if not username:
                error = 'Username is required'
            elif not password:
                error = 'Password is required'
            elif User.query.filter_by(username=username).first():
                error = 'Username is already taken'

            if error is None:
                user = User(username=username, password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                flash('Successfully signed up. Please log in', 'success')
                return redirect(url_for('log_in'))

            flash(error, 'error')
        return render_template('sign_up.html')







    return app
