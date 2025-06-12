pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                    # Install jq for JSON processing
                    apt-get update && apt-get install -y jq || true
                '''
            }
        }
        stage('Force Cleanup') {
            steps {
                sh '''
                    docker rm -f journal_backend || true
                    docker rm -f journal_frontend || true
                    docker network prune -f
                '''
            }
        }
        stage('Build & Run') {
            steps {
                sh 'docker compose up --build -d'
            }
        }
        stage('Verify') {
            steps {
                sleep 5
                script {
                    try {
                        // First check if curl works without jq
                        def response = sh(script: 'curl -s http://localhost:5000/entries', returnStdout: true).trim()
                        if (response) {
                            echo "API Response: ${response}"
                        } else {
                            error "Empty response from API"
                        }
                        
                        // If we have jq, format nicely
                        sh 'which jq && curl -s http://localhost:5000/entries | jq . || curl -s http://localhost:5000/entries'
                    } catch (Exception e) {
                        error "Verification failed: ${e.getMessage()}"
                    }
                }
            }
        }
    }
    post {
        always {
            sh '''
                docker compose down || true
                docker rm -f journal_backend journal_frontend || true
            '''
        }
    }
}