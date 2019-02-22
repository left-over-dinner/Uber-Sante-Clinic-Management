from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = 'patient'
    card_number = db.Column(db.String(250), primary_key=True)
    birth_day = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def __init__(self, card_number, birth_day, gender, phone_number, address, email):
        self.card_number = card_number
        self.birth_day = birth_day
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.email = email


class PatientSchema(ma.Schema):
    card_number = fields.String()
    # birth_day = fields.String()
    gender = fields.String()
    phone_number = fields.String()
    address = fields.String()
    email = fields.String()
