pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Verify Tools') {
            steps {
                bat 'python --version'
                bat 'git --version'
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-app .'
            }
        }

        stage('Run Container') {
            steps {
                // Remove an older container with this name, if present.
                bat 'docker rm -f student-app-container 2>NUL || exit /b 0'
                bat 'docker run -d --name student-app-container -p 5000:5000 student-app'
            }
        }

        stage('Verify Application') {
            steps {
                // Give Flask a few seconds to start, then check the endpoint.
                bat 'powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Sleep -Seconds 3; $r = Invoke-WebRequest -UseBasicParsing http://localhost:5000/; if ($r.StatusCode -ne 200 -or $r.Content -notlike ''*Flask application is running*'') { throw ''Application health check failed'' }; Write-Output $r.Content"'
            }
        }

        stage('Generate Monitoring Report') {
            steps {
                bat 'python monitor.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Check the stage results and Console Output.'
        }
    }
}
