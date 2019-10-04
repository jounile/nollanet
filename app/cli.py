# coding=utf-8

import click
from flask import Flask
from flask_mysqldb import MySQL
from flask_cli import FlaskCLI
from flask_bcrypt import Bcrypt

from .config import DefaultConfig

app = Flask(__name__, instance_relative_config=True)

# DefaultConfig
app.config.from_object(DefaultConfig)

# Instance specific configurations
app.config.from_pyfile('config.py')

# Database connection
db = MySQL(app)

FlaskCLI(app)

# Encryption
bcrypt = Bcrypt(app)

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


