@Library('Demo-Shared-Library@main') _

pipeline {
    agent { label 'my-node' }

    environment {
        // Optional: helpful if you want to reuse these values later
        DOCKER_CREDENTIALS_ID = 'Token'
        DOCKER_REPO_NAME      = 'flask-app'
        DOCKER_TAG            = 'latest'
        FLASK_IMAGE           = 'today-flask-app:latest'
        NGINX_IMAGE           = 'nginx-app:latest'
        GIT_REPO_URL          = 'https://github.com/syedhamzaarees/Flask-based-web-application-with-Nginx-reverse-proxy-and-MySQL-database-fully-containerized-using-D.git'
        GIT_BRANCH            = 'main'
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                script {
                    echo '🚀 Cloning project repository...'
                    cloneCode(
                        repo: env.GIT_REPO_URL,
                        branch: env.GIT_BRANCH
                    )
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    echo '🔧 Building Flask and Nginx Docker images...'
                    buildFlask(imageName: env.FLASK_IMAGE)
                    buildNginx(imageName: env.NGINX_IMAGE)
                }
            }
        }

        stage('Push Flask Image to Docker Hub') {
            steps {
                script {
                    echo '📤 Pushing Flask image to Docker Hub...'
                    pushToDockerHub(
                        localImage: env.FLASK_IMAGE,
                        repoName: env.DOCKER_REPO_NAME,
                        tag: env.DOCKER_TAG,
                        credentialsId: env.DOCKER_CREDENTIALS_ID
                    )
                }
            }
        }

        stage('Deploy Containers') {
            steps {
                script {
                    echo '🚀 Deploying application using Docker Compose...'
                    deployApp()
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully! Flask + Nginx deployment complete.'
        }
        failure {
            echo '❌ Pipeline failed! Check Jenkins console logs for details.'
        }
    }
}
