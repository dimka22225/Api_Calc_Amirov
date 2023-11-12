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



  stage('Scan code for vulnerabilities') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv .venv
                source .venv/bin/activate
                pip3 install semgrep
                semgrep --config=auto --junit-xml -o reports/api_calc-scan_Amirov.xml api_calc_Amirov.py
                deactivate'''
                junit skipMarkingBuildUnstable: true, testResults: 'reports/api_calc-scan_Amirov.xml'
            }
        }



        stage('docker build'){
            steps{
                script{
                    sh 'docker build -f Dockerfile -t docker_amirov_calc .'
                }
            }
        }



         stage('Scan container with Trivy') {
            steps {
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'
                sh 'mkdir -p reports'
                sh 'trivy image --ignore-unfixed --format template --template "@html.tpl" -o reports/api_calc-scan_Amirov.html docker_amirov_calc:latest'
                publishHTML target : [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'api_calc-scan_Amirov.html',
                    reportName: 'Trivy Scan',
                    reportTitles: 'Trivy Scan'
                ]

                // Scan again and fail on CRITICAL vulns
                sh 'trivy image --ignore-unfixed --exit-code 1 --severity CRITICAL docker_amirov_calc:latest'
            }
        }



         stage('docker run'){
            steps{
                script{
                    sh 'docker run -d -p 5000:5000 docker_amirov_calc:latest'
                }
            }
        }

    }
}
