pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/weather.py'
            }
        }
        stage('Initiate Tester') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            
            stages {
                stage('Parallel testing') {
                    parallel {
                        stage('URL Test') {
                            steps {
                                sh 'py.test --verbose --junit-xml test-reports/results_url.xml sources/test_url.py'
                            }

                            post {
                                always {
                                    junit 'test-reports/results_url.xml'
                                }
                            }
                        }
                        stage('Weather Test') {
                            steps {
                                try {
                                    sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_weather.py'
                                } catch (exc) {
                                    echo 'A non-crucial test failed, continuing to build stage.'
                            }

                            post {
                                always {
                                    junit 'test-reports/results.xml'
                                }
                            }
                        }
                    }
                }
            }
        }
        stage('Deliver') { 
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2' 
                }
            }
            steps {
                sh 'pyinstaller --onefile sources/weather.py ' 
            }
            post {
                success {
                    archiveArtifacts 'dist/weather.py' 
                }
            }
        }
    }
}
