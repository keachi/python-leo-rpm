%global srcname leo

Name:           python-%{srcname}
Version:        1.1.3
Release:        2%{?dist}
Summary:        Python library for leo dict
License:        Apache

Source0:        https://github.com/keachi/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}

Requires:       python3-lxml python3-beautifulsoup4

%description
Python library for leo dict.

%prep
%autosetup -n python-%{srcname}-%{version}

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%clean
rm -rf %{buildroot}

%files -n python-%{srcname}
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/leo
%{_bindir}/train
