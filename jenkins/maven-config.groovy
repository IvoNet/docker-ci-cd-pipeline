import jenkins.model.*
import java.nio.file.Files
import java.nio.file.Paths
import java.nio.file.StandardCopyOption;
import java.io.File

File f = new File("/var/jenkins_home/.m2");
if (!f.exists()) {
  Files.createDirectory(f.toPath());
}
println 'copy settings.xml to .m2 folder'
Files.copy(Paths.get("/usr/share/jenkins/m2/settings.xml"), Paths.get("/var/jenkins_home/.m2/settings.xml"), StandardCopyOption.REPLACE_EXISTING);

a=Jenkins.instance.getExtensionList(hudson.tasks.Maven.DescriptorImpl.class)[0];
b=(a.installations as List);
b.add(new hudson.tasks.Maven.MavenInstallation("MAVEN3", "/usr/share/maven", []));
a.installations=b
a.save()