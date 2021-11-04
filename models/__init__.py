from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), index=True)
    author = db.Column(db.String(255), index=True)

    def __init__(self, title, author):
        self.title=title
        self.author=author

__all__ = [
    "db",
    "Book"
]