FROM python:3.9-slim
WORKDIR /var/www
COPY http-test ./
CMD ["python3", "/var/www/test_server.py"]
