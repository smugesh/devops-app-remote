

pipeline {
	agant any  // This  pipeline can run on any agent

	stages {
		stage('Checkout Code') {
			steps {
				git 'git@github.com:smugesh/devops-app-remote.git'
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
				sh 'python3 test_app.py'
			}
		}
		stage ('Package Artifact') {
			steps {
				echo 'Packaging artifact'
				sh 'echo "Dummy Artifact packaging" > app.tar.gz'
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
			echo 'Pipeline failure'
		}
	}
}