pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello depuis un pipeline déclaratif'
            }
        }

        stage('Infos environnement') {
            steps {
                echo "Nom du noeud Jenkins: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }
        
        stage('Lancer les tests') {
            steps {
                bat """
                    pytest --maxfail=1 --disable-warnings -q
                """
            }
        }
    }
}
