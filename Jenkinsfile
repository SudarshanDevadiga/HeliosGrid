pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling the latest code from GitHub...'
                checkout scm
            }
        }
        
        stage('Test Application') {
            steps {
                echo 'Running tests to ensure the Python code is healthy...'
                // In a real scenario, you'd run something like `pytest` here
                sh 'echo "All telemetry systems functioning normally."'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Baking the new Docker container...'
                sh 'docker build --no-cache -t heliosgrid-app:v3 .'
            }
        }
    }
}