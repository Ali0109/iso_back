import os
from datetime import datetime

formatted_date = datetime.today().strftime("%Y-%m-%d")

bind = os.environ.get("BIND")
workers = os.environ.get("WORKERS")
accesslog = f'/iso_back/logs/access/{formatted_date}.log'
errorlog = f'/iso_back/logs/error/{formatted_date}.log'
