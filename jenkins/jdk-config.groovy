import hudson.model.JDK
import hudson.tools.JDKInstaller
import hudson.tools.InstallSourceProperty
import jenkins.model.Jenkins

def descriptor = new JDK.DescriptorImpl();

if (descriptor.getInstallations()) {
    println 'skip jdk installations'
} else {
    println 'add System JDK'
    descriptor.setInstallations(new JDK(JDK.DEFAULT_NAME, "/usr/lib/jvm/java-8-openjdk-amd64"))
}