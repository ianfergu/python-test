pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'master' }
            steps {
                dir ("/var/www/arahtml/") {
                     sh 'cp unknown.jpg weather.jpg && cd /var/lib/jenkins/workspace/python-test_develop'
                     }
                sh script: 'python -m py_compile sources/weather.py', label: "Compile the Application"
            }
        }
		stage('Web Test') {
		    agent { docker { image 'qnib/pytest' } }
		    	steps {
				sh script: 'py.test --verbose --junit-xml test-reports/results_web.xml sources/test_webtest.py', label: "Test web access and record results."
				}
			post {
			    always {
			    	junit 'test-reports/results_web.xml'
				    }
				failure {
				    agent { label 'master' }
                         dir ("/var/www/arahtml/") {
                         sh 'cp desert.jpg weather.jpg && cd /var/lib/jenkins/workspace/python-test_develop'
                        }
				    }
			    }
		    }
                stage('Testing') {
		
                    parallel {
                        stage('URL Test') {
                            agent { docker { image 'qnib/pytest' } }
                            steps {
                                sh script: 'py.test --verbose --junit-xml test-reports/results_url.xml sources/test_url.py', label: "Test the NWS URL and record results."
                            }

                            post {
                                always {
                                    junit 'test-reports/results_url.xml'
                                }
                                failure {
                                    agent { label 'master' }
                                     dir ("/var/www/arahtml/") {
                                      sh 'cp unknown.jpg weather.jpg && cd /var/lib/jenkins/workspace/python-test_develop'
                                     }
                                }
                            }
                        }
                        stage('Weather Test') {
                            agent { docker { image 'qnib/pytest'} }
                            steps {
                                    sh script: 'py.test --verbose --junit-xml test-reports/results.xml sources/test_weather.py', label: "Test the temperature and record results."
                                    }
                            post {
                                always {
                                     agent { label 'master' }
                                     junit 'test-reports/results.xml'
                                     dir ("/var/www/arahtml/") {
                                        sh 'cp desert.jpg weather.jpg && cd /var/lib/jenkins/workspace/python-test_develop'
                                     }
                                }
                            }
                        }
                    }
                }
        stage('Deliver') {
        agent { label 'master' }
             steps {
                dir ("/var/www/arahtml/") {
                    sh 'cp /var/www/arahtml/goodweather.jpg /var/www/arahtml/weather.jpg && cd /var/lib/jenkins/workspace/python-test_develop'

                }
            }
        }
    }
}
