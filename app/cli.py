# coding=utf-8

import click
from flask import Flask
from flask_cli import FlaskCLI
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, Float, Boolean, MetaData

from .config import DefaultConfig

from models import Storytype

app = Flask(__name__, instance_relative_config=True)

# DefaultConfig
app.config.from_object(DefaultConfig)

# Instance specific configurations
app.config.from_pyfile('config.py')

# Database connection
dba = SQLAlchemy(app)

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
        metadata.create_all(dba.engine)
        print(repr(data))

@app.cli.command("insert_types")
def insert_types():
        model1 = Storytype(id=1, type_id=1, type_name='general')
        model2 = Storytype(id=2, type_id=2, type_name='reviews')
        model3 = Storytype(id=3, type_id=3, type_name='interviews')
        model4 = Storytype(id=4, type_id=4, type_name='news')
        model5 = Storytype(id=5, type_id=99, type_name='other')
        dba.session.add(model1)
        dba.session.add(model2)
        dba.session.add(model3)
        dba.session.add(model4)
        dba.session.add(model5)
        dba.session.commit()

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
