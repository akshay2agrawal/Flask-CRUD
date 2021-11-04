# from app import db


# class Author(db.Model):
#     __tablename__ = "authors"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(255), index=True)
#     books = db.relationship('Book', backref='authors', lazy='dynamic')


from models import db


