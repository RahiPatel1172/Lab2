pipeline {
    agent any
    
    triggers {
        // Polling configuration - check every 5 minutes
        pollSCM('H/5 * * * *')
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Starting Git checkout...'
                checkout scm
                echo 'Git checkout completed successfully'
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    echo "Setting up Python environment..."
                    python3 -m venv venv
                    . venv/bin/activate
                    echo "Installing dependencies..."
                    pip install -r requirements.txt
                    echo "Build completed successfully"
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    echo "Activating virtual environment..."
                    . venv/bin/activate
                    echo "Running tests with coverage..."
                    python -m pytest tests/ -v --cov=app --cov-report=term-missing
                    echo "Tests completed"
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploying application..."
                    echo "In a real scenario, this would deploy to a cloud provider"
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            emailext (
                subject: "Pipeline Succeeded: ${currentBuild.fullDisplayName}",
                body: """
                <h2>Build Status: SUCCESS</h2>
                <p>Build Number: ${BUILD_NUMBER}</p>
                <p>Build URL: ${BUILD_URL}</p>
                <p>Build Duration: ${currentBuild.durationString}</p>
                <p>Git Commit: ${GIT_COMMIT}</p>
                <p>Git Branch: ${GIT_BRANCH}</p>
                """,
                to: 'rahican11@gmail.com',
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                body: """
                <h2>Build Status: FAILURE</h2>
                <p>Build Number: ${BUILD_NUMBER}</p>
                <p>Build URL: ${BUILD_URL}</p>
                <p>Build Duration: ${currentBuild.durationString}</p>
                <p>Git Commit: ${GIT_COMMIT}</p>
                <p>Git Branch: ${GIT_BRANCH}</p>
                <p>Please check the build logs for more details.</p>
                """,
                to: 'rahican11@gmail.com',
                mimeType: 'text/html'
            )
        }
    }
} 