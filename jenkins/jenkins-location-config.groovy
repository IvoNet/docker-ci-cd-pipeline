import jenkins.model.*

def jenkinsLocationConfiguration = JenkinsLocationConfiguration.get()

jenkinsLocationConfiguration.setUrl("https://jenkins:8081/");

jenkinsLocationConfiguration.save()