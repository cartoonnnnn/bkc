git --version
git mkdir newproject
cd newproject
nano demo.py

# Write inside demo.py
print("Hello World")

git init
git config --global user.name "AKDIAZ15"
git config --global user.email "aryanraj.cd23@bmsce.ac.in"

git status
git add demo.py
git commit -m "first commit"

nano demo.py

# Change code to
print("Hello Git")

git status
git diff
git add demo.py
git commit -m "main code added"

git branch add-feature
git checkout add-feature

nano demo.py

# Add feature code
print("Feature Added")

git status
git add demo.py
git commit -m "feature added"

git log
git checkout master
git merge add-feature

git remote add origin https://github.com/AKDIAZ15/newproject.git
git remote -v

# GitHub Token Steps
# Sign in GitHub
# Profile -> Settings
# Developer Settings -> Personal Access Tokens -> Tokens (Classic)
# Generate new token
# Add note
# Select No Expiration
# Check all boxes
# Generate token
# Copy and save token in text file

git push -u origin master

# Username = Your GitHub Username
# Password = Generated Token

# Verify repository on GitHub
