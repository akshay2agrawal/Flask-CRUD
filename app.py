import os
from os.path import dirname, abspath

from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect

from models import *

def create_app(config_filename):
    app = Flask(__name__,template_folder="templates")
    db.init_app(app)
    app.config.from_pyfile(config_filename)
    return app

def config_file():
    return os.path.join(dirname(abspath(__name__)), 'config.cfg')

def run():
    app = create_app(config_file())
    app_host = "localhost"

    app_port = 5000
    db.init_app(app)
    @app.route('/', methods=['GET', 'POST'])
    def index():

        if (request.method=="POST"):
            book = Book(title=request.form.get('title'),author=request.form.get('author'), )
            db.session.add(book)
            db.session.commit()
        books = Book.query.all()
        return render_template("index.html", books=books)

    @app.route('/delete/<int:id>', methods=['GET'])
    def delete(id):

        book= Book.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit()
        books = Book.query.all()
        return render_template("index.html", books=books)


    @app.route('/update/<int:id>', methods=['GET', "POST"])
    def update(id):
        book= Book.query.filter_by(id=id).first()
        if (request.method=="GET"):

            return render_template("update.html", book=book)

        elif (request.method=="POST"):
            title = request.form.get("title")
            author = request.form.get("author")
            book.title = title
            book.author = author
            db.session.commit()
            return  redirect(url_for('index'))

    app.run(debug=True, host=app_host, port=app_port)


def db_init():
    from flask_sqlalchemy import SQLAlchemy

    print("> init DB ")

    app = create_app(config_file())


    from models import db

    db.init_app(app)
    app.test_request_context().push()
    db.create_all()

    db.session.commit()

    # run_role_permission_seeder(db)
    # run_user_seeder(db)

    # try:
    #     db.session.commit()
    # except IntegrityError:
    #     print("already seeded")

    print("> OK init")

run()