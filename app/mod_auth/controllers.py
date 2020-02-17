from datetime import datetime

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import requests, json, uuid

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, From, To)

from app.mod_auth.form import RegisterForm, ProfileForm

from app import app, dba
from app.models import User, PwdRecover
from app.mod_auth import bcrypt

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/register' , methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

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
                    level=2,
                    bornyear='',
                    sukupuoli='',
                    oikeus='',
                    lang_id='',
                    lastloginip='',
                    lastloginclient='',
                    emails='',
                    puhelin='',
                    kantaasiakasnro='',
                    lamina_lisatieto='',
                    blogs='',
                    user_showid='',
                    messenger='',
                    myspace='',
                    rss='',
                    youtube='',
                    ircgalleria='',
                    last_profile_update='',
                    avatar='',
                    flickr_username=''
                    )

                dba.session.add(newUser)
                dba.session.commit()

                flash("User " + username + " has been registered.")
            except Exception as e:
                print(e)
            return redirect(url_for("home"))
    else:
        print("Invalid form data")

    return render_template('auth/register.html', form=form)

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
            session['user_id'] = user.user_id
            session['user_level'] = user.level

            # Increment login_count by one
            login_count = user.login_count + 1
            try:
                result = dba.session.query(User).filter(User.username == username).update(dict(login_count=login_count), synchronize_session=False)
                dba.session.commit()
            except Exception as e:
                print(e)
        else:
            flash("Wrong credentials!")

    return redirect(url_for('home'))

@mod_auth.route('/logout')
def logout():
    if session.get('logged_in'):
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

            form.user_id.data = user.user_id
            form.username.data = user.username
            form.name.data = user.name
            form.bornyear.data = user.bornyear
            form.email.data = user.email
            form.email2.data = user.email2
            form.homepage.data = user.homepage
            form.info.data = user.info
            form.location.data = user.location
            form.date.data = user.date
            form.hobbies.data = user.hobbies
            # open
            form.extrainfo.data = user.extrainfo
            form.sukupuoli.process_data(user.sukupuoli) #selected
            form.icq.data = user.icq
            form.apulainen.data = user.apulainen
            form.last_login.data = user.last_login
            form.chat.data = user.chat
            form.oikeus.data = user.oikeus
            form.lang_id.process_data(user.lang_id) #selected
            form.login_count.data = user.login_count
            # lastloginip
            # lastloginclient
            form.address.data = user.address
            form.postnumber.data = user.postnumber
            form.emails.data = user.emails
            form.puhelin.data = user.puhelin
            # kantaasiakasnro
            # lamina_lisatieto
            form.blogs.data = user.blogs
            # user_showid
            # blog_level
            # last_login2
            form.messenger.data = user.messenger
            form.myspace.data = user.myspace
            form.rss.data = user.rss
            form.youtube.data = user.youtube
            form.ircgalleria.data = user.ircgalleria
            form.last_profile_update.data = user.last_profile_update
            form.avatar.data = user.avatar
            form.flickr_username.data = user.flickr_username

            return render_template('auth/profile.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                user = {
                    'user_id': form.user_id.data,
                    'username': form.username.data,
                    'name': form.name.data,
                    'bornyear': form.bornyear.data,
                    'email': form.email.data,
                    'email2': form.email2.data,
                    'homepage': form.homepage.data,
                    'info': form.info.data,
                    'location': form.location.data,
                    'date': form.date.data,
                    'hobbies': form.hobbies.data,
                    # open
                    'extrainfo': form.extrainfo.data,
                    'sukupuoli': form.sukupuoli.data,
                    'icq': form.icq.data,
                    'apulainen': form.apulainen.data,
                    'last_login': form.last_login.data,
                    'chat': form.chat.data,
                    'oikeus': form.oikeus.data,
                    'lang_id': form.lang_id.data,
                    'login_count': form.login_count.data,
                    # lastloginip
                    # lastloginclient
                    'address': form.address.data,
                    'postnumber': form.postnumber.data,
                    'emails': form.emails.data,
                    'puhelin': form.puhelin.data,
                    # kantaasiakasnro
                    # lamina_lisatieto
                    'blogs': form.blogs.data,
                    # user_showid
                    # blog_level
                    # last_login2
                    'messenger': form.messenger.data,
                    'myspace': form.myspace.data,
                    'rss': form.rss.data,
                    'youtube': form.youtube.data,
                    'ircgalleria': form.ircgalleria.data,
                    'last_profile_update': datetime.now(),
                    'avatar': form.avatar.data,
                    'flickr_username': form.flickr_username.data
                }
                form.update_details(user)
                print("Form update details")
            else:
                print("Form validation error", form.errors)
            return redirect(url_for('auth.profile'))

@mod_auth.route('/admin')
def admin():
    if session.get('logged_in') and session.get('user_level') == 1:    
        return render_template('auth/admin.html')
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))

@mod_auth.route('/promote', methods=['GET','POST'])
def promote():
    if session.get('logged_in') and session.get('user_level') == 1:
        if request.method == 'GET':
            return render_template('auth/promote.html')
        if request.method == 'POST':
            username = request.form.get('username')
            level = request.form.get('level')
            User.query.filter_by(username=username).update({"level": level})
            dba.session.commit()
            flash('User '+ username + ' is now updated to level ' + level + '.')
            return redirect(url_for('home'))
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))

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
                dba.session.commit()
            except Exception as e:
                print(str(e))

            # Get token for user
            pwdrecover = PwdRecover.query.filter_by(username=username).first()
            if pwdrecover:
                # Remove token from database
                try:
                    PwdRecover.query.filter_by(token=pwdrecover.token).delete()
                    dba.session.commit()
                except Exception as e:
                    print(str(e))
            else:
                print("No token exists")

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
                dba.session.add(newPwdRecover)
                dba.session.commit()
            except Exception as e:
                print(str(e))

            message = Mail(
                from_email=app.config.get('NOLLANET_EMAIL'),
                to_emails=user.email,
                subject='nolla.net - Change your password',
                html_content='Change your password <a href="' + request.url_root + 'auth/pwdchange/' + token + '" target="_blank">' + request.url_root + 'auth/pwdchange/' + token + '</a>')

            try:
                sg = SendGridAPIClient(app.config.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                #print(response.status_code)
                #print(response.body)
                #print(response.headers)
                #print('Password reset email was sent succesfully.')
                flash('We have sent a temporary link to the email address defined in your user profile. Please follow the link and change your password.')
            except Exception as e:
                print(str(e))
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
