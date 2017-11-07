from flask import Flask, render_template, session, redirect, request, url_for
import os
import models as db

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    message = None
    """
     if request.method == 'POST':
        username= request.form['username']
        password = request.form['password']
        #if enterd username exists
        if db.userExists(username) == True:
            if db.getPassword(username) == password:
                session['username'] = username
                return redirect(url_for('user'))
            else:
                message = "INVALID PASSWORD"
                return render_template('index.html')
    """

    return render_template('index.html', message = message)
@app.route('/registration', methods=['GET', "POST"])
def registeraion():
    messages = []
    if request.method== 'POST':
        username = request.form['username']
        password= request.form['password']
        if len(username)<4:
            messages.append("Invalid username. Username must be between at leat 4 characters in length!")
        if len(username)>20:
            messages.append("Invalid Username. Your username is too long , Please use 20 characters maximum ")

        if len(password) < 4:
            messages.append("Invalid Password. Username must be between at leat 4 characters in length!")
        if len(password) > 20:
            messages.append("Invalid Password. Your username is too long , Please use 20 characters maximum ")
        if len(messages)!= 0:
            return render_template('registeration.html', messages = messages)

        if db.userExists(username) == True:
            messages.append("Username already exists!!")
            return render_template('registeration.html', messages = messages)
        else:
            db.insertUser(username, password)
            session['username'] = username
            return redirect(url_for('user'))
    else:
        return render_template('registeration.html', messages = messages)



if __name__ == '__main__':
    app.run(debug=True)
