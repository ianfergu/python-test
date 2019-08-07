pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'master' }
            steps {
                dir ("/var/www/arahtml/") {
                     sh 'cp unknownwebpage webpage'
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
                         sh 'cp hotwebpage webpage'
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
                                      sh 'cp unknownwebpage webpage'
                                     }
                                }
                            }
                        }
                        stage('Weather Test') {
                            agent { docker { image 'qnib/pytest'} }
                            steps {
                                    sh script: 'py.test --verbose --junit-xml test-reports/results.xml sources/test_weather.py', label: "Test the temperature and record results"
                                    }

                            post {
                                always {
                                     junit 'test-reports/results.xml'
                                }
                            }
                        }
                        stage('Update Website With Results') {
                            agent { label 'master' }
                            steps {
                                 sh 'sleep 5s'
                                 dir ("/var/www/arahtml/") {
                                      sh 'cp hotwebpage webpage'
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
                    archiveArtifacts 'sources/weather.py' 
                }
            }
        } 
        stage('Update Results') {
        agent { label 'master' }
             steps {
                dir ("/var/www/arahtml/") {
                    sh 'cp nicewebpage webpage'

                }
            }
        }
    }
}
