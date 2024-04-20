pipeline{
    agent any
    stages {
        stage('Build Maven') {
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '2ec33201-353f-4de5-ad1e-7c8a9f7b768f', url: 'https://github.com/veera1016/jenkins-docker-image.git']])
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
