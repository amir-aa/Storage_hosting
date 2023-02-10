from flask import Flask,request,Blueprint,redirect,url_for,jsonify,render_template,session,redirect,send_file,flash
from flask_login import *
import models
from hashlib import pbkdf2_hmac
app=Flask(__name__)
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
app.config['SECRET_KEY'] = "incom.PayandebadMihanamEy#khaake@Iran2092!!!"

@login_manager.user_loader
def User_loader(email):
    udata=models.Users.select().where(models.Users.Email==email)
    if email not in udata[0].Email:
        return
    user=models.Users()
    user.Email=email
    return user


@app.route('/')
def main():
    return render_template('storage.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    if request.method=='POST':
        user=models.Users().select().where(models.Users.Email=='aainfoira@gmail.com')
        if user[0].Email ==request.form['username'] and user[0].Password==pbkdf2_hmac('sha256',request.form['passw'].encode(),b'S@lT1',9000).hex():
            login_user(user[0],True)
            return redirect(url_for('main'))
        else:
            flash('Unable to Login. Email or Password is incorrect!')
    return render_template('login.html')

app.run()