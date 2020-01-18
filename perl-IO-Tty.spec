Name:           perl-IO-Tty
Version:        1.10
Release:        11%{?dist}
Summary:        Perl interface to pseudo tty's
License:        (GPL+ or Artistic) and BSD
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/IO-Tty/
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/IO-Tty-%{version}.tar.gz
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
IO::Tty and IO::Pty provide an interface to pseudo tty's.

%prep
%setup -q -n IO-Tty-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/IO/
%{_mandir}/man3/*.3pm*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.10-11
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.10-10
- Mass rebuild 2013-12-27

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 1.10-9
- Buildrequire perl(Cwd), simplify filters

* Thu Nov 15 2012 Petr Šabata <contyk@redhat.com> - 1.10-8
- Fix the dependencies
- Re-enable the test suite
- Modernize the spec
- Correct the license tag

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.10-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.10-4
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.10-3
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Steven Pritchard <steve@kspei.com> 1.10-1
- Update to 1.10.
- Use fixperms macro instead of our own chmod incantation.
- Update Source0 URL.
- BR Test::More.

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-6
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.08-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 16 2009 Chris Weyl <cweyl@alumni.drew.edu> - 1.08-2
- filter out private Perl .so provides

* Wed Feb 25 2009 Paul Howarth <paul@city-fan.org> - 1.08-1
- Update to 1.08 (add support for posix_openpt())
- Fix argument order for find with -depth

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-5
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.07-4
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.07-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-2
- Rebuild for FC6.

* Fri Jul 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-1
- Update to 1.07.

* Tue Jul 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.

* Sat Jun 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- Update to 1.05.

* Wed May 31 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-1
- Update to 1.04.

* Tue May  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- Update to 1.03.
- Taking maintainership.

* Tue Feb 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.02-5
- Rebuild.

* Tue Jan 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.02-4
- Rebuild, cosmetic cleanups.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.02-3
- rebuilt

* Sun Feb  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.02-0.fdr.2
- Reduce directory ownership bloat.

* Fri Nov 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.02-0.fdr.1
- First build.
