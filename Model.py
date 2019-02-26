from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


# ------------------------------- Patient start ------------------------------------
class Patient(db.Model):
    __tablename__ = 'patient'
    card_number = db.Column(db.String(250), primary_key=True)
    birth_day = db.Column(db.Date, nullable=False)
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
    birth_day = fields.Date()
    gender = fields.String()
    phone_number = fields.String()
    address = fields.String()
    email = fields.String()


# ------------------------------- Patient end ------------------------------------

# ------------------------------- Doctor start ------------------------------------
class Doctor(db.Model):
    __tablename__ = 'doctor'
    permit_number = db.Column(db.String(250), primary_key=True)
    last_name = db.Column(db.String(250), nullable=False)
    firs_name = db.Column(db.String(250), nullable=False)
    speciality = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)

    def __init__(self, permit_number, last_name, firs_name, speciality, city):
        self.permit_number = permit_number
        self.last_name = last_name
        self.firs_name = firs_name
        self.speciality = speciality
        self.city = city


class DoctorSchema(ma.Schema):
    permit_number = fields.String()
    last_name = fields.Date()
    firs_name = fields.String()
    speciality = fields.String()
    city = fields.String()


# ------------------------------- Doctor end ------------------------------------

# ------------------------------- Nurse start ------------------------------------
class Nurse(db.Model):
    __tablename__ = 'nurse'
    access_id = db.Column(db.String(250), primary_key=True)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, access_id, password):
        self.access_id = access_id
        self.password = password


class NurseSchema(ma.Schema):
    access_id = fields.String()
    password = fields.String()


# ------------------------------- Nurse end ------------------------------------

# ------------------------------- Appointment start ------------------------------------
class Appointment(db.Model):
    __tablename__ = 'appointment'
    patient_card_number = db.Column(db.String(250), db.ForeignKey('patient.card_number',
                                                                  ondelete='CASCADE'), primary_key=True)
    doctor_permit_number = db.Column(db.String(250), db.ForeignKey('doctor.permit_number',
                                                                   ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    slots = db.Column(db.JSON(), nullable=False)
    appointment_type = db.Column(db.String(250), nullable=False)

    def __init__(self, patient_card_number, doctor_permit_number, date, slots, appointment_type):
        self.patient_card_number = patient_card_number
        self.doctor_permit_number = doctor_permit_number
        self.date = date
        self.slots = slots
        self.appointment_type = appointment_type


class AppointmentSchema(ma.Schema):
    patient_card_number = fields.String()
    doctor_permit_number = fields.String()
    date = fields.Date()
    slots = fields.Raw()
    appointment_type = fields.String()


# ------------------------------- Appointment end ------------------------------------

# ------------------------------- Availability start ------------------------------------
class Availability(db.Model):
    __tablename__ = 'availability'
    id = db.Column(db.Integer, primary_key=True)
    doctor_permit_number = db.Column(db.String(250), db.ForeignKey('doctor.permit_number',
                                                                   ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    slots = db.Column(db.JSON(), nullable=False)

    def __init__(self, availability_id, doctor_permit_number, date, slots):
        self.availability_id = availability_id
        self.doctor_permit_number = doctor_permit_number
        self.date = date
        self.slots = slots


class AvailabilitySchema(ma.Schema):
    availability_id = fields.Int()
    doctor_permit_number = fields.String()
    date = fields.Date()
    slots = fields.Raw()


# ------------------------------- Nurse end ------------------------------------

