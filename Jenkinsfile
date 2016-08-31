node ('master'){
    stage 'Checkout'
        deleteDir()
        checkout scm

    stage 'Compile'
        sh '''
            jar -cvf myapp.war *
        '''

    stage 'Clean Up'
        deleteDir()
}
