# ---------------------------------------------------
# LAB 4 - Jenkins Integrating with Git
# ---------------------------------------------------

sudo apt update

sudo apt install openjdk-21-jre -y

java --version

echo "deb [trusted=yes] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list

sudo apt update

sudo apt install jenkins -y

sudo systemctl start jenkins

sudo systemctl enable jenkins

sudo systemctl status jenkins

# Press q to exit status screen

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# Open Jenkins
# http://localhost:8080

# Install Suggested Plugins

# Create Admin User
# Username : admin
# Password : admin123
# Full Name : Nanas Maluiya
# Email : nanasmaluiya.cd23@bmsce.ac.in

# ---------------------------------------------------
# Create GitHub Repository BEFORE Jenkins Jobs
# ---------------------------------------------------

mkdir newproject

cd newproject

nano README.md

# Add text inside README.md

This is Jenkins Git Integration

git init

git config --global user.name "Nanas Maluiya"

git config --global user.email "nanasmaluiya.cd23@bmsce.ac.in"

git add .

git commit -m "initial commit"

git branch -M main

git remote add origin https://github.com/YOUR_USERNAME/demorepo.git

git push -u origin main

# For password use GitHub Personal Access Token
# Username = Your GitHub Username

# ---------------------------------------------------
# CREATE JOB1
# ---------------------------------------------------

# Dashboard -> New Item -> job1 -> Freestyle Project

# Add Build Step -> Execute Shell

java --version
date
echo "Pipeline created $(date)"

# Post Build Actions
# Build other projects -> job2

# Save

# ---------------------------------------------------
# CREATE JOB2
# ---------------------------------------------------

# Dashboard -> New Item -> job2 -> Freestyle Project

# Build Triggers
# Select -> Build after other projects are built
# Projects to watch -> job1

# Add Build Step -> Execute Shell

python3 --version
date

# Post Build Actions
# Build other projects -> job-git

# Save

# ---------------------------------------------------
# Add GitHub Credentials in Jenkins
# ---------------------------------------------------

# Dashboard -> Manage Jenkins -> Credentials

# System -> Global credentials -> Add Credentials

# Kind -> Username with password

# Username -> YOUR_GITHUB_USERNAME

# Password -> YOUR_GITHUB_PERSONAL_ACCESS_TOKEN

# ID -> github-token

# Description -> github-token

# Save

# ---------------------------------------------------
# CREATE job-git
# ---------------------------------------------------

# Dashboard -> New Item -> job-git -> Freestyle Project

# Source Code Management -> Git

# Repository URL
https://github.com/YOUR_USERNAME/demorepo.git

# Credentials
github-token

# Branch
*/main

# Build -> Execute Shell

cat README.md

# Post Build Actions
# Build other projects -> pipeline-job

# Save

# ---------------------------------------------------
# LAB 5 - Jenkins Pipeline View with Plugin
# ---------------------------------------------------

cd ~

mkdir pipelineproject

cd pipelineproject

nano demo.py

# Add code

print("Hello from Jenkins Pipeline")

git init

git config --global user.name "Nanas Maluiya"

git config --global user.email "nanasmaluiya.cd23@bmsce.ac.in"

git add .

git commit -m "pipeline job"

git branch -M main

git remote add origin https://github.com/YOUR_USERNAME/pipelinerepo.git

git push -u origin main

# ---------------------------------------------------
# Install Build Pipeline Plugin
# ---------------------------------------------------

# Dashboard -> Manage Jenkins

# Plugins -> Available Plugins

# Search:
Build Pipeline

# Install Plugin

# After installation:
# Go back to top page

# ---------------------------------------------------
# CREATE PIPELINE VIEW
# ---------------------------------------------------

# Click "+" icon near All tab

# Enter View Name:
pipeline-view

# Select:
Build Pipeline View

# Click:
Create

# Build Pipeline View Title:
Pipeline Test

# Select Initial Job:
job1

# Keep remaining configuration default

# Apply and Save

# ---------------------------------------------------
# CREATE pipeline-job
# ---------------------------------------------------

# Dashboard -> New Item -> pipeline-job -> Pipeline

# Save

# ---------------------------------------------------
# RUN COMPLETE WORKFLOW
# ---------------------------------------------------

# Open:
pipeline-view

# Click:
Build Now on job1

# Workflow:

# job1 ---> job2 ---> job-git ---> pipeline-job

# job1 runs successfully
# job2 starts automatically
# job-git starts automatically
# pipeline-job starts automatically

# Successful jobs appear in green color

# ---------------------------------------------------
# STOP JENKINS SERVER
# ---------------------------------------------------

sudo systemctl stop jenkins
