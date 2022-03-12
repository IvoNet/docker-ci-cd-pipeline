#!/bin/sh

docker run -p 10080:80 -p 10443:443 --name gitlab gitlab/gitlab-ce:8.7.2-ce.0
