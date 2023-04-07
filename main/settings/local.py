from .base import *

DOMAIN = f"http://{os.environ.get('LOCAL_DOMAIN')}"
BOT_KEY = os.environ.get('LOCAL_BOT_KEY')
ALLOWED_HOSTS = ["*"]
