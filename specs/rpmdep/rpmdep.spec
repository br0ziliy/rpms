# $Id: $

# Authority: dries
# Upstream: dries

Summary: Check the dependencies of source and binary rpms
Name: rpmdep
Version: 1.0
Release: 1
License: GPL
Group: Development/Libraries
URL: none

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: rpmdep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires:  

%description
This checks the dependencies of source and binary rpms. 
This program is still in development and far from finished.

%prep
%setup -n rpmdep

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/rpmdep

%changelog
* Mon Aug 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
