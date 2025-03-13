pipeline {
    agent any
    
    triggers {
        // Polling configuration - check every 5 minutes
        pollSCM('H/5 * * * *')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Checking out code from GitHub repository'
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    echo "Build completed successfully"
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests/ --cov=app --cov-report=term-missing
                    echo "Tests completed successfully"
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
                Build Status: SUCCESS
                Build Number: ${BUILD_NUMBER}
                Build URL: ${BUILD_URL}
                Changes: ${CHANGES}
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
        failure {
            emailext (
                subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                body: """
                Build Status: FAILURE
                Build Number: ${BUILD_NUMBER}
                Build URL: ${BUILD_URL}
                Changes: ${CHANGES}
                """,
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
} 