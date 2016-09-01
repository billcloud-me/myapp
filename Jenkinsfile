node ('master'){
    stage 'Checkout'
        deleteDir()
        checkout scm

    stage 'Compile'
        sh '''
            jar -cvf myapp.war *
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
