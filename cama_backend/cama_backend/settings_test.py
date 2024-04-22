from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pum10test",
        "USER": "pum10admin",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
    }
}