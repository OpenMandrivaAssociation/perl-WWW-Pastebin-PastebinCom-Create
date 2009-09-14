%define realname   WWW-Pastebin-PastebinCom-Create
%define version    0.002
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Paste to http://pastebin.com from Perl
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/WWW/%{realname}-%{version}.tar.gz
BuildRequires: perl(Carp)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(overload)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The module provides means of pasting large texts into the
http://pastebin.com manpage pastebin site.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/WWW

