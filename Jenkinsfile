node ('master'){
    stage 'Checkout'
        deleteDir()
        checkout scm

    stage 'Compile'
        sh '''
            jar -cvx myapp.war *
        '''

    stage 'Clean Up'
        deleteDir()
}
