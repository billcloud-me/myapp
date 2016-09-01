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
            whoami
            docker build -t billcloudme/myapp:devel .
        '''

    stage 'Clean Up'
        deleteDir()
}
