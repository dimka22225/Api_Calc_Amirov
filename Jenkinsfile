pipeline {
    agent any

    stages{
        stage('docker stop, docker rm'){
            steps{
                script{
                    sh 'docker stop $(docker ps -qa)'
                    sh 'docker rm $(docker ps -qa)'
                    sh 'docker rmi $(docker images -q)'
                }
            }
        }
        stage('docker build, docker run'){
            steps{
                script{
                    sh 'docker build -f Dockerfile -t docker_amirov_calc .'
                    sh 'docker run -d -p 5000:5000 docker_amirov_calc:latest'
                }
            }
        }
    }
}
