%define name	jutils
%define version	1.1.0
%define release	%mkrel 2

Name:		%{name}
Summary:	Java Game project utils
Version:	%{version}
Release:	%{release} 
Source0:	jutils-src-svn-20100422.tar.bz2
Patch0:		%{name}-%{version}-indexed-jar.patch
URL:		https://jutils.dev.java.net/

Group:		Development/Java
License:        BSD

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	java-rpmbuild
Requires:	java

BuildArch: noarch

%description
The JUtils Project hosts an implementation of a set of APIs utilized by other
Java Game Technology Group projects (eg JInput).

%files
%defattr(-,root,root,-)
%doc www/index.html
%doc README.txt
%_javadir/*.jar

#--------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for jutils
Group:		Development/Java

%description javadoc
Javadoc for jutils.


%files javadoc
%defattr(-,root,root,-)
%_javadocdir/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
pwd
%patch0 -p0

%build
export CLASSPATH="." 
%ant all javadoc

%install
rm -rf $RPM_BUILD_ROOT

%__install -dm 755 $RPM_BUILD_ROOT%_javadir
%__install -m 644 bin/jutils.jar $RPM_BUILD_ROOT%_javadir/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%_javadir/%{name}.jar

# javadoc
%__install -dm 755 $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
pushd apidocs
cp -pr * $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
popd
ln -s %{name}-%{version} $RPM_BUILD_ROOT%_javadocdir/%{name}

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2011.0
+ Revision: 612515
- the mass rebuild of 2010.1 packages

* Thu Apr 22 2010 Jonathan Bayle <mrhide@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 537827
- import jutils


