Docker
=======
All kind of docker files script and other related stuff.

Note1:
A small note on running docker-compose, up and down are not complementary:
* docker-compose up, to start the application;
* docker-compose stop, to stop the application;
* docker-compose down, to stop and remove all images, data volumes, etc, etc.

Note2:
Deleting untaged images
```bash
docker rmi $(docker images | grep '^<none>' | awk '{print $3}')
```



CI
==
ci, continous integration, Docker-compose to start an ci build environment with [jenkins](https://jenkins.io/), [sonar](http://www.sonarqube.org/), [Hygieia](https://github.com/capitalone/Hygieia), and [nexus](http://www.sonatype.org/nexus/).

Derby
==
Docker file to get a working derby database image, based on java:alpine I think this is the smallest derby image posible.
```bash
docker build -t ivoent/derbydb .
```

GitLab
==
Just a shell script to run the GitLab docker image see [GitLab Docker](https://hub.docker.com/r/gitlab/gitlab-ce/).

The shell script simply runs something like:
```bash
docker run -p 10080:80 -p 10443:443 --name gitlab gitlab/gitlab-ce:8.7.2-ce.0
```

Gogs
==
Docker-compose file to start Gogs with a Postgresql database. See [Gogs Docker](https://hub.docker.com/r/gogs/gogs/).

http-server
===
Docker file to create a simple node based http-server. I use this as a base image for static content servers.

```bash
 docker build -t ivonet/http-server .
```
Hygieia
==
Docker-compose file to start Hygieia. Actualy only used as a simple test, as hygieia is integrated into the CI compose file.

Jenkins
===
Docker file to create a jenkins environment with maven, git, sonar-runner, and maven configured to use nexus.

```bash
  docker build -t ivonet/jenkins .
```
SonarQube
===
Docker-compose file to start SonarQube with Postgresql database. See [SonarQube Docker](https://hub.docker.com/_/sonarqube/).
