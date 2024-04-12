import pytest
from django.db import connections
import psycopg2

@pytest.fixture(scope='session')
def django_db_setup():
    from django.conf import settings
    settings.DATABASES=['default']['NAME'] = 'test'
    settings.DATABASES=['default']['HOST'] = 'localhost'
    settings.DATABASES=['default']['PORT'] = '8000'

