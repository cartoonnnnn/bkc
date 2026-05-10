----------

sudo apt update

# ---------------------------------------------------
# Install kubectl
# ---------------------------------------------------

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

chmod +x kubectl

sudo mv kubectl /usr/local/bin/

kubectl version --client

# ---------------------------------------------------
# Install Minikube
# ---------------------------------------------------

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube version

# ---------------------------------------------------
# Configure Docker Permission
# ---------------------------------------------------

sudo usermod -aG docker $USER

newgrp docker

docker --version

# ---------------------------------------------------
# Start Minikube
# ---------------------------------------------------

minikube start --driver=docker

minikube status

# ---------------------------------------------------
# Kubernetes Node Information
# ---------------------------------------------------

kubectl get nodes

# ---------------------------------------------------
# Create Pod
# ---------------------------------------------------

kubectl run my-pod --image=nginx --restart=Never

kubectl get pods

kubectl get pod my-pod -o wide

# ---------------------------------------------------
# Expose Pod
# ---------------------------------------------------

kubectl expose pod my-pod --type=NodePort --port=80 --name=my-service

kubectl get services

minikube service my-service --url

# ---------------------------------------------------
# Delete Pod Service
# ---------------------------------------------------

kubectl delete service my-service

kubectl delete pod my-pod

# ---------------------------------------------------
# Create Deployment
# ---------------------------------------------------

kubectl create deployment my-deployment --image=nginx --replicas=2

kubectl get deployments

kubectl get pods

# ---------------------------------------------------
# Expose Deployment
# ---------------------------------------------------

kubectl expose deployment my-deployment --type=NodePort --port=80

minikube service my-deployment --url

# ---------------------------------------------------
# Scale Deployment
# ---------------------------------------------------

kubectl scale deployment my-deployment --replicas=5

kubectl get pods

# ---------------------------------------------------
# Delete Deployment
# ---------------------------------------------------

kubectl delete deployment my-deployment

kubectl get pods

# ---------------------------------------------------
# Stop Minikube
# ---------------------------------------------------

minikube stop
