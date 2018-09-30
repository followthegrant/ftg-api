"""
settings for ftg-api
"""


import os


# elastic
ELASTIC = {
    'HOST': os.getenv('ELASTIC_HOST', 'localhost'),
    'PORT': os.getenv('ELASTIC_PORT', '9200'),
    'INDEX': os.getenv('ELASTIC_INDEX', 'ftg-disclosures')
}

PAGINATION = 50
EXCLUDE_FIELDS = ('host', '@timestamp', '@version')
ALLOW_ALL = os.getenv('ALLOW_ALL', 'false').lower() == 'true'
