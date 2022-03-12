import jenkins.model.*
import hudson.plugins.sonar.*
import hudson.tools.*

def inst = Jenkins.getInstance()

def desc = inst.getDescriptor("hudson.plugins.sonar.SonarRunnerInstallation")

def sinst = new SonarRunnerInstallation("(Default)", "/usr/share/sonar-runner-2.4", null)
desc.setInstallations(sinst)

desc.save()