pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python test_Login.py'
            }
        }
		
		stage('test'){
			steps {
				echo 'testing the login script'
			}
		}
    }
}