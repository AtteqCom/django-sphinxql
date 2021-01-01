import os

# for testing postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sphinx_example',
        'USER': 'postgres',
    },
}
# for testing mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sphinx_example',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root_test',
        'PASSWORD': 'root_test'
    },
}

INSTALLED_APPS = ('tests.query', 'tests.queryset', 'tests.indexing', 'tests.foreign_relationships', 'sphinxql')

SECRET_KEY = "django_tests_secret_key"

MIDDLEWARE_CLASSES = ()

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_sphinx')

# we add 'U+00E2' to test unicode
# we cannot override settings since this is used at config time.
INDEXES = {
    'path': os.path.join(BASE_DIR, 'test_sphinx_index'),
    'sphinx_path': BASE_DIR,
    'index_params': {'charset_table': '0..9, A..Z->a..z, _, a..z, /, U+00E2'}
}

try:
    import tests.settings_test_local

    if getattr(tests.settings_test_local, 'INDEXES'):
        INDEXES.update(tests.settings_test_local.INDEXES)

    if getattr(tests.settings_test_local, 'DATABASES'):
        DATABASES.update(tests.settings_test_local.DATABASES)
except:
    pass
