Summary:	Yodl: Yet oneOther Document Language
Summary(pl.UTF-8):   Yodl: Jeszcze jeden język opisu dokumentów
Name:		yodl
Version:	1.31.18
Release:	5
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.lilypond.org/pub/yodl/development/%{name}-%{version}.tar.gz
# Source0-md5:	247c5bf178baeb1f0b96511323f30a61
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

%description -l pl.UTF-8
Yodl to pakiet z implementacją języka pre-dokumentu i narzędzi do jego
przetwarzania. Idea Yodla jest taka, że pisze się dokument w
pre-języku, następnie używa narzędzi (np. yodl2html) by
przekonwertować go do jakiegoś docelowego języka dokumentu. Aktualnie
yodl zawiera konwertery do: HTML, ms, man, LaTeX, SGML i texinfo, oraz
text. Główne typy dokumentów to "artykuł", "raport", "książka" i
"strona podręcznika man". Język Yodl był projektowany tak, by być
łatwy w użyciu i rozszerzalny.

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
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}/yodl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.txt AUTHORS.txt PATCHES.txt README.txt CHANGES TODO
%doc ANNOUNCE-1.22 ChangeLog-1.22
# verbatim include of Documentation: list the directory without issuing a %dir
%doc Documentation
%attr(755,root,root) %{_bindir}/*
%{_datadir}/yodl

%{_mandir}/man?/*
