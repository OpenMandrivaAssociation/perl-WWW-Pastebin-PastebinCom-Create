%define upstream_name    WWW-Pastebin-PastebinCom-Create
%define upstream_version 1.003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Paste to http://pastebin.com from Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/WWW-Pastebin-PastebinCom-Create-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(overload)

BuildArch:	noarch

%description
The module provides means of pasting large texts into the
http://pastebin.com manpage pastebin site.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/WWW

%changelog
* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 526460
- update to 0.003

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.002-2mdv2010.0
+ Revision: 440747
- rebuild

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.002-1mdv2009.1
+ Revision: 330951
- update to new version 0.002
- update to new version 0.002

* Fri Jan 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.001-1mdv2009.1
+ Revision: 327407
- import perl-WWW-Pastebin-PastebinCom-Create


* Fri Jan 09 2009 cpan2dist 0.001-1mdv
- initial mdv release, generated with cpan2dist



