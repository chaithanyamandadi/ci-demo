pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Test') {
      steps {
        sh 'python3 --version'
        sh 'python3 -m pip install --upgrade pip --user'
        sh 'python3 -m pip install --user pytest'
        sh 'python3 -m pytest -q'
      }
    }
  }
}


