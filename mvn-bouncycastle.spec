#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-bouncycastle
Version  : 1rv51
Release  : 8
URL      : https://github.com/bcgit/bc-java/archive/r1rv51.tar.gz
Source0  : https://github.com/bcgit/bc-java/archive/r1rv51.tar.gz
Source1  : https://repo1.maven.org/maven2/bouncycastle/bcprov-jdk15/140/bcprov-jdk15-140.jar
Source2  : https://repo1.maven.org/maven2/bouncycastle/bcprov-jdk15/140/bcprov-jdk15-140.pom
Source3  : https://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/1.57/bcpg-jdk15on-1.57.jar
Source4  : https://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/1.57/bcpg-jdk15on-1.57.pom
Source5  : https://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/1.60/bcpg-jdk15on-1.60.jar
Source6  : https://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/1.60/bcpg-jdk15on-1.60.pom
Source7  : https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/1.59/bcpkix-jdk15on-1.59.jar
Source8  : https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/1.59/bcpkix-jdk15on-1.59.pom
Source9  : https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/1.60/bcpkix-jdk15on-1.60.jar
Source10  : https://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/1.60/bcpkix-jdk15on-1.60.pom
Source11  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15/1.40/bcprov-jdk15-1.40.jar
Source12  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15/1.40/bcprov-jdk15-1.40.pom
Source13  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.jar
Source14  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.pom
Source15  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar
Source16  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.pom
Source17  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.jar
Source18  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.pom
Source19  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.jar
Source20  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.pom
Source21  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.57/bcprov-jdk15on-1.57.jar
Source22  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.57/bcprov-jdk15on-1.57.pom
Source23  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.59/bcprov-jdk15on-1.59.jar
Source24  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.59/bcprov-jdk15on-1.59.pom
Source25  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.60/bcprov-jdk15on-1.60.jar
Source26  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.60/bcprov-jdk15on-1.60.pom
Source27  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar
Source28  : https://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-bouncycastle-data = %{version}-%{release}
Requires: mvn-bouncycastle-license = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
No detailed description available

%package data
Summary: data components for the mvn-bouncycastle package.
Group: Data

%description data
data components for the mvn-bouncycastle package.


%package license
Summary: license components for the mvn-bouncycastle package.
Group: Default

%description license
license components for the mvn-bouncycastle package.


%prep
%setup -q -n bc-java-r1rv51

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-bouncycastle
cp LICENSE.html %{buildroot}/usr/share/package-licenses/mvn-bouncycastle/LICENSE.html
cp core/src/main/java/org/bouncycastle/LICENSE.java %{buildroot}/usr/share/package-licenses/mvn-bouncycastle/core_src_main_java_org_bouncycastle_LICENSE.java
mkdir -p %{buildroot}/usr/share/java/.m2/repository/bouncycastle/bcprov-jdk15/140
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/bouncycastle/bcprov-jdk15/140/bcprov-jdk15-140.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/bouncycastle/bcprov-jdk15/140
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/bouncycastle/bcprov-jdk15/140/bcprov-jdk15-140.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.57
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.57/bcpg-jdk15on-1.57.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.57
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.57/bcpg-jdk15on-1.57.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.60
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.60/bcpg-jdk15on-1.60.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.60
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.60/bcpg-jdk15on-1.60.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.59
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.59/bcpkix-jdk15on-1.59.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.59
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.59/bcpkix-jdk15on-1.59.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.60
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.60/bcpkix-jdk15on-1.60.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.60
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.60/bcpkix-jdk15on-1.60.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15/1.40
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15/1.40/bcprov-jdk15-1.40.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15/1.40
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15/1.40/bcprov-jdk15-1.40.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.57
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.57/bcprov-jdk15on-1.57.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.57
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.57/bcprov-jdk15on-1.57.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.59
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.59/bcprov-jdk15on-1.59.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.59
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.59/bcprov-jdk15on-1.59.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.60
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.60/bcprov-jdk15on-1.60.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.60
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.60/bcprov-jdk15on-1.60.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/bouncycastle/bcprov-jdk15/140/bcprov-jdk15-140.jar
/usr/share/java/.m2/repository/bouncycastle/bcprov-jdk15/140/bcprov-jdk15-140.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.57/bcpg-jdk15on-1.57.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.57/bcpg-jdk15on-1.57.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.60/bcpg-jdk15on-1.60.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcpg-jdk15on/1.60/bcpg-jdk15on-1.60.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.59/bcpkix-jdk15on-1.59.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.59/bcpkix-jdk15on-1.59.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.60/bcpkix-jdk15on-1.60.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcpkix-jdk15on/1.60/bcpkix-jdk15on-1.60.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15/1.40/bcprov-jdk15-1.40.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15/1.40/bcprov-jdk15-1.40.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.50/bcprov-jdk15on-1.50.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.52/bcprov-jdk15on-1.52.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.55/bcprov-jdk15on-1.55.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.57/bcprov-jdk15on-1.57.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.57/bcprov-jdk15on-1.57.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.59/bcprov-jdk15on-1.59.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.59/bcprov-jdk15on-1.59.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.60/bcprov-jdk15on-1.60.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk15on/1.60/bcprov-jdk15on-1.60.pom
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.jar
/usr/share/java/.m2/repository/org/bouncycastle/bcprov-jdk16/1.46/bcprov-jdk16-1.46.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-bouncycastle/LICENSE.html
/usr/share/package-licenses/mvn-bouncycastle/core_src_main_java_org_bouncycastle_LICENSE.java
