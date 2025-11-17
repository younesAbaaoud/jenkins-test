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
        
        stage('Installer pytest') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    python -m pip install pytest
                """
            }
        }
        stage('Lancer les tests') {
            steps {
                bat """
                   python -m pytest --maxfail=1 --disable-warnings -q
                """
            }
        }
    }
}
