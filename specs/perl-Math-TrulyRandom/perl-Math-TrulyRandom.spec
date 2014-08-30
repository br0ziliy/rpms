# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-TrulyRandom

Summary: Perl interface to a truly random number generator function
Name: perl-Math-TrulyRandom
Version: 1.0
Release: 1.3%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-TrulyRandom/

Source: http://www.cpan.org/modules/by-module/Math/Math-TrulyRandom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Perl interface to a truly random number generator function.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Change to real perl. (Please fix upstream)
%{__perl} -pi -e 's|^#!\s+/.*bin/perl|#!%{__perl}|i' *.pm

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/TrulyRandom.pm
%doc %{perl_vendorarch}/Math/TrulyRandom.pod
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/TrulyRandom/

%changelog
* Sun Aug 30 2014 Vasyl "Br0ziliy" Kaigorodov <vkaigoro@redhat.com> - 1.2-1.3
- Fixed .spec file to build correctly on .el6

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
