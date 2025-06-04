FROM jenkins/jenkins:lts

COPY casc.yaml /var/jenkins_home/casc.yaml
COPY pipeline/ /var/jenkins_home/workspace/pipeline


USER root

# Instalar plugins necesarios
RUN jenkins-plugin-cli --plugins workflow-aggregator

# Crear carpeta de inicialización
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d
COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/.

USER jenkins

EXPOSE 8080
EXPOSE 50000
