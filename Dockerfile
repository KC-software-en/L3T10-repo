##############################################
# This was the original:Nginx is typically used as a web server or reverse proxy in front of Django applications
# to handle tasks like serving static files, load balancing, and SSL termination. 
# However, it's not strictly necessary for running a Django app in a development or testing environment.

# tell Docker to fetch this image from the Docker Hub because we’ll be building on it and using it for our own image. 
# This is common practice in containerisation
# comment out: FROM nginx 
# tell Docker to copy everything in our directory (that’s what the dot means) to a specific directory inside the container. 
# This directory is where nginx serves its web content.
# comment out: COPY . /usr/share/nginx/html
##############################################

# Use the official Python 3.7 image as the base image
FROM python:3.7.0

# Set environment variables (if needed)
# ENV VARIABLE_NAME value

# Create and set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Expose the port on which Django runs (you might adjust this based on your Django project's settings)
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
