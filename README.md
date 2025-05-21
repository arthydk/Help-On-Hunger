# HELP ON HUNGER

A Django-based web application to help connect food donors with those in need. The platform allows users to register as donors, fill out food donation forms, and view/manage their donation details. Admins can manage donor records through a secure dashboard. The backend database is powered by MySQL (via XAMPP).

---

## Features

- Donor Registration and Login System
- Food Donation Form Submission
- View and Manage Donation Records
- Admin Panel to Oversee Donations and Donor Details
- MySQL Database Integration (via XAMPP)
- Authentication and Authorization using Django’s built-in system


## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap (optional for styling)
- **Backend**: Python (Django Framework)
- **Database**: MySQL (XAMPP)
- **Tools**: Django Admin Panel, XAMPP, Git


## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/arthyk20/help-on-hunger.git
cd help-on-hunger

## Setup Virtual Environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

## Setup MySQL Database 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'helponhunger',
        'USER': 'root',
        'PASSWORD': '',  # your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

## Run Migration 

python manage.py makemigrations
python manage.py migrate

## Create Admin
python manage.py createsuperuser

## Run The Server 

python manage.py runserver