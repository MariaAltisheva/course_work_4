from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favourite_genre = db.Column(db.String(255))



class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Str()
