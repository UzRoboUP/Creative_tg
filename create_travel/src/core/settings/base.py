from pathlib import Path
from decouple import config
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
ALLOWED_IPS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

APPS = [
    'account.apps.AccountConfig',
    'app.apps.AppConfig',
    'press_service.apps.PressServiceConfig',

    ]

DEV_APPS = [
    'rest_framework',
    "corsheaders",
    'axes',
    # "django_celery_results",
    # "django_celery_beat",
    "drf_yasg",
    'django_filters',
    
]



INSTALLED_APPS += APPS + DEV_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # translate
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.default_language.CustomLocaleMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
    # AxesStandaloneBackend should be the first backend in the
    'axes.backends.AxesStandaloneBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# JWT settings

SIMPLE_JWT = {
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    'user_model': 'account.User',
}

# AXES settings

AXES_FAILURE_LIMIT = 3
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]
AXES_COOLOFF_TIME = timedelta(minutes=1)
AXES_CACHE = 'axes'

# LOGGING settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'axes_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'axes.log',
        },
    },
    'loggers': {
        'axes': {
            'handlers': ['axes_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"{config('REDIS_URL', 'redis://localhost:6379/0')}",
        "KEY_PREFIX": "create_travel",  # todo: you must change this with your project name or something else
    }
}

# Auditlog
AUDITLOG_INCLUDE_ALL_MODELS = True

# CELERY CONFIGURATION
# CELERY_BROKER_URL = config("CELERY_BROKER_URL", "redis://localhost:6379")
# CELERY_RESULT_BACKEND = config("CELERY_BROKER_URL", "redis://localhost:6379")

# CELERY_TIMEZONE = "Asia/Tashkent"

# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

gettext=lambda s:s

LANGUAGES = (
    ('uz', gettext("O'zbek tili")),
    ('ru', gettext('Russian')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz','ru')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz','ru')
TRANSLATABLE_MODEL_MODULES = ('press_service.models', 'app.models',)

MODELTRANSLATION_TRANSLATION_FILES = (
    'app.translation',
    'press_service.translation',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# HOST = 'https://6b4d-185-213-229-48.ngrok-free.app'
# HOST = 'http://localhost:8000'
HOST='https://creativetg.leetcode.uz'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True



SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = ['https://www.creativetg.leetcode.uz', 'https://creativetg.leetcode.uz']

AXES_LOCKOUT_URL = HOST + '/lockout/'

TOKEN = config("TOKEN")

try:
    from .jazzmin import JAZZMIN_UI_TWEAKS, JAZZMIN_SETTINGS
except ImportError:
    from jazzmin.settings import JAZZMIN_UI_TWEAKS, JAZZMIN_SETTINGS
