FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY nginx.conf /etc/nginx/sites-available/default

# Install nginx
RUN apt update && apt install -y nginx

# Copy nginx config
COPY nginx.conf /etc/nginx/sites-available/default

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose ports
EXPOSE 80

# Start both gunicorn and nginx
CMD service nginx start && gunicorn project.wsgi:application --bind 0.0.0.0:8000
