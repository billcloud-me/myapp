node ('master'){
    stage 'Checkout'
        deleteDir()
        checkout scm

    stage 'Build and Test'
        env.PATH = "${tool 'Ant'}/bin:${env.PATH}"
        sh 'ant'

    stage 'Compile War'
        sh '''
            jar -cvf myapp.war -C WebContent .
        '''

    stage 'Build Tomcat Container'
        sh '''
            echo 'user: '
            docker build -t billcloudme/myapp:devel .
            docker tag billcloudme/myapp:devel 192.168.1.114:5000/myapp:devel
            docker push 192.168.1.114:5000/myapp:devel 
        '''

    stage 'Clean Up'
        deleteDir()
}
