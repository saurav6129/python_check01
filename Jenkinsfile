pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '"C:\Users\Saurav\AppData\Local\Programs\Python\Python37\pythonw.exe" python test_Login.py'
            }
        }
		
		stage('test'){
			steps {
				echo 'testing the login script'
			}
		}
    }
}