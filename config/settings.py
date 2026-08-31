import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Завантаження .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Секретний ключ
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-secret-key")

# Debug режим
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'trendai-web.onrender.com']


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # твої додатки
    'config.apps.ConfigConfig',
    'product_engine.apps.ProductEngineConfig',
    'campaigns.apps.CampaignsConfig',
    'rest_framework',
    'ai',
    'analytics',
    'traffic',
    'trends',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database (універсальна конфігурація)
DATABASES = {
    "default": dj_database_url.config(
        default=f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST','localhost')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB')}"
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & Media files
STATIC_URL = 'static/'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'