from flask import Flask, render_template, request, session, redirect, url_for
import models 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'\x85\x8ec\xb9\x81`\xf9k2H\x8b\xb0\x7f\x13\x1c:@\xa2\xb0\xf3:\xe2\x8b\x93'
db = SQLAlchemy(app)

from flask import Flask

app = Flask(__name__) # create a flask app named app
@app.route("/")
def home():
    return '''My name is Yomi Vigo. This is my CA2 work.
     My GitHub URL is https://github.com/yomivigo'''
    # In the return statement above, Use your own name and GitHub URL

@app.route("/process-signup/", methods=['POST'])
def process_signup():
 # Let's get the request object and extract the parameters sent into local variables.
 firstname = request.form['firstname']
 lastname = request.form['lastname']
 dob = request.form['dob']
 address = request.form['address']
 NIN = request.form['NIN']
 # let's write to the database
 try:
     user = models.User(firstname=firstname, lastname=lastname, dob=dob, address=address, NIN=NIN)
     db.session.add(user)
     db.session.commit()

 except Exception as e:
     # Error caught, prepare error information for return
     information = 'Could not submit. The error message is {}'.format(e.__cause__)
     return render_template('form.html', title="SIGN-UP", information=information)

 # If we have gotten to this point, it means that database write has been successful. Let us compose success info

 # Let us prepare success feedback information

 information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname,
                                                                                                       lastname, dob)

 return render_template('form.html', title="SIGN-UP", information=information)

if __name__ == "__main__":
 app.run(port=5005)