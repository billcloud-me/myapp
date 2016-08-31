Name            : hodor
Summary         : hodor grid application
Version         : 0.0.1
Release         : 0.1

Group           : Applications/File
License         : GPL

BuildArch       : noarch
BuildRoot       : rpm


# Use "Requires" for any dependencies, for example:
# Requires        : tomcat6

# Description gives information about the rpm package. This can be expanded up to multiple lines.
%description
hodor app

# The installation. 
# We actually just put all our install files into a directory structure that mimics a server directory structure here
%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/opt/tomcat/webapps
echo `pwd`
cp ../SOURCES/hodor.war $RPM_BUILD_ROOT/opt/tomcat/webapps/.

# Contains a list of the files that are part of the package
# See useful directives such as attr here: http://www.rpm.org/max-rpm-snapshot/s1-rpm-specref-files-list-directives.html
%files
%attr(755, root, -) /opt/tomcat/webapps/hodor.war
/opt/tomcat/webapps/hodor.war

# Used to store any changes between versions
%changelog
