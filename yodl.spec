Summary:	Yodl: Yet oneOther Document Language
Name:		yodl
Version:	1.31.0
Release:	1
Copyright:	GPL
Group:		Converters/Text
Source:		ftp://ftp.lilypond.org/pub/yodl/development/%{name}-%{version}.tar.gz
URL:		http://www.xs4all.nl/~jantien/yodl/
BuildRoot:	/tmp/%{name}-%{version}-root
Prereq:		bash

%description 
Yodl  is  a  package that implements a pre-document language
and tools to process it.  The idea of Yodl is that you write
up  a  document  in a pre-language, then use the tools (e.g.
yodl2html) to convert it to some  final  document  language.
Current  converters  are  for  HTML, ms, man, LaTeX SGML and
texinfo, plus a poor-man's text  converter.   Main  document
types  are  "article",  "report", "book" and "manpage".  The
Yodl document language is designed to be  easy  to  use  and
extensible.

%prep
%setup -q

%build
export ac_cv_prog_BASH=/bin/bash
%configure --prefix=%{_prefix}
make all

%install
rm -rf $RPM_BUILD_ROOT
make -C Documentation info || true
make install \
	prefix=$RPM_BUILD_ROOT/%{_prefix} \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir}/yodl

strip --strip-unneeded $RPM_BUILD_ROOT/%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man{1,7}/* \
	ANNOUNCE.txt AUTHORS.txt COPYING INSTALL.txt PATCHES.txt README.txt \
	NEWS TODO ANNOUNCE-1.22 ChangeLog-1.22

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%doc {ANNOUNCE.txt,AUTHORS.txt,COPYING,INSTALL.txt,PATCHES.txt,README.txt}.gz
%doc {NEWS,TODO,ANNOUNCE-1.22,ChangeLog-1.22}.gz
# verbatim include of Documentation: list the directory without issuing a %dir
%doc Documentation
%dir /usr/share/yodl
%attr(755, root, root) %{_bindir}/*
/usr/share/yodl/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
* Thu Jun 24 1999 Jan RÍkorajski <baggins@pld.org.pl>
  [1.31.0-1]
- spec for PLD
