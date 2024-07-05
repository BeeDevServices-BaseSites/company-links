from pathlib import Path
import os
from environ import Env

env = Env()
env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('LOCAL_KEY')
# SECRET_KEY = env('DEV_KEY')
# SECRET_KEY = env('PROD_KEY')
INITIAL_REGISTRATION_CODE = env('LOCAL_INITIAL_REG_CODE')
# INITIAL_REGISTRATION_CODE = env('DEV_INITIAL_REG_CODE')
# INITIAL_REGISTRATION_CODE = env('PROD_INITIAL_REG_CODE')

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['wiki.beedev-services.com']

# CORS_ALLOWED_ORIGINS = []

# CORS_ALLOWED_ALL_ORIGINS: True

# X_FRAME_OPTIONS = "SAMEORIGIN"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'django_ckeditor_5',
    'core.apps.CoreConfig',
    'user.apps.UserConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'company_links.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'company_links.wsgi.application'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            ['Bold', 'Italic', 'Underline'],
            {'name': 'forms', 'items': ['Form', 'Checkbox', 'Radio', 'ImageButton']},
            ['Link', 'Unlink'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'insert', 'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            ['RemoveFormat', 'Source'],
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
        ],
        'height': 300,
        'width': '100%',
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'mysql.connector.django',
        'ENGINE':'django.db.backends.mysql',
        'NAME': env('LOCAL_SQL_NAME'),
        # 'NAME': env('PROD_SQL_NAME'),
        'USER': env('LOCAL_SQL_USER'),
        # 'USER': env('LOCAL_SQL_USER'),
        # 'PASSWORD': env('LOCAL_SQL_PASS'),
        'PASSWORD': 'HoneyBee#4',
        # 'PASSWORD': env('LOCAL_SQL_PASS'),
        'HOST': 'localhost',
        'PORT': '3306',
        # 'OPTIONS': {'charset': 'utf8mb4'},
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'beedev.services@gmail.com'
# EMAIL_HOST_PASSWORD = env('HOST_PASSWORD')
