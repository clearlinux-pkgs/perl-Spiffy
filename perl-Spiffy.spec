#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Spiffy
Version  : 0.46
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/I/IN/INGY/Spiffy-0.46.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IN/INGY/Spiffy-0.46.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libspiffy-perl/libspiffy-perl_0.41-1.debian.tar.xz
Summary  : 'Spiffy Perl Interface Framework For You'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Spiffy-license = %{version}-%{release}
Requires: perl-Spiffy-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Spiffy - Spiffy Perl Interface Framework For You
SYNOPSIS
package Keen;
use Spiffy -Base;
field 'mirth';
const mood => ':-)';

%package dev
Summary: dev components for the perl-Spiffy package.
Group: Development
Provides: perl-Spiffy-devel = %{version}-%{release}
Requires: perl-Spiffy = %{version}-%{release}

%description dev
dev components for the perl-Spiffy package.


%package license
Summary: license components for the perl-Spiffy package.
Group: Default

%description license
license components for the perl-Spiffy package.


%package perl
Summary: perl components for the perl-Spiffy package.
Group: Default
Requires: perl-Spiffy = %{version}-%{release}

%description perl
perl components for the perl-Spiffy package.


%prep
%setup -q -n Spiffy-0.46
cd %{_builddir}
tar xf %{_sourcedir}/libspiffy-perl_0.41-1.debian.tar.xz
cd %{_builddir}/Spiffy-0.46
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Spiffy-0.46/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Spiffy
cp %{_builddir}/Spiffy-0.46/LICENSE %{buildroot}/usr/share/package-licenses/perl-Spiffy/cf5d6a48250e5dda7a902a071cd225d67ceed773
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Spiffy.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Spiffy/cf5d6a48250e5dda7a902a071cd225d67ceed773

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Spiffy.pm
/usr/lib/perl5/vendor_perl/5.30.2/Spiffy.pod
/usr/lib/perl5/vendor_perl/5.30.2/Spiffy/mixin.pm
