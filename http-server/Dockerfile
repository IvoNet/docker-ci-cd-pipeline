# tjonahen/http-server
# node image with a http server installed
# docker build -t tjonahen/http-server .
# VERSION 1.0.0

FROM node
MAINTAINER IvoNet <webmaster@ivonet.nl>
RUN npm install http-server -g
EXPOSE 80
ENTRYPOINT http-server -p 80 -c300