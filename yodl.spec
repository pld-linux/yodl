Summary:	Yodl: Yet oneOther Document Language
Summary(pl):	Yodl: Jeszcze jeden jêzyk opisu dokumentów
Name:		yodl
Version:	1.31.18
Release:	3
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.lilypond.org/pub/yodl/development/%{name}-%{version}.tar.gz
URL:		http://www.xs4all.nl/~jantien/yodl/
BuildRequires:	bash
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Yodl is a package that implements a pre-document language and tools to
process it. The idea of Yodl is that you write up a document in a
pre-language, then use the tools (e.g. yodl2html) to convert it to
some final document language. Current converters are for HTML, ms,
man, LaTeX SGML and texinfo, plus a poor-man's text converter. Main
document types are "article", "report", "book" and "manpage". The Yodl
document language is designed to be easy to use and extensible.

%description -l pl
Yodl to pakiet z implementacj± jêzyka pre-dokumentu i narzêdzi do jego
przetwarzania. Idea Yodla jest taka, ¿e pisze siê dokument w
pre-jêzyku, nastêpnie u¿ywa narzêdzi (np. yodl2html) by
przekonwertowaæ go do jakiego¶ docelowego jêzyka dokumentu. Aktualnie
yodl zawiera konwertery do: HTML, ms, man, LaTeX, SGML i texinfo, oraz
text. G³ówne typy dokumentów to "artyku³", "raport", "ksi±¿ka" i
"strona podrêcznika man". Jêzyk Yodl by³ projektowany tak, by byæ
³atwy w u¿yciu i rozszerzalny.

%prep
%setup -q

%build
ac_cv_prog_BASH=/bin/bash; export ac_cv_prog_BASH
%configure2_13 
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C Documentation info || true
%{__make} install \
	prefix=$RPM_BUILD_ROOT/%{_prefix} \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir}/yodl

gzip -9nf ANNOUNCE.txt AUTHORS.txt PATCHES.txt README.txt \
	CHANGES TODO ANNOUNCE-1.22 ChangeLog-1.22

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
# verbatim include of Documentation: list the directory without issuing a %dir
%doc Documentation
%attr(755,root,root) %{_bindir}/*
%{_datadir}/yodl

%{_mandir}/man?/*
