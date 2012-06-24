%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       IPv4
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - IPv4 network calculations and validation
Summary(pl):	%{_class}_%{_subclass} -
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class used for calculating IPv4 (AF_INET family) address information
such as network as addresses as well as IP address validity.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
