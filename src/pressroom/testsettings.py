import os
DIRNAME = os.path.dirname(__file__)
DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/pressroom.db',
        },
    }


MEDIA_ROOT = os.path.realpath(os.path.join(DIRNAME, 'tests', 'media/'))
MEDIA_URL = '/site_media/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, "tests", "templates"),
)
INSTALLED_APPS = ['django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'taggit',
                  'photologue',
                  'pressroom', ]
ROOT_URLCONF = 'pressroom.tests.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}