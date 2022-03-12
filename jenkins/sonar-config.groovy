import jenkins.model.*
import hudson.plugins.sonar.*
import hudson.plugins.sonar.model.*

def inst = Jenkins.getInstance()

if (SonarInstallation.all().length != 0) {
  println 'skip sonar installations'
} else {
  def desc = inst.getDescriptor("hudson.plugins.sonar.SonarPublisher")
  
  def sinst = new SonarInstallation(
    "sonarqube",
    false,
    "http://sonarqube:9000",
    "",
    "",
    "",
    "3.0.1",
    "",
    new TriggersConfig(),
    "",
    "",
    ""
  )
  
  desc.setBuildWrapperEnabled(true)
  
  desc.setInstallations(sinst)

  desc.save()
}