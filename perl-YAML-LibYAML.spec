#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-YAML-LibYAML
Version  : 0.88
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/YAML-LibYAML-0.88.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/YAML-LibYAML-0.88.tar.gz
Summary  : 'Perl YAML Serialization using XS and libyaml'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 MIT
Requires: perl-YAML-LibYAML-license = %{version}-%{release}
Requires: perl-YAML-LibYAML-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
YAML::XS - Perl YAML Serialization using XS and libyaml
SYNOPSIS
use YAML::XS;

my $yaml = Dump [ 1..4 ];
my $array = Load $yaml;

%package dev
Summary: dev components for the perl-YAML-LibYAML package.
Group: Development
Provides: perl-YAML-LibYAML-devel = %{version}-%{release}
Requires: perl-YAML-LibYAML = %{version}-%{release}

%description dev
dev components for the perl-YAML-LibYAML package.


%package license
Summary: license components for the perl-YAML-LibYAML package.
Group: Default

%description license
license components for the perl-YAML-LibYAML package.


%package perl
Summary: perl components for the perl-YAML-LibYAML package.
Group: Default
Requires: perl-YAML-LibYAML = %{version}-%{release}

%description perl
perl components for the perl-YAML-LibYAML package.


%prep
%setup -q -n YAML-LibYAML-0.88
cd %{_builddir}/YAML-LibYAML-0.88
pushd ..
cp -a YAML-LibYAML-0.88 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML
cp %{_builddir}/YAML-LibYAML-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML/8ebf906fcf0eb467d966a6605855d9c003e76598 || :
cp %{_builddir}/YAML-LibYAML-%{version}/LibYAML/License %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML/75c83b388350c9f313c608a57313314cf7767208 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/YAML::LibYAML.3
/usr/share/man/man3/YAML::XS.3
/usr/share/man/man3/YAML::XS::LibYAML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-YAML-LibYAML/75c83b388350c9f313c608a57313314cf7767208
/usr/share/package-licenses/perl-YAML-LibYAML/8ebf906fcf0eb467d966a6605855d9c003e76598

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
