pipeline {
    agent none
  //  options {
        //skipStagesAfterUnstable()
  //  }
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
                stage('Testing') {
		    stage('Web Test') {
		    	steps {
				sh 'py.test --verbose --junit-xml test-reports/results_web.xml sources/test_webtest.py'
				}
			post {
			    always {
			    	junit 'test-reports/results_web.xml'
				}
			    }
		    }
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
                                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_weather.py'
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
