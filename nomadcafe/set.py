from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={"default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "Cafe"
    }},
    INSTALLED_APPS=[__name__]
)