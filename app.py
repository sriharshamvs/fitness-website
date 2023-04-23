from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from models import db, User, Plan

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['WTF_CSRF_ENABLED'] = True
csrf = CSRFProtect(app)

# Initialize the Flask-Login extension
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# SQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness-hub.db'

db.init_app(app)
migrate = Migrate(app, db)


def seed_plans():
    plans = [
        {'name': 'Basic Plan', 'price': 19.99,
            'description': 'Access to our workout library and basic diet plans and personalized classes.'},
        {'name': 'Premium Plan', 'price': 39.99,
            'description': 'Personalized workout and meal plans, plus access to a dedicated fitness coach.'},
        {'name': 'Elite Plan', 'price': 59.99,
            'description': 'All Premium features, plus advanced analytics, and priority support.'},
    ]

    for plan in plans:
        existing_plan = Plan.query.filter_by(name=plan['name']).first()
        if not existing_plan:
            new_plan = Plan(
                name=plan['name'], price=plan['price'], description=plan['description'])
            db.session.add(new_plan)

    db.session.commit()


@app.before_first_request
def create_table():
    db.create_all()
    seed_plans()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/plans')
def plans():
    return render_template('plans.html')
# Load user function for Flask-Login


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        plan_id = request.form['plan']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('An account with this email address already exists.', 'danger')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email,
                        password=hashed_password, plan_id=plan_id)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login route


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            print("LOGIN SUCCESSFULL")
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')

    return render_template('login.html')

# Logout route


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/profile')
@login_required
def profile():
    user_plan = current_user.plan
    print("PLAN:::: ", user_plan)
    return render_template('profile.html', user_plan=user_plan)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        about = request.form['about']

        current_user.username = username
        current_user.email = email
        current_user.about = about
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html')


if __name__ == '__main__':
    app.run(debug=True)
