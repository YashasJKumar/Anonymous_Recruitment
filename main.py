'''
Created on December 21, 2023,

Yashas J Kumar
'''

# ------------------------------------------- IMPORTS ------------------------------------------------------
import os
from questions_data import api_response
import random
import smtplib
from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from jinja2.nodes import Test
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
from functools import wraps
from dotenv import load_dotenv

#------------------------------------------- CONSTANTS -----------------------------------------------------

load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Initializing a new Flask Application __name__ ⇒ Root Path of the appln & tells where to find the requirements like temlates, static
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('KEY') # Security setting to manage sessions & cookies.
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<postgres_username>:<postgres_password>@localhost:5433/<DB_NAME>'
# Specifies the URl of the primary db to SQLAlchemy.

# Binds → bind multiple databases to a single Flask application.
# app.config['SQLALCHEMY_BINDS'] = {
#     'company': os.environ.get('C_DB'),
#     'tests': os.environ.get('T_DB'),
#     'written': os.environ.get('W_DB')
# }

"""
SQLAlchemy → SQLAlchemy is an Object Relational Mapper (ORM) that provides a high-level abstraction for interacting 
with databases, 
allowing us to work with database tables as Python classes and instances.
"""
db = SQLAlchemy()
db.init_app(app)  # Binding Flask app to SQLAlchemy so that it can manage database interactions within the context of the app.


# Configure Flask-Login's Login Manager → Manages USer auth & session management
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
# Critical for Flask-Login to manage User sessions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def company_login_required(function):
    def wrapper(*args, **kwargs):
        if 'c_name' in session:
            return function(*args, **kwargs)
        else:
            # Redirect to the login page or another appropriate page
            return redirect(url_for('sign_in_company'))

    return wrapper


# ---------------------------------------- DB Tables ------------------------------------------------------ #

"""
FUNDAMENTAL'S :

db.Model: This is a base class for all models in SQLAlchemy. By inheriting from db.Model, 
the User class is recognized as a table in the database, where each instance of User represents a row in that table.

UserMixin -> mixin class provided by Flask-Login. It provides default implementations for the methods that Flask-Login 
expects a user model to have, such as is_authenticated, is_active, is_anonymous, and get_id(). 

ORM Mapping: The User class is mapped to a database table where each attribute represents a column. SQLAlchemy uses this
 class to perform operations on the database, such as creating, reading, updating, and deleting user records.
"""
class User(UserMixin, db.Model):
    id = db.Column(db.String(20), primary_key=True, unique=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(120), nullable=False)
    # image = db.Column(db.BLOB, nullable=False)


class Company(db.Model, UserMixin):
    # __bind_key__ = 'company'
    # Optional Attribute → Telling SQLAlchemy that this model should use a specific database connection.

    c_name = db.Column(db.String(80), nullable=False, primary_key=True)
    c_email = db.Column(db.String(120, ), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    sector = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    mobile = db.Column(db.String(120), nullable=False)

    def get_id(self):
        return self.c_name


class Tests(UserMixin, db.Model):
    test_id = db.Column(db.String(20), primary_key=True, unique=True)
    company_name = db.Column(db.String(80), nullable=False, unique=True)
    c_sector = db.Column(db.String(80), nullable=False)
    c_email = db.Column(db.String(120, ), nullable=False, unique=True)
    c_url = db.Column(db.String(120), nullable=False)
    job_role = db.Column(db.String(80), nullable=False)
    skills = db.Column(db.String(120), nullable=False)
    lpa = db.Column(db.String(120), nullable=False)


class Written(UserMixin, db.Model):
    sl_no = db.Column(db.Integer, nullable=False, primary_key=True)
    c_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False)


"""
App Context: Certain operations, like creating or querying the database schema, require access to the Flask 
application’s configuration and context. 

db.create_all() needs to interact with the Flask app to get the database URI and other configurations.

db.create_all() examines the models you’ve defined (i.e., classes that inherit from db.Model) and generates the 
corresponding tables in the database. 
If a table already exists, it will not attempt to recreate it, making it a safe operation for initial setup.
"""

with app.app_context():
    db.create_all()


# FlaskForm -> Base class from Flask-WTF to handle form data, render forms, and perform validation.
class Exam_Form(FlaskForm):
    id = StringField('Enter your User ID: (YUNXXXX)', validators=[DataRequired()])
    get_otp = SubmitField('Get OTP')


class Otp_Form(FlaskForm):
    otp = StringField('Enter OTP', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/student/<username>')
@login_required
def student_home(username):
    return render_template('student_dashboard.html', username=username)


@app.route('/sign-in')
def sign_in():
    return render_template('signin.html')


@app.route('/student/sign-in', methods=['POST', 'GET'])
def student_sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar() # Retrieves a single result from the query. Since we expect only one user with a specific email,
        if not user:
            flash("That email does not exist, Please try again.")
            return redirect(url_for('student_sign_in'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, Please try again.')
            return redirect(url_for('student_sign_in'))
        else:
            login_user(user)
            return redirect(url_for('student_home', username=user.username))
    return render_template('sign_in_student.html')


@app.route('/company/<c_name>')
def company_home(c_name):
    if 'c_name' in session:
        return render_template('company_dashboard.html', c_name=session['c_name'])


@app.route('/company/sign-in/', methods=['GET', 'POST'])
def sign_in_company():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = db.session.execute(db.select(Company).where(Company.c_email == email))
        user = result.scalar()
        if not user:
            flash("That email does not exist, Please try again.")
            return redirect(url_for('sign_in_company'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, Please try again.')
            return redirect(url_for('sign_in_company'))
        else:
            session['c_name'] = user.c_name
            return redirect(url_for('company_home', c_name=user.c_name))
    return render_template('sign_in_company.html')


@app.route('/sign-up/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        dob = request.form['dob']
        mobile = request.form['mobile']
        role = request.form['role']

        if role == "company":
            result = db.session.execute(db.select(Company).where(Company.c_email == email))
            user = result.scalar()
            if user:
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('sign_in_company'))
            hash_and_salted_password = generate_password_hash(
                password=password,
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = Company(
                c_name=username, c_email=email, password=hash_and_salted_password,
                address=address, mobile=mobile, sector=request.form['companySector']
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('sign_in_company'))

        elif role == "applicant":
            result = db.session.execute(db.select(User).where(User.email == email))
            user = result.scalar()
            if user:
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('student_sign_in'))
            hash_and_salted_password = generate_password_hash(
                password=password,
                method='pbkdf2:sha256',
                salt_length=8
            )
            # Generate ID
            id = generate_unique_id()
            new_user = User(
                id=id, username=username, email=email,
                password=hash_and_salted_password, address=address, mobile=mobile, dob=dob
            )
            db.session.add(new_user)
            message = (f"Subject: Welcome to Yunigma!\n\n Hello {username} \n Your ID is {id}\n"
                       f"Please keep this unique id confidential & and do not share it with anyone.\n"
                       f"If you have any concerns about the security of your account or suspect any unauthorized activity,"
                       f"please contact our support team immediately.\n"
                       f"Feel free to reach out to our support team at [support@email.com]"
                       f"Best regards,\n\n Team Yunigma.")
            send_mail(to=email, subject=message)
            db.session.commit()
            return redirect(url_for('student_sign_in'))

    return render_template('signup.html')


@app.route('/exam-page/<c_name>', methods=['GET', 'POST'])
@login_required
def exam_page(c_name):
    exam_form = Exam_Form()
    if exam_form.validate_on_submit():
        user_id = exam_form.id.data
        has_written = Written.query.filter_by(user_id=user_id, c_name=c_name).first()
        user = db.get_or_404(User, user_id)
        user_email = user.email
        user = User.query.filter_by(email=user_email).first()
        if has_written:
            flash("You have already written this exam!")
            return redirect(url_for('exam_page', c_name=c_name))
        session['c_name'] = c_name
        generated_otp = random.randint(100000, 9999999)
        with open("generated_otp.txt", "w") as otp_file:
            otp_file.write(str(generated_otp))
        message = (f'Subject:Yunigma Mailing Services\n\n OTP Generated\n\n'
                   f'Your otp is: {generated_otp}\n Valid only for 1min.')
        send_mail(user_email, message)
        return redirect(url_for('generated_otp'))
    return render_template("index.html", exam_form=exam_form)


@app.route('/logout')
def logout():
    if 'c_name' in session:
        session.pop('c_name', None)
    else:
        logout_user()
    return redirect(url_for('home'))


@app.route('/about/')
def about_page():
    if current_user.is_authenticated:
        return render_template('about.html', user=current_user.username)
    elif 'c_name' in session:
        return render_template('about.html', cname=session['c_name'])
    else:
        return render_template('about.html')


@app.route('/quiz/', methods=['GET', 'POST'])
@login_required
def index():
    user_id = current_user.id
    result = db.session.execute(db.select(User).where(User.id == user_id))
    user = result.scalar()
    username = user.username
    if request.method == 'POST':
        # Process the form submission and calculate the score
        user_answers = {key: request.form[key] for key in request.form}
        score = calculate_score(user_answers)
        with open("./count.txt", "r") as file:
            count = int(file.read())
            sl_no = count + 1
        with open("./count.txt", "w") as file:
            file.write(str(sl_no))
        c_name = session['c_name']
        new_writer = Written(user_id=user_id, sl_no=sl_no, c_name=c_name, score=score)
        db.session.add(new_writer)
        db.session.commit()
        if score > 10:
            message = ("Subject:Congratulations!\n\n You have successfully passed the assessment\n"
                       "Use this link: at DD/MM/YYYY HH: to continue in your interview process.")
            send_mail(to=user.email, subject=message)
            written_user_row = Written.query.filter_by(user_id=user_id, c_name=c_name).first()
            company_row = Tests.query.filter_by(company_name=c_name).first()
            c_email = company_row.c_email
            message = (f"Subject:New Applicant\n\n A new user passed the assessment.\n"
                       f"User Id: {user_id}\n\n Score: {score}")
            send_mail(to=c_email, subject=message)
        return render_template('result.html', score=score, total_questions=len(api_response), username=username)
    elif request.method == 'GET':
        return render_template('quiz.html', questions=api_response, username=username)


def calculate_score(user_answers):
    correct_answers, i = 0, 0
    for c_ans in user_answers.values():
        if c_ans == api_response[i]['correct_answer']:
            correct_answers += 1
        i += 1
    return correct_answers


@app.route('/otp', methods=['GET', 'POST'])
@login_required
def generated_otp():
    if request.method == 'GET':
        return render_template('otp.html', form=Otp_Form())
    elif request.method == 'POST':
        with open("generated_otp.txt", 'r') as f:
            generated_otp = int(f.read())
        otp = request.form['otp']
        if int(otp) == int(generated_otp):
            return redirect(url_for('index'))
        else:
            return f"<h1>Invalid OTP!</h1>"


@app.route('/user/<username>/jobs')
@login_required
def jobs(username):
    results = db.session.execute(db.select(Tests)).scalars()
    all_jobs = []

    for result in results:
        job = []
        job.append(result.company_name)
        job.append(result.skills)
        job.append(result.job_role)
        job.append(result.lpa)
        all_jobs.append(job)
    all_jobs.reverse()  # To render the newly created job first.
    return render_template("jobs.html", username=username, all_jobs=all_jobs)


@app.route('/company/hire', methods=['GET', 'POST'])
def hire():
    if request.method == 'POST':
        c_name = request.form['companyName']
        c_sector = request.form['companySector']
        c_url = request.form['c_url']
        c_email = request.form['c_email']
        job_role = request.form['jobRole']
        skills = request.form['skills']
        lpa = request.form['annualPackage'].strip()
        test_id = generate_test_id()

        new_test = Tests(company_name=c_name, job_role=job_role,
                         skills=skills, lpa=lpa, test_id=test_id, c_sector=c_sector,
                         c_url=c_url, c_email=c_email
                         )
        db.session.add(new_test)
        db.session.commit()
        cname = session['c_name']
        return redirect('/company/' + cname)
    return render_template("hire_new.html")


@app.route('/student/skills', methods=['GET', 'POST'])
def skills():
    if request.method == 'POST':
        skills = request.form['skills']
    # Method not implemented currently.
    return render_template("enter_skills.html")


def generate_unique_id():
    unique_id = ""
    with open('unique_id.txt', 'r') as unique_id_file:
        prev_id = int(unique_id_file.read())
        prev_id += 1
        unique_id = "YUN" + str(prev_id)
    with open('unique_id.txt', 'w') as unique_id_file:
        unique_id_file.write(str(prev_id))

    return unique_id


def generate_test_id():
    test_id = "TEST"
    with open("./test_id.txt", "r") as id_file:
        prev_no = int(id_file.read())
        cur_no = prev_no + 1
        test_id += str(cur_no)

    # Updating the file.
    with open("./test_id.txt", "w") as id_file:
        id_file.write(str(cur_no))

    return test_id


def send_mail(to, subject):
    with smtplib.SMTP('smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(
            from_addr=EMAIL,
            to_addrs=to,
            msg=subject
        )


if __name__ == '__main__':
    app.run(debug=False)

