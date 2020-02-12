from datetime import datetime
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import requests, json
from app.mod_auth.form import RegisterForm, ProfileForm

from app import app, dba
from app.models import User
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
            form.date.data = user.date
            form.last_login.data = user.last_login
            form.name.data = user.name
            form.email.data = user.email
            form.location.data = user.location
            form.address.data = user.address
            form.postnumber.data = user.postnumber
            form.bornyear.data = user.bornyear
            form.email2.data = user.email2
            form.homepage.data = user.homepage
            form.info.data = user.info
            form.hobbies.data = user.hobbies
            form.extrainfo.data = user.extrainfo
            form.sukupuoli.data = user.sukupuoli
            form.sukupuoli.process_data(user.sukupuoli) #selected
            form.icq.data = user.icq
            form.apulainen.data = user.apulainen
            form.chat.data = user.chat
            form.oikeus.data = user.oikeus
            form.lang_id.data = user.lang_id
            form.lang_id.process_data(user.lang_id) #selected
            form.login_count.data = user.login_count
            form.emails.data = user.emails
            form.puhelin.data = user.puhelin
            form.blogs.data = user.blogs
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
                    'username': form.username.data,
                    'name': form.name.data,
                    'email': form.email.data,
                    'location': form.location.data,
                    'address': form.address.data,
                    'postnumber': form.postnumber.data,
                    'bornyear': form.bornyear.data,
                    'email2': form.email2.data,
                    'homepage': form.homepage.data,
                    'info': form.info.data,
                    'hobbies': form.hobbies.data,
                    'extrainfo': form.extrainfo.data,
                    'sukupuoli': form.sukupuoli.data,
                    'icq': form.icq.data,
                    'apulainen': form.apulainen.data,
                    'chat': form.chat.data,
                    'oikeus': form.oikeus.data,
                    'lang_id': form.lang_id.data,
                    'login_count': form.login_count.data,
                    'emails': form.emails.data,
                    'puhelin': form.puhelin.data,
                    'blogs': form.blogs.data,
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

            else:
                print("Form validation error")
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
    if session.get('logged_in'):
        if request.method == 'GET':
            return render_template('auth/pwdreset.html')
        if request.method == 'POST':
            username = session['username']
            newpwd1 = request.form.get('newpwd1')
            newpwd2 = request.form.get('newpwd2')
            if newpwd1 == newpwd2:
                crypted_password = bcrypt.generate_password_hash(newpwd2)
                User.query.filter_by(username=username).update({"password": crypted_password})
                dba.session.commit()
                flash('Your password was updated successfully.')
                return redirect(url_for('home'))
            else:
                return render_template('auth/pwdreset.html', error='You mistyped. Please try again.')
    else:
        flash('You are not logged in as administrator')
        return redirect(url_for('home'))
