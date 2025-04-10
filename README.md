# Quora clone

## Features

1. User Login
2. Post questions
3. View question details by others
4. Answer question by others
5. Like answers of other users
6. Logout/ Signup

![Quora Clone Home Page](https://github.com/mayurgajbhiye4/quora-clone/blob/master/assets/quora_clone.png)

## Environment Variables

DJANGO_SECRET_KEY =your_secret_key     

## Clone the repository

git clone https://github.com/mayurgajbhiye4/quora-clone.git
cd quora-clone

## Set up a virtual environment

### Create a virtual environment
python -m venv venv

### Activate the virtual environment
On Windows
venv\Scripts\activate
### On macOS/Linux
source venv/bin/activate

## Install dependencies

pip install -r requirements.txt

## Set up environment variables

Create a .env file in the project root directory and add the required environment variables as listed above.

## Set up the database

### Make migrations
python manage.py makemigrations

### Apply migrations
python manage.py migrate

### Create a superuser (admin)
python manage.py createsuperuser

## Running the Project

python manage.py runserver






