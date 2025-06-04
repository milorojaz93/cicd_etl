import jenkins.model.*
import org.jenkinsci.plugins.workflow.job.*
import org.jenkinsci.plugins.workflow.cps.*

// Referencia al Jenkins global
def jenkins = Jenkins.getInstance()

def jobName = "pipeline"
def job = jenkins.getItem(jobName)

if (job == null) {
    println "Creando pipeline job '${jobName}'..."

    // Crear el job pipeline
    def pipelineJob = new WorkflowJob(jenkins, jobName)
    
   def jenkinsfilePath = "/var/jenkins_home/workspace/pipeline/Jenkinsfile"
    def pipelineScript = new File(jenkinsfilePath).text

    // Asignar el script embebido al job
    def flowDefinition = new CpsFlowDefinition(pipelineScript, true)
    pipelineJob.setDefinition(flowDefinition)
    pipelineJob.save()

    jenkins.reload()
    println "Job '${jobName}' creado exitosamente."
} else {
    println "El pipeline job '${jobName}' ya existe. No se crea de nuevo."
}
