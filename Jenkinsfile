pipeline {

    agent any

    stages {

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m playwright install'
            }
        }

        stage('Run Web Scraper') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" scrapers\\scrape.py'
            }
        }

        stage('Run UI Automation') {
            steps {
                bat '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" tests\\test_contact_form.py'
            }
        }
    }

    post {

        always {

            archiveArtifacts artifacts: 'output/*.csv', allowEmptyArchive: true

            archiveArtifacts artifacts: 'output/*.json', allowEmptyArchive: true

            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }

        success {
            echo 'Build completed successfully.'
        }

        failure {
            echo 'Build failed. Check the console output and archived screenshots.'
        }
    }
}