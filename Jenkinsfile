pipeline{
    agent any
    stages {
        stage('Build Maven') {
            steps{
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'a3b8dd6b-3e3a-4e2e-b8c1-ef8b44631258', url: 'https://github.com/veera1016/Stock_market-Project.git']])
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
