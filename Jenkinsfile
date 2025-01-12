pipeline {
    agent any
    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    bat '''
                    venv\\Scripts\\activate
                    python -m unittest discover tests
                    '''
                }
            }
        }
    }
}
