pipeline {
    agent any
    stages {
        stage('Force Cleanup') {
            steps {
                script {
                    // Force remove any containers with these names if they exist
                    sh '''
                        docker rm -f journal_backend || true
                        docker rm -f journal_frontend || true
                        docker network prune -f
                    '''
                }
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
                sh 'curl -s http://localhost:5000/entries | jq .'
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
      


