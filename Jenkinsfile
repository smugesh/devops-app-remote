pipeline {
    agent any  // This pipeline can run on any agent

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    try {
                        git branch: 'main', url:'git@github.com:smugesh/devops-app-remote.git'  // Replace with your actual GitHub URL
                    } catch (Exception e) {
                        error "Failed to checkout code: ${e.message}"
                    }
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Python Application'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests'
                sh 'python3 test_app.py'  // Ensure python3 is available
            }
        }
        stage('Package Artifact') {
            steps {
                echo 'Packaging artifact'
                sh 'tar -czf app.tar.gz .'  // Adjust as needed
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished'
        }

        success {
            echo 'Pipeline Success'
        }

        failure {
            echo 'Pipeline Failure'
        }
    }
}
