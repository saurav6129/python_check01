pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh python -m py_compile sources /test_Login.py '
            }
        }
		
		stage('test'){
			steps {
				echo 'testing the login script'
			}
		}
    }
}