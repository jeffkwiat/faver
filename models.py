from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


# Model to store user details
class User(Base):

    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    favorites = db.relationship('Favorite', backref='favorite',
                                lazy='dynamic')


    def __repr__(self):
        return self.username


# Model for favorite photos
class Favorite(Base):
    user_id = db.Column(db.ForeignKey('user.id'))
    title = db.Column(db.String(500))
    link = db.Column(db.String(500))
    date_taken = db.Column(db.DateTime)
    published = db.Column(db.DateTime)
    author = db.Column(db.String(100))
    author_id = db.Column(db.String(50))
    tags = db.Column(db.String(50))

    def __repr__(self):
        return self.title

    # returns dictionary that can easily be jsonified
    def to_json(self):
        return {
                'title': self.title,
                'link': self.link,
                'date_taken': self.date_taken,
                'published': self.published,
                'author': self.author,
                'author_id': self.author_id,
                'tags': ', '.join(self.tags.split(' '))
            }