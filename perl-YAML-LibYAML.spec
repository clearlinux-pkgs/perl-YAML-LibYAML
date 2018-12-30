#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-YAML-LibYAML
Version  : 0.76
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-0.76.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-LibYAML-0.76.tar.gz
Summary  : 'Perl YAML Serialization using XS and libyaml'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-YAML-LibYAML-lib = %{version}-%{release}
Requires: perl-YAML-LibYAML-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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
Requires: perl-YAML-LibYAML-lib = %{version}-%{release}
Provides: perl-YAML-LibYAML-devel = %{version}-%{release}

%description dev
dev components for the perl-YAML-LibYAML package.


%package lib
Summary: lib components for the perl-YAML-LibYAML package.
Group: Libraries
Requires: perl-YAML-LibYAML-license = %{version}-%{release}

%description lib
lib components for the perl-YAML-LibYAML package.


%package license
Summary: license components for the perl-YAML-LibYAML package.
Group: Default

%description license
license components for the perl-YAML-LibYAML package.


%prep
%setup -q -n YAML-LibYAML-0.76

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-YAML-LibYAML/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/YAML/LibYAML.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/YAML/LibYAML.pod
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/YAML/XS.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/YAML/XS.pod
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/YAML/XS/LibYAML.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/YAML::LibYAML.3
/usr/share/man/man3/YAML::XS.3
/usr/share/man/man3/YAML::XS::LibYAML.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/YAML/XS/LibYAML/LibYAML.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-YAML-LibYAML/LICENSE
