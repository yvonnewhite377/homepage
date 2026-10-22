import os

DEBUG = os.getenv('DEBUG', '') == '1'
TIMEOUT = int(os.getenv('TIMEOUT', '30'))
