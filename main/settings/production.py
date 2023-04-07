from .base import *

HTTPS_DOMAIN = f"https://{os.environ.get('PRODUCTION_DOMAIN')}"
HTTP_DOMAIN = f"http://{os.environ.get('PRODUCTION_DOMAIN')}"
BOT_KEY = os.environ.get('PRODUCTION_BOT_KEY')
ALLOWED_HOSTS = [HTTPS_DOMAIN, HTTP_DOMAIN, 'localhost:8020']
