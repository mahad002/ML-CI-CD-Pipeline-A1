// Jenkinsfile
pipeline {
    agent any
    
    triggers {
        githubPush()
    }
    
    environment {
        DOCKER_HUB_CREDS = credentials('docker-hub-credentials')
        DOCKER_IMAGE_NAME = 'yourusername/ml-model'
        DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ."
                sh "docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_NAME}:latest"
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                sh "echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin"
                sh "docker push ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                sh "docker push ${DOCKER_IMAGE_NAME}:latest"
            }
        }
        
        stage('Notify Admin') {
            steps {
                emailext (
                    subject: "Deployment Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                    <p>Deployment to production was successful.</p>
                    <p>Build: ${env.BUILD_NUMBER}</p>
                    <p>Docker Image: ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}</p>
                    """,
                    to: 'admin@example.com',
                    mimeType: 'text/html'
                )
            }
        }
    }
    
    post {
        always {
            sh "docker logout"
        }
    }
}