from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.sql.expression import func
from models import db, User, Plan, Workout, Nutrition

from random import choice
from urllib.parse import urlparse, parse_qs

from constanst import WORKOUTS, NUTRITION_DATA, ARTICLES

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


def get_youtube_video_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    video_id = query_params.get('v', [None])[0]
    return video_id


def populate_workouts_and_nutrition():
    # Populate workouts
    for workout_type, exercises in WORKOUTS.items():
        for exercise in exercises:
            video_id = get_youtube_video_id(exercise['video'])
            workout = Workout(type=workout_type,
                              name=exercise['name'],
                              reps=exercise['reps'],
                              video_id=video_id)
            db.session.add(workout)

    # Populate nutrition data
    for nutrition_data in NUTRITION_DATA:
        for meal in nutrition_data['meals']:
            nutrition = Nutrition(time=nutrition_data['time'],
                                  meal=meal['name'],
                                  image_url=meal['image_url'])
            db.session.add(nutrition)

    db.session.commit()


def get_random_workout_and_nutrition():
    workout_types = ['fullBody', 'upperBody', 'lowerBody', 'cardio']
    random_workout_type = choice(workout_types)

    workouts = Workout.query.filter(Workout.type == random_workout_type).order_by(
        func.random()).limit(10).all()

    breakfast = Nutrition.query.filter(
        Nutrition.time == "Breakfast").order_by(func.random()).first()
    lunch = Nutrition.query.filter(
        Nutrition.time == "Lunch").order_by(func.random()).first()
    dinner = Nutrition.query.filter(
        Nutrition.time == "Dinner").order_by(func.random()).first()
    snack = Nutrition.query.filter(
        Nutrition.time == "Snacks").order_by(func.random()).first()

    return workouts, [breakfast, lunch, dinner, snack]


def calculate_bmi(height_cm, weight_lb):
    if height_cm and weight_lb:
        height_m = height_cm / 100  # Convert height from centimeters to meters
        weight_kg = weight_lb * 0.453592  # Convert weight from pounds to kilograms
        return weight_kg / (height_m ** 2)
    return None


@app.before_first_request
def create_table():
    db.create_all()
    seed_plans()
    populate_workouts_and_nutrition()


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
    workouts, meals = get_random_workout_and_nutrition()
    bmi = calculate_bmi(current_user.height, current_user.weight)
    return render_template('dashboard.html', workouts=workouts, meals=meals, articles=ARTICLES, bmi=bmi)


@app.route('/profile')
@login_required
def profile():
    user_plan = current_user.plan
    return render_template('profile.html', user_plan=user_plan)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        about = request.form['about']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        mobile_number = request.form['mobile_number']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']

        current_user.username = username
        current_user.email = email
        current_user.about = about
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.mobile_number = mobile_number
        current_user.age = age
        current_user.height = height
        current_user.weight = weight

        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html')


if __name__ == '__main__':
    app.run(debug=True)
