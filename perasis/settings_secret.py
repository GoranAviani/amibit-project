# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8z!!$*7#)zkq7tit0!#rsn!yuga4191+i+gb(@jqb+0q7yl!'

ALLOWED_HOSTS = ['www.amibit.org','amibit.org','78.46.164.210','127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'perasisdb',
        'USER': 'admin',
        'PASSWORD': '2008perasis',
        'HOST':'localhost',
        #'HOST': '127.0.0.1',
        'PORT': '',
    }
 }
