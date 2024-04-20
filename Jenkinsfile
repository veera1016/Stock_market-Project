pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from Git using Git commands
                script {
                    // Define the Git tool to use
                    def gitHome = tool 'Default'
                    
                    // Set up Git environment
                    env.PATH = "${gitHome}/bin:${env.PATH}"
                    
                    // Execute Git commands
                    sh "git clone --branch main https://github.com/veera1016/Stock_market-Project.git"
                }
            }
        }
        
    stage('Build Docker Image'){
        steps{
            script {
                sh 'docker build -t veera1016/my-app-2.0 .'
            }
        }
    }
    stage('push Docker Image') {
            steps {
                script {
                withCredentials([string(credentialsId: 'veera1016', variable: 'Docker')]) {
                sh 'docker login -u veera1016 -p ${Docker}'
                
                sh 'docker push veera1016/my-app-2.0'
            }
        }
      }
    }
  }
}
