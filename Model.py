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
    last_name = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, card_number, birth_day, gender, phone_number, address, email, last_name, first_name, password):
        self.card_number = card_number
        self.birth_day = birth_day
        self.gender = gender
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.last_name = last_name
        self.first_name = first_name
        self.password = password
    
    @classmethod
    def createEmpty(cls):
        return cls("", None, "", "", "", "", "", "", "")

    def set_fields(self, fields_dictionary):
        fields = fields_dictionary.items()
        for key, value in fields:
            self.__setattr__(key, value)
        pass


class PatientSchema(ma.Schema):
    card_number = fields.String()
    birth_day = fields.Date()
    gender = fields.String()
    phone_number = fields.String()
    address = fields.String()
    email = fields.String()
    last_name = fields.String()
    first_name = fields.String()
    password = fields.String()


# ------------------------------- Patient end ------------------------------------

# ------------------------------- Doctor start ------------------------------------
class Doctor(db.Model):
    __tablename__ = 'doctor'
    permit_number = db.Column(db.String(250), primary_key=True)
    last_name = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    specialty = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'), nullable=False)

    def __init__(self, permit_number, last_name, first_name, specialty, location, email, password, clinic_id):
        self.permit_number = permit_number
        self.last_name = last_name
        self.first_name = first_name
        self.specialty = specialty
        self.location = location
        self.email = email
        self.password = password
        self.clinic_id = clinic_id
    
    @classmethod
    def createEmpty(cls):
        return cls("", "", "", "", "", "", "","")

    def set_fields(self, fields_dictionary):
        fields = fields_dictionary.items()
        for key, value in fields:
            self.__setattr__(key, value)
        pass


class DoctorSchema(ma.Schema):
    permit_number = fields.String()
    last_name = fields.String()
    first_name = fields.String()
    specialty = fields.String()
    location = fields.String()
    email = fields.String()
    password = fields.String()
    clinic_id = fields.Int()


# ------------------------------- Doctor end ------------------------------------

# ------------------------------- Nurse start ------------------------------------
class Nurse(db.Model):
    __tablename__ = 'nurse'
    access_id = db.Column(db.String(250), primary_key=True)
    password = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.clinic_id'), nullable=False)

    def __init__(self, access_id, password, last_name, first_name, email, clinic_id):
        self.access_id = access_id
        self.password = password
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.clinic_id = clinic_id

    @classmethod
    def createEmpty(cls):
        return cls("", "", "", "", "", "")

    def set_fields(self, fields_dictionary):
        fields = fields_dictionary.items()
        for key, value in fields:
            self.__setattr__(key, value)
        pass


class NurseSchema(ma.Schema):
    access_id = fields.String()
    password = fields.String()
    last_name = fields.String()
    first_name = fields.String()
    email = fields.String()
    clinic_id = fields.Int()


# ------------------------------- Nurse end ------------------------------------

# ------------------------------- Appointment start ------------------------------------
class Appointment(db.Model):
    __tablename__ = 'appointment'
    appointment_id = db.Column(db.INT(), primary_key=True, autoincrement=True)
    patient_card_number = db.Column(db.String(250), db.ForeignKey('patient.card_number',
                                                                  ondelete='CASCADE'), nullable=False)
    doctor_permit_number = db.Column(db.String(250), db.ForeignKey('doctor.permit_number',
                                                                   ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    slots = db.Column(db.JSON(), nullable=False)
    appointment_type = db.Column(db.String(250), nullable=False)

    def __init__(self,  patient_card_number, doctor_permit_number, date, slots, appointment_type):
        self.patient_card_number = patient_card_number
        self.doctor_permit_number = doctor_permit_number
        self.date = date
        self.slots = slots
        self.appointment_type = appointment_type


class AppointmentSchema(ma.Schema):
    appointment_id = fields.Int()
    patient_card_number = fields.String()
    doctor_permit_number = fields.String()
    date = fields.Date()
    slots = fields.Raw()
    appointment_type = fields.String()


# ------------------------------- Appointment end ------------------------------------

# ------------------------------- Availability start ------------------------------------
class Availability(db.Model):
    __tablename__ = 'availability'
    availability_id = db.Column(db.Integer, primary_key=True, )
    doctor_permit_number = db.Column(db.String(250), db.ForeignKey('doctor.permit_number',
                                                                   ondelete='CASCADE'), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    slots = db.Column(db.JSON(), nullable=False)

    def __init__(self, doctor_permit_number, date, slots):
        # this column is set to auto-increment by the database
        # it must not be supplied in the constructor
        #self.availability_id = availability_id
        self.doctor_permit_number = doctor_permit_number
        self.date = date
        self.slots = slots


class AvailabilitySchema(ma.Schema):
    availability_id = fields.Int()
    doctor_permit_number = fields.String()
    date = fields.Date()
    slots = fields.Raw()


# ------------------------------- Availability end ------------------------------------

# ------------------------------- Clinic start ------------------------------------
class Clinics(db.Model):
    __tablename__ = 'clinics'
    clinic_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    no_doctors = db.Column(db.INT(), nullable=False)
    no_nurses = db.Column(db.INT(), nullable=False)
    no_rooms = db.Column(db.INT(), nullable=False)
    schedule = db.Column(db.String(250), nullable=False)

    def __init__(self, clinic_id,name, no_doctors, no_nurses, no_rooms, schedule):
        # this column is set to auto-increment by the database
        # it must not be supplied in the constructor
        #self.clinic_id = clinic_id
        self.clinic_id=clinic_id
        self.name = name
        self.no_doctors = no_doctors
        self.no_nurses = no_nurses
        self.no_rooms = no_rooms
        self.schedule = schedule


class ClinicsSchema(ma.Schema):
    clinic_id = fields.Int()
    name = fields.String()
    no_doctors = fields.Int()
    no_nurses = fields.Int()
    no_rooms = fields.Int()
    schedule = fields.String()

# ------------------------------- Clinic end ------------------------------------
