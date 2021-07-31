from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')

db = SQLAlchemy(app)

db.init_app

class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)

    meaning = db.Column(db.String(255))
    paradigm = db.Column(db.String(255))

    singular_id = db.Column(db.ForeignKey('nominalnumber.id'))
    dual_id = db.Column(db.ForeignKey('nominalnumber.id'))
    plural_id = db.Column(db.ForeignKey('nominalnumber.id'))

    singular = db.relationship('NominalNumber', foreign_keys=singular_id, backref='singular')
    dual = db.relationship('NominalNumber', foreign_keys=dual_id, backref='dual')
    plural = db.relationship('NominalNumber', foreign_keys=plural_id, backref='plural')

class NominalNumber(db.Model):
    __tablename__ = 'nominalnumber'
    id = db.Column(db.Integer, primary_key=True)

    nominative = db.Column(db.String(255))
    genitive = db.Column(db.String(255))
    dative = db.Column(db.String(255))
    accusative = db.Column(db.String(255))
    vocative = db.Column(db.String(255))
    

class Verb(db.Model):
    __tablename__ = 'verb'
    id = db.Column(db.Integer, primary_key=True)

    meaning = db.Column(db.String(255))
    paradigm = db.Column(db.String(255))

    present_id = db.Column(db.ForeignKey('tense.id'))
    imperfect_id = db.Column(db.ForeignKey('tense.id'))
    future_id = db.Column(db.ForeignKey('tense.id'))
    aorist_id = db.Column(db.ForeignKey('tense.id'))
    perfect_id = db.Column(db.ForeignKey('tense.id'))
    pluperfect_id = db.Column(db.ForeignKey('tense.id'))

    present = db.relationship('Tense', foreign_keys=present_id, backref='present')
    imperfect = db.relationship('Tense', foreign_keys=imperfect_id, backref='imperfect')
    future = db.relationship('Tense', foreign_keys=future_id, backref='future')
    aorist = db.relationship('Tense', foreign_keys=aorist_id, backref='aorist')
    perfect = db.relationship('Tense', foreign_keys=perfect_id, backref='perfect')
    pluperfect = db.relationship('Tense', foreign_keys=pluperfect_id, backref='pluperfect')

class Tense(db.Model):
    __tablename__ = 'tense'
    id = db.Column(db.Integer, primary_key=True)

    infinitive_id = db.Column(db.ForeignKey('infinitive.id'))
    participle_id = db.Column(db.ForeignKey('participle.id'))
    indicative_id = db.Column(db.ForeignKey('mood.id'))
    optative_id = db.Column(db.ForeignKey('mood.id'))
    subjunctive_id = db.Column(db.ForeignKey('mood.id'))
    imperative_id = db.Column(db.ForeignKey('mood.id'))

    infinitive = db.relationship('Infinitive', foreign_keys=infinitive_id, backref='infinitive')
    participle = db.relationship('Participle', foreign_keys=participle_id, backref='participle')
    indicative = db.relationship('Mood', foreign_keys=indicative_id, backref='indicative')
    optative = db.relationship('Mood', foreign_keys=optative_id, backref='optative')
    subjunctive = db.relationship('Mood', foreign_keys=subjunctive_id, backref='subjunctive')
    imperative = db.relationship('Mood', foreign_keys=imperative_id, backref='imperative')

class Infinitive(db.Model):
    __tablename__ = 'infinitive'
    id = db.Column(db.Integer, primary_key=True)

    active = db.Column(db.String(255))
    middle = db.Column(db.String(255))
    passive = db.Column(db.String(255))

class Participle(db.Model):
    __tablename__ = 'participle'
    id = db.Column(db.Integer, primary_key=True)

    active_id = db.Column(db.ForeignKey('participlevoice.id'))
    middle_id = db.Column(db.ForeignKey('participlevoice.id'))
    passive_id = db.Column(db.ForeignKey('participlevoice.id'))

    active = db.relationship('ParticipleVoice', foreign_keys=active_id, backref='active')
    middle = db.relationship('ParticipleVoice', foreign_keys=middle_id, backref='middle')
    passive = db.relationship('ParticipleVoice', foreign_keys=passive_id, backref='passive')

class ParticipleVoice(db.Model):
    __tablename__ = 'participlevoice'
    id = db.Column(db.Integer, primary_key=True)

    masculine_id = db.Column(db.ForeignKey('word.id'))
    feminine_id = db.Column(db.ForeignKey('word.id'))
    neuter_id = db.Column(db.ForeignKey('word.id'))

    masculine = db.relationship('Word', foreign_keys=masculine_id, backref='masculine')
    feminine = db.relationship('Word', foreign_keys=feminine_id, backref='feminine')
    neuter = db.relationship('Word', foreign_keys=neuter_id, backref='neuter')

class Mood(db.Model):
    __tablename__ = 'mood'
    id = db.Column(db.Integer, primary_key=True)

    active_id = db.Column(db.ForeignKey('voice.id'))
    middle_id = db.Column(db.ForeignKey('voice.id'))
    passive_id = db.Column(db.ForeignKey('voice.id'))

    active = db.relationship('Voice', foreign_keys=active_id, backref='active')
    middle = db.relationship('Voice', foreign_keys=middle_id, backref='middle')
    passive = db.relationship('Voice', foreign_keys=passive_id, backref='passive')

class Voice(db.Model):
    __tablename__ = 'voice'
    id = db.Column(db.Integer, primary_key=True)

    singular_id = db.Column(db.ForeignKey('verbalnumber.id'))
    dual_id = db.Column(db.ForeignKey('verbalnumber.id'))
    plural_id = db.Column(db.ForeignKey('verbalnumber.id'))

    singular = db.relationship('VerbalNumber', foreign_keys=singular_id, backref='singular')
    dual = db.relationship('VerbalNumber', foreign_keys=dual_id, backref='dual')
    plural = db.relationship('VerbalNumber', foreign_keys=plural_id, backref='plural')

class VerbalNumber(db.Model):
    __tablename__ = 'verbalnumber'
    id = db.Column(db.Integer, primary_key=True)

    first = db.Column(db.String(255))
    second = db.Column(db.String(255))
    third = db.Column(db.String(255))












