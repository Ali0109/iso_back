FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN ln -sf /usr/share/zoneinfo/Asia/Tashkent /etc/localtime
WORKDIR /iso_back
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
