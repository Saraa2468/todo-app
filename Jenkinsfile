pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Saraa2468/todo-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t todo-app:latest .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop old container if exists
                    sh 'docker stop todo-app || true && docker rm todo-app || true'
                    
                    // Run new container
                    sh 'docker run -d -p 5000:5000 --name todo-app todo-app:latest'
                }
            }
        }
    }
}