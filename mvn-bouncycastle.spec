#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-bouncycastle
Version  : 1rv51
Release  : 2
URL      : https://github.com/bcgit/bc-java/archive/r1rv51.tar.gz
Source0  : https://github.com/bcgit/bc-java/archive/r1rv51.tar.gz
Source1  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.jar
Source2  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.pom
Source3  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar
Source4  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.pom
Source5  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.jar
Source6  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.pom
Source7  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.jar
Source8  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.pom
Source9  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar
Source10  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-bouncycastle-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-bouncycastle package.
Group: Data

%description data
data components for the mvn-bouncycastle package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.pom
