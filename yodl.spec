Summary:	Yodl: Yet oneOther Document Language
Summary(pl.UTF-8):	Yodl - jeszcze jeden język opisu dokumentów
Name:		yodl
Version:	3.05.01
Release:	1
# according to src/yodl/warranty.c (although GPL v3 text is included in LICENSE)
License:	GPL v2
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/yodl/%{name}_%{version}.orig.tar.gz
# Source0-md5:	68bdd1de6da7f49e510da69a99dc26f2
URL:		https://gitlab.com/fbb-git/yodl
BuildRequires:	bash
BuildRequires:	icmake
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	python
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_udatadir	%{_datadir}/%{name}

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

%{__sed} -i -e 's#-O2#%{rpmcflags} %{rpmcppflags}#g' build
%{__sed} -i -e '/COMPILER/ s#gcc#%{__cc}#' -e '/CXX/ s#g++#%{__cxx}#' INSTALL.im

%build
./build programs
./build macros
./build man
./build manual

%install
rm -rf $RPM_BUILD_ROOT

./build install programs $RPM_BUILD_ROOT
./build install macros $RPM_BUILD_ROOT
./build install man $RPM_BUILD_ROOT
./build install manual $RPM_BUILD_ROOT
./build install docs $RPM_BUILD_ROOT

rm -rf yodl-doc
%{__mv} $RPM_BUILD_ROOT%{_datadir}/doc/yodl-doc .
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/yodl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES README* changelog yodl-doc
%attr(755,root,root) %{_bindir}/yodl*
%{_datadir}/yodl
%{_mandir}/man1/yodl*.1*
%{_mandir}/man7/yodl*.7*
