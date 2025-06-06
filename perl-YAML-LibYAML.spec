#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v25
# autospec commit: 9594167
#
Name     : perl-YAML-LibYAML
Version  : 0.904.0
Release  : 48
URL      : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-v0.904.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-v0.904.0.tar.gz
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

# Classic functional interface
my $yaml = Dump [ 1..4 ];
my $array = Load $yaml;

# EXPERIMENTAL: Object Oriented interface for YAML 1.2
# Incompatible to functional interface!
my $xs = YAML::XS->new;
my $yaml = $xs->dump([ 1..4 ]);
my $array = $xs->load($yaml);

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
%setup -q -n YAML-LibYAML-v0.904.0
cd %{_builddir}/YAML-LibYAML-v0.904.0
pushd ..
cp -a YAML-LibYAML-v0.904.0 buildavx2
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
cp %{_builddir}/YAML-LibYAML-v%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML/0c0d651ab068ba7132a397e5cfccee4a044e04a2 || :
cp %{_builddir}/YAML-LibYAML-v%{version}/LibYAML/License %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML/75c83b388350c9f313c608a57313314cf7767208 || :
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
/usr/share/package-licenses/perl-YAML-LibYAML/0c0d651ab068ba7132a397e5cfccee4a044e04a2
/usr/share/package-licenses/perl-YAML-LibYAML/75c83b388350c9f313c608a57313314cf7767208

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
