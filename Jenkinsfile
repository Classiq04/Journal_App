pipeline {
    agent any
    
    environment {
        COMPOSE_PROJECT_NAME = "journal_app_${BUILD_NUMBER}"
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    docker --version
                    docker-compose --version
                '''
            }
        }

        stage('Build & Run') {
            steps {
                sh '''
                    docker compose down --remove-orphans || true
                    docker compose build --no-cache
                    docker compose up -d
                '''
            }
        }

        stage('Verify') {
            steps {
                sleep(time: 15, unit: 'SECONDS')
                sh '''
                    curl -sSf http://localhost:5000/entries > /dev/null || \
                    (echo "API check failed"; exit 1)
                '''
            }
        }
    }

    post {
        always {
            sh 'docker compose down || true'
        }
    }
}