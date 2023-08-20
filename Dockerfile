# tell Docker to fetch this image from the Docker Hub because we’ll be building on it and using it for our own image. 
# This is common practice in containerisation
FROM nginx
# tell Docker to copy everything in our directory (that’s what the dot means) to a specific directory inside the container. 
# This directory is where nginx serves its web content.
COPY . /usr/share/nginx/html
