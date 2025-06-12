pipeline {
    agent any
    stages {
        stage('Cleanup') {
            steps {
                sh 'docker compose down || true'
            }
        }
        stage('Build & Run') {
            steps {
                sh 'docker compose up --build -d'
            }
        }
        stage('Verify') {
            steps {
                sh 'sleep 5' // Give containers time to start
                sh 'curl -s http://localhost:5000/entries | jq .'
            }
        }
    }
    post {
        always {
            sh 'docker compose down' // Final cleanup
        }
    }
}
