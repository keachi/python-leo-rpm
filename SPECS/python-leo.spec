%define __python /usr/bin/python2.7

Name:           python-leo
Version:        1.1.2
Release:        3%{?dist}
Summary:        Python library for leo dict
License:        Apache

Source0:        https://github.com/keachi/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}

Requires:       python2-lxml python-beautifulsoup4

%description
Python library for leo dict.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%license LICENSE.txt
#%doc README.md
%{python_sitelib}/*
%{_prefix}/bin/leo
%{_prefix}/bin/train
