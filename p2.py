sudo su -

# Docker Basic Commands
docker images
docker pull nginx
docker run hello-world
docker run -d -p 8000:80 nginx
docker ps

# Stop Container using Container ID
docker stop <container_id>

docker ps
docker ps -a

# Start Container again
docker start <container_id>

docker ps

# Stop and Remove Container
docker stop <container_id>
docker rm <container_id>

docker ps -a

# Run nginx container with custom container name
docker run -d -p 8000:80 my_nginx nginx

# Enter inside container
docker exec -it my-nginx bash

# Move to nginx html directory
cd /usr/share/nginx/html

# Create and edit HTML file
nano index.html

# Edit index.html content and save file
exit

docker ps

# Stop and remove container
docker stop <container_id>
docker rm <container_id>

# Remove nginx image
docker rmi nginx

# If nano does not exist
apt update
apt install nano -y

# ---------------------------------------------------
# Creating Custom Flask Docker Image
# ---------------------------------------------------

mkdir Documents
cd Documents

mkdir pythonproject
cd pythonproject

mkdir templates

# Create Flask app
nano app.py

# Add following code in app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Move to templates folder
cd templates

# Create HTML file
nano index.html

# Add following HTML code

<!DOCTYPE html>
<html>
<head>
<title>Home Page</title>
</head>

<body>
<h1>Welcome to my Flask app</h1>
<p>This is the home page</p>
</body>

</html>

# Move back
cd ..

# Install Flask
pip install flask --break-system-packages

# Run Flask app
python3 app.py

# Create Dockerfile
nano Dockerfile

# Add following Dockerfile code

FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install flask
CMD ["python3","app.py"]

# Build Docker Image
sudo docker build -t myimage:1 .

# Check Docker Images
sudo docker images

# Run Docker Container
sudo docker run -p 8000:5000 myimage:1

# ---------------------------------------------------
# Working with Docker Hub
# ---------------------------------------------------

# Login to Docker Hub website
# https://hub.docker.com

# Login from terminal
sudo docker login

# Tag Docker Image
sudo docker tag myimage:1 <your docker username>/dockerimage:1

# Check Images
sudo docker images

# Push Image to Docker Hub
sudo docker push omanazzz/dockerimage:1
