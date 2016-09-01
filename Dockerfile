FROM tomcat:9.0.0.M8-jre8
MAINTAINER billcloud

ADD *.war /usr/local/tomcat/webapps/
ADD tomcat-users.xml /usr/local/tomcat/conf/
CMD ["catalina.sh", "run"]
