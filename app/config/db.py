import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

# psycopg2
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# mysqlclient
MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
