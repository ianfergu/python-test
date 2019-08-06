pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'cp /var/www/arahtml/unknown.jpg /var/www/arahtml/weather.jpg'
            }
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'cp /var/www/arahtml/unknown.jpg /var/www/arahtml/weather.jpg'
                sh script: 'python -m py_compile sources/weather.py', label: "Compile the Application"
            }
        }
        stage('Initiate Tester') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            stages {
		stage('Web Test') {
		    	steps {
				sh script: 'py.test --verbose --junit-xml test-reports/results_web.xml sources/test_webtest.py', label: "Test web access and record results."
				}
			post {
			    always {
			    	junit 'test-reports/results_web.xml'
				    }
			    }
		    }
                stage('Testing') {
		
                    parallel {
                        stage('URL Test') {
                            steps {
                                sh script: 'py.test --verbose --junit-xml test-reports/results_url.xml sources/test_url.py', label: "Test the NWS URL and record results."
                            }

                            post {
                                always {
                                    junit 'test-reports/results_url.xml'
                                }
                            }
                        }
                        stage('Weather Test') {
                            steps {
                                sh script: 'py.test --verbose --junit-xml test-reports/results.xml sources/test_weather.py', label: "Test the temperature and record results."
                                sh 'sudo cp /var/www/arahtml/desert.jpg /var/www/arahtml/weather.jpg'
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
             steps {
                  sh 'sudo cp /var/www/arahtml/goodweather.jpg /var/www/arahtml/weather.jpg'
            }
        }
    }
}
