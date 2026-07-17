pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install --upgrade pip'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'py -m playwright install'
            }
        }

        stage('Run Web Scraper') {
            steps {
                bat 'py scrapers\\scrape.py'
            }
        }

        stage('Run Login Automation') {
            steps {
                bat 'py tests\\test_contact_form.py'
            }
        }

    }

    post {

        always {

            archiveArtifacts artifacts: 'output/*', allowEmptyArchive: true

            archiveArtifacts artifacts: 'screenshots/*', allowEmptyArchive: true

        }
    }
}