import jenkins.model.*
import org.jenkinsci.plugins.workflow.job.*
import org.jenkinsci.plugins.workflow.cps.*

// Referencia al Jenkins global
def jenkins = Jenkins.getInstance()

def jobName = "etl-proveedores"
def job = jenkins.getItem(jobName)

if (job == null) {
    println "📌 Creando pipeline job '${jobName}'..."

    // Crear el job pipeline
    def pipelineJob = new WorkflowJob(jenkins, jobName)
    
    // Jenkinsfile embebido (puedes ajustar aquí)
    def pipelineScript = """
        pipeline {
            agent any

            environment {
                VENV = ".venv"
            }

            stages {
                stage('Crear entorno virtual e instalar dependencias') {
                    steps {
                        sh '''
                            python3 -m venv \${VENV}
                            . \${VENV}/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }

                stage('Validar sintaxis') {
                    steps {
                        sh '''
                            . \${VENV}/bin/activate
                            flake8 src/ tests/ || true
                        '''
                    }
                }

                stage('Ejecutar pruebas') {
                    steps {
                        sh '''
                            . \${VENV}/bin/activate
                            pytest --junitxml=tests/results.xml tests/
                        '''
                    }
                }

                stage('Generar documentación') {
                    steps {
                        sh '''
                            . \${VENV}/bin/activate
                            pdoc --html src -o docs --force
                        '''
                    }
                }
            }

            post {
                always {
                    archiveArtifacts artifacts: 'docs/**/*', allowEmptyArchive: true
                    junit 'tests/results.xml'
                }
                failure {
                    echo 'Falló el pipeline. Revisa los logs.'
                }
                success {
                    echo 'Pipeline ejecutado exitosamente.'
                }
            }
        }
    """

    // Asignar el script embebido al job
    def flowDefinition = new CpsFlowDefinition(pipelineScript, true)
    pipelineJob.setDefinition(flowDefinition)
    pipelineJob.save()

    jenkins.reload()
    println "✅ Job '${jobName}' creado exitosamente."
} else {
    println "ℹ️ El pipeline job '${jobName}' ya existe. No se crea de nuevo."
}
