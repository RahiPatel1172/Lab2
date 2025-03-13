# CI/CD Pipeline Lab - Jenkins and GitHub Integration

This project demonstrates the integration of Jenkins with GitHub for automated CI/CD. The project uses a polling-based approach to detect changes in the GitHub repository.

## Project Overview

This is a simple Flask web application that serves as a demonstration project for setting up a CI/CD pipeline using Jenkins and GitHub.

## Project Structure

```
.
├── app/
│   └── app.py          # Main Flask application
├── tests/
│   └── test_app.py     # Unit tests
├── requirements.txt    # Python dependencies
├── Jenkinsfile        # Jenkins pipeline configuration
└── README.md          # This file
```

## Setup Instructions

### 1. GitHub Repository Setup

1. Create a new repository on GitHub
2. Push this code to your repository:
```bash
git init
git add .
git commit -m "Initial commit: CI/CD pipeline setup"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### 2. Jenkins Setup

1. Install Jenkins on your server
2. Install required plugins:
   - GitHub plugin
   - Pipeline plugin
   - Email Extension plugin
   - Git plugin

3. Configure Jenkins:
   - Go to Manage Jenkins > Configure System
   - Set up email notifications (use your college email)
   - Configure Git credentials if needed

4. Create a new Pipeline job:
   - Click "New Item"
   - Select "Pipeline"
   - Name your job (e.g., "flask-app-pipeline")
   - In the Pipeline section:
     - Select "Pipeline script from SCM"
     - Choose Git as SCM
     - Enter your GitHub repository URL
     - Set the branch to monitor (e.g., main)
     - Set the script path to "Jenkinsfile"

5. Configure polling:
   - The Jenkinsfile is configured to poll GitHub every 5 minutes
   - This is set using the `pollSCM('H/5 * * * *')` trigger

### 3. Testing the Pipeline

1. Make a small change to any file (e.g., modify the README)
2. Commit and push the changes:
```bash
git add README.md
git commit -m "Test: Trigger Jenkins pipeline"
git push
```
3. Wait for the polling to detect changes (up to 5 minutes)
4. Check Jenkins for the triggered build
5. Verify email notifications

## Pipeline Stages

The Jenkins pipeline includes the following stages:

1. **Checkout**: Clones the GitHub repository
2. **Build**: Sets up Python environment and installs dependencies
3. **Test**: Runs pytest with coverage reporting
4. **Deploy**: Placeholder for deployment to cloud provider

## Email Notifications

The pipeline is configured to send email notifications to your college email address for:
- Successful builds
- Failed builds

## Verification Steps

1. Confirm Jenkins is polling GitHub:
   - Check the Jenkins job configuration
   - Verify the polling schedule is set to every 5 minutes

2. Verify pipeline stages:
   - Check the Jenkins build log
   - Ensure all stages complete successfully
   - Review test coverage report

3. Test email notifications:
   - Make a change to trigger the pipeline
   - Verify you receive email notifications

## Troubleshooting

1. If polling doesn't work:
   - Check Jenkins logs for errors
   - Verify GitHub repository permissions
   - Ensure Jenkins has network access to GitHub

2. If email notifications fail:
   - Verify email settings in Jenkins
   - Check spam folder
   - Review Jenkins logs for email-related errors

## Lab Requirements Met

- [x] Jenkins integration with GitHub
- [x] Polling-based approach (checking every 5 minutes)
- [x] Pipeline stages (checkout, build, test, deploy)
- [x] Email notifications
- [x] Documentation of setup and verification 