from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    # import the database connection
    # import JASON columns specifically due to unstability of Postgres/ SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    # run the first time we create a new result
    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    # represent the object when we query for it
    def __repr__(self):
        return '<id {}>'.format(self.id)