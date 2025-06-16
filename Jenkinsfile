pipeline {
    agent any
    
    environment {
        COMPOSE_PROJECT_NAME = "journal_app_${BUILD_NUMBER}"
        COMPOSE_DOCKER_CLI_BUILD: 1  # Enable modern Docker features
    }

    stages {
        stage('Tool Check') {
            steps {
                sh '''
                    echo "=== Versions ==="
                    docker --version
                    docker compose version || docker-compose --version
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    # Clean previous runs
                    docker compose down --remove-orphans 2>/dev/null || true
                    
                    # Build with cache cleanup
                    docker compose build --no-cache --pull
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    # Start with clean slate
                    docker compose up -d --force-recreate
                '''
            }
        }

        stage('Health Check') {
            steps {
                retry(3) {  # Retry up to 3 times
                    timeout(time: 1, unit: 'MINUTES') {
                        sh '''
                            until curl -sSf http://localhost:5000/entries >/dev/null; do
                                sleep 5
                                echo "Waiting for API..."
                            done
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            sh '''
                docker compose logs app  # Replace 'app' with your service name
                docker compose down -v --remove-orphans
            '''
        }
        failure {
            emailext body: "Build ${BUILD_NUMBER} failed\n\nCheck logs: ${BUILD_URL}",
                    subject: "FAILED: ${JOB_NAME}",
                    to: 'devops@yourcompany.com'
        }
    }
}