BOOBS_API_URL = 'http://api.oboobs.ru/'
BOOBS_MEDIA_URL = 'http://media.oboobs.ru/'
BOOBS_AMOUNT = 1
BOOBS_TOKEN = '***'

# Trying to load local settings
try:
    from local import *
except ImportError:
    pass
