from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
import requests, json, uuid

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, From, To)

from app.mod_auth.form import RegisterForm, ProfileForm

from app import app, db, utils
from app.models import User, LoggedInUser, PwdRecover, Links, LinkCategories
from app.mod_auth import bcrypt

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/register' , methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'GET':
        return render_template('auth/register.html', form=form)
    if request.method == 'POST' and form.validate():

        username = form.username.data
        password = form.password.data

        # Check if user exists
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            flash("Username " + username + " exists already.")
            return render_template('auth/register.html', form=form)
        else:
            crypted_password = bcrypt.generate_password_hash(password)
            date = datetime.today().strftime('%Y-%m-%d')
            login_count = 0
            try:
                newUser = User(date=date,
                    login_count=login_count,
                    name=form.name.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=crypted_password,
                    location=form.location.data,
                    address=form.address.data,
                    postnumber=form.postnumber.data,
                    level=5,
                    bornyear=form.bornyear.data,
                    gender=form.gender.data,
                    lang_id=1,
                    telephone='',
                    youtube='',
                    last_update=datetime.now(),
                    avatar=''
                    )

                db.session.add(newUser)
                db.session.commit()
                app.logger.info("User " + username + " was registered successfully")
                flash("User " + username + " has been registered.")
                return redirect(url_for("auth.login"))
            except Exception as e:
                app.logger.error('Registering user ' + username + ' failed. ' + str(e))
                return redirect(url_for("auth.register"))
    else:
        app.logger.info('Registration failed ' + str(form.errors))
        flash("Registration failed")
        return render_template("auth/register.html", form=form)

@mod_auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    if request.method == 'POST':

        username = request.form['username']
        usr_entered = request.form['password']

        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            flash("User " + username + " does not exist")
            return redirect(url_for('auth.login'))

        if user and bcrypt.check_password_hash(user.password, usr_entered):
            flash("Welcome " + user.username + "!")
            session['logged_in'] = True
            session['username'] = user.username
            session['user_id'] = user.id
            session['user_level'] = user.level
            app.logger.info('User ' + user.username + ' logged in.')

            # Increment login_count by one
            login_count = user.login_count + 1
            try:
                result = db.session.query(User).filter(User.username == username).update(dict(login_count=login_count, last_login=datetime.now()), synchronize_session=False)
                db.session.commit()
                app.logger.info("Incrementing login_count by one was successful")
            except Exception as e:
                app.logger.error("Incrementing login_count failed")

            # Add user to user_online table
            try:
                loggedInUser = LoggedInUser(user_id=user.id,
                            username=user.username,
                            created_time=datetime.now()
                        )
                db.session.add(loggedInUser)
                db.session.commit()
                app.logger.info("Adding to user_online table was successful")
            except Exception as e:
                app.logger.error("Adding to user_online table failed")
        else:
            flash("Wrong credentials!")

    return redirect(url_for('home'))

@mod_auth.route('/logout')
def logout():
    if session.get('logged_in'):
        app.logger.info('Logout user ' +  session.get('username') + '.')
        # Delete user from user_online table
        try:
            LoggedInUser.query.filter_by(username=session.get('username')).delete()
            db.session.commit()
            app.logger.info("Removing user from user_online table was successful")
        except Exception as e:
            app.logger.error("Removing user from user_online table failed")

        # Logout by deleting session data
        session['logged_in'] = False
        session.pop('username')
        session.pop('user_id')
        session.pop('user_level')

    return redirect(url_for('home'))

@mod_auth.route('/profile', methods=['GET','POST'])
def profile():
    if not session.get('logged_in'):
        flash('You are not logged in')
        return render_template('auth/login.html')
    else:
        form = ProfileForm()

        if request.method == 'GET':
            username = session.get('username')
            user = User.query.filter_by(username=username).first()

            form.id.data = user.id
            form.level.data = user.level
            form.username.data = user.username
            form.name.data = user.name
            form.bornyear.data = user.bornyear
            form.email.data = user.email
            form.homepage.data = user.homepage
            form.info.data = user.info
            form.location.data = user.location
            form.date.data = user.date
            form.hobbies.data = user.hobbies
            form.gender.process_data(user.gender) #selected
            form.last_login.data = user.last_login
            form.lang_id.process_data(user.lang_id) #selected
            form.login_count.data = user.login_count
            form.address.data = user.address
            form.postnumber.data = user.postnumber
            form.telephone.data = user.telephone
            form.youtube.data = user.youtube
            form.last_update.data = user.last_update
            form.avatar.data = user.avatar

            return render_template('auth/profile.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                user = {
                    'id': form.id.data,
                    'username': form.username.data,
                    'name': form.name.data,
                    'bornyear': form.bornyear.data,
                    'email': form.email.data,
                    'homepage': form.homepage.data,
                    'info': form.info.data,
                    'location': form.location.data,
                    'date': form.date.data,
                    'gender': form.gender.data,
                    'last_login': form.last_login.data,
                    'lang_id': form.lang_id.data,
                    'login_count': form.login_count.data,
                    'address': form.address.data,
                    'postnumber': form.postnumber.data,
                    'telephone': form.telephone.data,
                    'youtube': form.youtube.data,
                    'last_update': datetime.now(),
                    'avatar': form.avatar.data
                }
                form.update_details(user)
                app.logger.info('Updated user profile')
            else:
                app.logger.error("Form validation error")
            return redirect(url_for('auth.profile'))

@mod_auth.route('/pwdreset', methods=['GET','POST'])
def pwdreset():
    if request.method == 'GET':
        return render_template('auth/pwdreset.html')
    if request.method == 'POST':

        # Determine user type
        if session.get('logged_in'): # logged in user
            username = session.get('username')
        else: # anonymous user
            username = request.form.get('username')

        newpwd1 = request.form.get('newpwd1')
        newpwd2 = request.form.get('newpwd2')
        if newpwd1 == newpwd2:
            # Update password
            try:
                crypted_password = bcrypt.generate_password_hash(newpwd2)
                User.query.filter_by(username=username).update({"password": crypted_password})
                db.session.commit()
            except Exception as e:
                app.logger.error("Password update failed.")

            # Get token for user
            pwdrecover = PwdRecover.query.filter_by(username=username).first()
            if pwdrecover:
                # Remove token from database
                try:
                    PwdRecover.query.filter_by(token=pwdrecover.token).delete()
                    db.session.commit()
                except Exception as e:
                    app.logger.error("Failed to remove token from database.")
            else:
                app.logger.info("No token exists")

            flash('Your password was updated successfully.')
            return redirect(url_for('auth.logout'))
        else:
            return render_template('auth/pwdreset.html', error='You mistyped. Please try again.')
    else:
        flash('Please login first')
        return redirect(url_for('home'))

@mod_auth.route('/pwdrecover', methods=['GET','POST'])
def pwdrecover():
    if request.method == 'GET':
        return render_template('auth/pwdrecover.html')
    if request.method == 'POST':

        # Get entered username
        username = request.form.get('username')

        # Retrieve email address of the entered username
        user = User.query.filter_by(username=username).first()
        if user:
            # Generate a unique token
            token = str(uuid.uuid4())

            # Save the email & token & timestamp into database table pwdrecover
            try:
                newPwdRecover = PwdRecover(username=username, email=user.email, token=token)
                db.session.add(newPwdRecover)
                db.session.commit()
            except Exception as e:
                app.logger.error("Failed to save email, token and timestamp.")

            message = Mail(
                from_email=app.config.get('NOLLANET_EMAIL'),
                to_emails=user.email,
                subject='nolla.net - Change your password',
                html_content='Change your password <a href="' + request.url_root + 'auth/pwdchange/' + token + '" target="_blank">' + request.url_root + 'auth/pwdchange/' + token + '</a>')

            try:
                sg = SendGridAPIClient(app.config.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                flash('We have sent a temporary link to the email address defined in your user profile. Please follow the link and change your password.')
            except Exception as e:
                app.logger.error("Failed to send a temporary link via email")
        else:
            flash("Please try again.")

        return redirect(url_for('home'))

@mod_auth.route('/pwdchange/<token>', methods=['GET','POST'])
def pwdchange(token):
    if request.method == 'GET':
        # Check token exists
        pwdrecover = PwdRecover.query.filter_by(token=token).first()
        if pwdrecover:
            return render_template('auth/pwdreset.html', username=pwdrecover.username)
        else:
            flash('Token was not found in database')
            return redirect(url_for('home'))

    return redirect(url_for('home'))
