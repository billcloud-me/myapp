FROM tomcat:9.0.0.M8-jre8
MAINTAINER billcloud

ADD *.war /usr/local/tomcat/webapps/
ADD tomcat-users.xml /usr/local/tomcat/conf/
ADD context.xml /usr/local/tomcat/webapps/manager/META-INF/
CMD ["catalina.sh", "run"]
