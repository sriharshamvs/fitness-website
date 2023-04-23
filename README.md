# Fitness Hub Website

At Fitness Hub, we are dedicated to helping you achieve your fitness goals. We offer personalized workout plans, custom meal plans, and a wide range of resources to support your journey towards a healthier lifestyle.

## Our Services

- Personalized Workout Plans

- Custom Meal Plans

- Supportive Community

# Deploy

## Creating a development/production environment

- Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/.

- Open a command prompt (Windows) or terminal (Mac or Linux).

- Navigate into the `fitness-hub` directory:

```sh
cd fitness-hub
```

- Create a new virtual environment using the venv module that comes with Python:

```sh
python3 -m venv env
```

This will create a new directory called "env" that contains the virtual environment for your project.

- Activate the virtual environment:

On Windows:

```sh
.\env\Scripts\activate
```

On Mac/Linux:

```sh
source env/bin/activate
```

- Once the virtual environment is activated, you should see the name of the environment in your command prompt/terminal prompt. For example:

```sh
(env) C:\path\to\fitness-hub>
```

- Next, you can install the required packages from the requirements.txt file:

```sh
pip install -r requirements.txt
```

This command will install all the packages listed in the requirements.txt file.

## Running Flask

- Set the FLASK_APP environment variable to the name of your Flask application file.

On Windows:

```sh
set FLASK_APP=app.py
```

On Mac/Linux:

```sh
export FLASK_APP=app.py
```

__Note__: you can also set the FLASK_ENV environment variable to "development" to enable debug mode and automatic reloading of the server when changes are made to the code. For example:

```sh
export FLASK_ENV=development
```

- Run the Flask application using the flask run command:

```sh
flask run
```
