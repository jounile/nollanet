# coding=utf-8

import click
from flask import Flask
from flask_cli import FlaskCLI
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, Float, Boolean, MetaData

from .config import DefaultConfig

from models import StoryType, Genre, MediaType, Country

app = Flask(__name__, instance_relative_config=True)

# DefaultConfig
app.config.from_object(DefaultConfig)

# Instance specific configurations
app.config.from_pyfile('config.py')

# Database connection
db = SQLAlchemy(app)

FlaskCLI(app)

# Encryption
bcrypt = Bcrypt(app)

@app.cli.command("create_storytype")
def create_storytype():
        metadata = MetaData()
        data = Table('storytype', metadata,
                Column('id', Integer(), primary_key=True),
                Column('type_id', Integer()),
                Column('type_name', String(50))
        )
        metadata.create_all(db.engine)
        print(repr(data))

@app.cli.command("insert_storytypes")
def insert_types():
        model1 = StoryType(id=1, type_id=1, type_name='general')
        model2 = StoryType(id=2, type_id=2, type_name='reviews')
        model3 = StoryType(id=3, type_id=3, type_name='interviews')
        model4 = StoryType(id=4, type_id=4, type_name='news')
        model5 = StoryType(id=5, type_id=99, type_name='other')
        db.session.add(model1)
        db.session.add(model2)
        db.session.add(model3)
        db.session.add(model4)
        db.session.add(model5)
        db.session.commit()

@app.cli.command("create_genre")
def create_genre():
        metadata = MetaData()
        data = Table('genre', metadata,
                Column('id', Integer(), primary_key=True),
                Column('type_id', Integer()),
                Column('type_name', String(50))
        )
        metadata.create_all(db.engine)
        print(repr(data))

@app.cli.command("insert_genres")
def insert_types():
        model1 = Genre(id=1, type_id=1, type_name='skateboarding')
        model2 = Genre(id=2, type_id=2, type_name='snowboarding')
        model3 = Genre(id=3, type_id=3, type_name='nollagang')
        model4 = Genre(id=4, type_id=4, type_name='snowskate')
        db.session.add(model1)
        db.session.add(model2)
        db.session.add(model3)
        db.session.add(model4)
        db.session.commit()

@app.cli.command("create_mediatype")
def create_mediatype():
        metadata = MetaData()
        data = Table('mediatype', metadata,
                Column('id', Integer(), primary_key=True),
                Column('type_id', Integer()),
                Column('type_name', String(50))
        )
        metadata.create_all(db.engine)
        print(repr(data))

@app.cli.command("insert_mediatypes")
def insert_mediatypes():
        model1 = MediaType(id=1, type_id=1, type_name='photo')
        model2 = MediaType(id=2, type_id=2, type_name='mediatype2')
        model3 = MediaType(id=3, type_id=3, type_name='music')
        model4 = MediaType(id=4, type_id=4, type_name='movies')
        model5 = MediaType(id=5, type_id=5, type_name='stories') # interviews, reviews
        model6 = MediaType(id=6, type_id=6, type_name='video')
        db.session.add(model1)
        db.session.add(model2)
        db.session.add(model3)
        db.session.add(model4)
        db.session.add(model5)
        db.session.add(model6)
        db.session.commit()

@app.cli.command("create_countries")
def create_mediatype():
        metadata = MetaData()
        data = Table('countries', metadata,
                Column('id', Integer(), primary_key=True),
                Column('country_code', String(50)),
                Column('country_name', String(50))
        )
        metadata.create_all(db.engine)
        print(repr(data))

@app.cli.command("insert_countries")
def insert_mediatypes():
        model1 = Country(id=1, country_code='fi', country_name='Finland')
        model2 = Country(id=2, country_code='se', country_name='Sweden')
        model3 = Country(id=3, country_code='ee', country_name='Estonia')
        model4 = Country(id=4, country_code='dk', country_name='Denmark')
        model5 = Country(id=5, country_code='de', country_name='Germany')
        db.session.add(model1)
        db.session.add(model2)
        db.session.add(model3)
        db.session.add(model4)
        db.session.add(model5)
        db.session.commit()

"""
@app.cli.command("alter_database")
def alter_database():
    cursor = db.connection.cursor()
    cursor.execute("SELECT username, password FROM users WHERE password like 'hylätty_%' OR password IS NULL OR password = ''")
    result = cursor.fetchall()
    #print(result)
    cursor.execute("SET sql_mode = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION'")
    cursor.execute("ALTER TABLE users MODIFY COLUMN password varchar(60)")
    db.connection.commit()
    cursor.execute("DELETE FROM users WHERE password like 'hylätty_%' OR password IS NULL OR password = ''")
    cursor.execute("SELECT username, password FROM users WHERE password not like 'hylätty_%' AND password IS NOT NULL AND password != ''")
    result = cursor.fetchall()

    for user in result:
        username = user[0]
        password = user[1]

        crypted_password = bcrypt.generate_password_hash(password)
        print(crypted_password)
        
        cursor = db.connection.cursor()
        sql = "UPDATE users SET password=%s WHERE username=%s"
        cursor.execute(sql, (crypted_password, username))
        db.connection.commit()
"""
