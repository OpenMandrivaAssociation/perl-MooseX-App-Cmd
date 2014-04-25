%define upstream_name    MooseX-App-Cmd
%define upstream_version 0.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Reads from config file


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Mouse)
BuildRequires: perl(Any::Moose)
BuildRequires:	perl(App::Cmd)
BuildRequires:	perl(Getopt::Long::Descriptive)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Test::Output)
BuildRequires:  perl(namespace::autoclean)
BuildArch:	noarch

%description
This module marries the App::Cmd manpage with the MooseX::Getopt manpage.

Use it like the App::Cmd manpage advises (especially see the
App::Cmd::Tutorial manpage), swapping the App::Cmd::Command manpage for the
MooseX::App::Cmd::Command manpage.

Then you can write your moose commands as moose classes, with the
MooseX::Getopt manpage defining the options for you instead of 'opt_spec'
returning a the Getopt::Long::Descriptive manpage spec.

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
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


