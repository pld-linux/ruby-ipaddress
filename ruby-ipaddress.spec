%define pkgname ipaddress
Summary:	IPv4/IPv6 addresses manipulation library
Name:		ruby-%{pkgname}
Version:	0.8.3
Release:	1
License:	Distributable
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	15c3ce3bcf68ecaee8d25070b033bcac
URL:		http://github.com/bluemonk/ipaddress
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPAddress is a Ruby library designed to make manipulation of IPv4 and
IPv6 addresses both powerful and simple. It mantains a layer of
compatibility with Ruby's own IPAddr, while addressing many of its
issues.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGELOG.rdoc LICENSE.txt
%{ruby_vendorlibdir}/ipaddress.rb
%{ruby_vendorlibdir}/ipaddress
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
