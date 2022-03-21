pipeline {
    agent none
        stage('Build'){
            agent {
                docker {
                    image 'python:3'
                }
            }
        steps {
            sh 'python3 -m py_compile sources/ping-pong.py'
            stash(name: 'compiled-results', includes: 'Game/*.py*')
        }
            
    }
}