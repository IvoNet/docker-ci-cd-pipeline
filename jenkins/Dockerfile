# jenkins:1.651.1
# maven:3.3.9
# 
FROM jenkins:1.651.1

# setup environment 
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    SONAR_RUNNER_VERSION=2.4 \
    SONAR_RUNNER_HOME=/usr/share/sonar-runner-${SONAR_RUNNER_VERSION} \
    MAVEN_VERSION=3.3.9 \
    MAVEN_HOME=/usr/share/maven\
    JENKINS_OPTS="--httpPort=8081"

# update jaxp properties to allow xsd from file system
COPY jaxp.properties $JAVA_HOME/jre/lib

# copy additional configuration scripts
COPY *.groovy /usr/share/jenkins/ref/init.groovy.d/

# copy and configure extra jenkins plugins
COPY plugins.txt /usr/share/jenkins/ref
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt

# setup maven to use nexus
COPY settings.xml /usr/share/jenkins/m2/settings.xml

USER root
# Install maven
RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION $MAVEN_HOME \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

# Install SonarQube runner
WORKDIR /usr/share

RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/${SONAR_RUNNER_VERSION}/sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip \
 && unzip sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip \
 && rm sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip

USER jenkins
EXPOSE 8081

