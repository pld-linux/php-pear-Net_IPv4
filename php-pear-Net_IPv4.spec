%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       IPv4
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - IPv4 network calculations and validation
Summary(pl):	%{_pearname} - obliczanie i kontrola adresów sieciowych IPv4
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aefbe0cd84023b8dab4256b24878d808
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class used for calculating IPv4 (AF_INET family) address information
such as network addresses as well as IP address validity.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa s³u¿y do obliczania informacji o adresach sieciowych IPv4
(rodzina AF_INET) takich jak adresy sieci, a tak¿e sprawdzania
poprawno¶ci adresów IP.

Ta klasa ma w PEAR status: %{_status}.

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
