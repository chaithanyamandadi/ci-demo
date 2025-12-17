pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Test') {
      steps {
        sh 'python3 --version'
        sh 'python3 -m pip install --upgrade pip'
        sh 'pip3 install pytest'
        sh 'pytest -q'
      }
    }
  }
}

