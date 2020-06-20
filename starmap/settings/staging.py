"""
    PROJECT STAGING ENVIRONMENT SETTINGS
"""
import os

from starmap.apps.base.utility.io import confirm_dir_exists
from starmap.settings import FILES_DIR


# SITE_NAME = 'ec2-18-224-64-103.us-east-2.compute.amazonaws'
# SITE_DOMAIN = 'ec2-18-224-64-103.us-east-2.compute.amazonaws.com'  # Careful while changing,
# SITE_SCHEME = 'http'
# BASE_URL = "%s://%s" % (SITE_SCHEME, SITE_DOMAIN)

ALLOWED_DOMAINS = ALLOWED_HOSTS = ['157.245.234.155', 'http://157.245.234.155',
                                   'http://design.mapyournight.com/', 'design.mapyournight.com']

# For Developers
ADMINS = (
  ('Rajiv', 'gurmukh.singh@techstriker.com'),
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'starmap',
        'USER': 'postgres',
        'PASSWORD': 'spider@123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

LOG_FILE_DIR = os.path.join(FILES_DIR, 'logs', 'staging')
confirm_dir_exists(LOG_FILE_DIR)
