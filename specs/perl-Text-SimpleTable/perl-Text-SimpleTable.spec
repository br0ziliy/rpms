# $Id$
# Authority: dries
# Upstream: Marcus Ramberg <mramberg@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-SimpleTable

Summary: Simple Eyecandy ASCII Tables
Name: perl-Text-SimpleTable
Version: 2.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-SimpleTable/

Source: http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/Text-SimpleTable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.008001
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(Test::More)
Requires: perl >= 5.008001

%filter_from_requires /^perl*/d
%filter_setup

%description
Simple eyecandy ASCII tables, as seen in Catalyst.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Text::SimpleTable.3pm*
%{perl_vendorlib}/Text/SimpleTable.pm

%changelog
* Fri Apr 16 2010 Christoph Maser <cmr@financial.com> - 2.03-1
- Updated to version 2.03.

* Thu Mar 11 2010 Christoph Maser <cmr@financial.com> - 2.02-1
- Updated to version 2.02.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 2.0-1
- Updated to version 2.0.

* Mon Aug  3 2009 Christoph Maser <cmr@financial.com> - 1.8-1
- Updated to version 1.8.

* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 1.4-1
- Updated to version 1.4.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.2-1
- Updated to version 1.2.

* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 1.1-1
- Updated to version 1.1.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.03-2
- Changed to use destdir with perl(Module::Build).

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
