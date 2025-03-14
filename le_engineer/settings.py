"""
Django settings for Le_Engineer project
Written by Leon Oliver.

This file defines settings, including database configurations,
authentication settings, middleware, templates, and static file handling.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys
from decouple import config  # Loads environment variables securely from a .env file.
from django.contrib.messages import constants as messages  # Enables message framework constants.
import dj_database_url  # Parses database URL from environment variables.
from pathlib import Path  # Provides an object-oriented approach to filesystem paths.

# Load environment variables from env.py if it exists.
if os.path.isfile('env.py'):
    import env

# Define base directory of the project.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # Path to the templates directory.

# Retrieve the secret key from the environment variables.
SECRET_KEY = config('SECRET_KEY')  # Keeps the secret key secure and out of source code.

# Debug mode setting (should be False in production for security reasons).
DEBUG = True

# Hosts allowed to access the application.
ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']  # Restricts access to defined domains.

# Application definition - List of installed Django apps.
INSTALLED_APPS = [
    'django.contrib.admin',  # Django's admin panel.
    'django.contrib.auth',  # Authentication system.
    'django.contrib.contenttypes',  # Content type framework.
    'django_summernote',  # WYSIWYG editor for rich text fields.
    'faq',  # FAQ application.
    'django_extensions',  # Extra Django management commands and utilities.
    'cloudinary',  # Cloud-based image and file storage.
    'django.contrib.sessions',  # Session management.
    'django.contrib.messages',  # User messaging framework.
    'django.contrib.staticfiles',  # Manages static files (CSS, JavaScript, images).
    'cloudinary_storage',  # Storage backend for Cloudinary.
    'django.contrib.sites',  # Site framework for handling multiple sites.
    'allauth',  # Third-party authentication and social login.
    'allauth.account',  # User account management via Django Allauth.
    'allauth.socialaccount',  # Social account authentication.
    'crispy_forms',  # Form layout management.
    'crispy_bootstrap5',  # Bootstrap 5 support for crispy forms.
    'blog',  # Custom blog application.
    'about',  # Custom about page application.
    'newsletter', # Custom model prompting users to subscribe to a newsletetr.
]

# FAQ application settings defining behavior for category descriptions.
FAQ_SETTINGS = ['no_category_description', 'no_category']

# Django Site Framework ID (used when running multi-site projects).
SITE_ID = 1

# Redirect URLs after login/logout actions.
LOGIN_REDIRECT_URL = '/'  # Redirect to home page after login.
LOGOUT_REDIRECT_URL = '/'  # Redirect to home page after logout.

# Django Crispy Forms settings for Bootstrap 5 integration.
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Middleware configuration - middleware components that process requests and responses.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Enhances security for the application.
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Manages static file serving in production.
    'django.contrib.sessions.middleware.SessionMiddleware',  # Enables session support.
    'django.middleware.common.CommonMiddleware',  # Provides various request/response utilities.
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks.
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Handles user authentication.
    'django.contrib.messages.middleware.MessageMiddleware',  # Enables message framework.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking attacks.
    'allauth.account.middleware.AccountMiddleware',  # Manages authentication through Django Allauth.
]

# Root URL configuration module.
ROOT_URLCONF = 'le_engineer.urls'

# Template configuration for rendering HTML templates.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django template engine.
        'DIRS': [TEMPLATES_DIR, 'templates'],  # Directories where templates are located.
        'APP_DIRS': True,  # Enables template discovery within installed apps.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Adds debugging context.
                'django.template.context_processors.request',  # Exposes request object in templates.
                'django.contrib.auth.context_processors.auth',  # Provides authentication context.
                'django.contrib.messages.context_processors.messages',  # Enables message framework.
            ],
        },
    },
]

# WSGI application entry point.
WSGI_APPLICATION = 'le_engineer.wsgi.application'

# Database configuration, retrieving settings from the environment.
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))  # Uses database URL from environment variables.
}

# Use SQLite database for testing to ensure a lightweight and isolated environment.
if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

# Trusted origins for CSRF protection.
CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]

# Authentication password validators for enforcing security policies.
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Email verification setting for user authentication.
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Disables email verification for authentication.

# Internationalization settings.
LANGUAGE_CODE = 'en-us'  # Default language.
TIME_ZONE = 'UTC'  # Default time zone.
USE_I18N = True  # Enable internationalization.
USE_TZ = True  # Enable timezone support.

# Django messages framework tags for Bootstrap styling.
MESSAGES_TAGS = {
    messages.SUCCESS: 'alert-success',  # Success messages use Bootstrap 'alert-success' class.
    messages.ERROR: 'alert-danger',  # Error messages use Bootstrap 'alert-danger' class.
}

# Static files (CSS, JavaScript, Images) settings.
STATIC_URL = 'static/'  # Base URL for static files.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Directories for additional static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory where static files are collected.

# Default primary key field type for Django models.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
