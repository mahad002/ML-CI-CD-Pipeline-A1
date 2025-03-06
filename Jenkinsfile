pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def image = docker.build("mahad002/ml-cicd-pipeline:${env.BUILD_ID}")
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        image.push()
                    }
                }
            }
        }
    }
    post {
        success {
            mail to: 'admin@example.com',
                 subject: "Deployment Successful",
                 body: "The deployment of build ${env.BUILD_ID} was successful."
        }
    }
}