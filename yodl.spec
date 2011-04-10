Summary:	Yodl: Yet oneOther Document Language
Summary(pl.UTF-8):	Yodl: Jeszcze jeden język opisu dokumentów
Name:		yodl
Version:	3.00.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/yodl/%{name}_%{version}.orig.tar.gz
# Source0-md5:	804703769e7995e25f5f5dd59ca3377c
URL:		http://downloads.sourceforge.net/
BuildRequires:	bash
BuildRequires:	icmake
BuildRequires:	python
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
sed -i -e 's#-O2#%{rpmcflags} %{rpmcppflags}#g' build
sed -i -e 's#gcc#%{__cc}#g' INSTALL.im

%build
./build programs
./build man
./build manual
./build macros

%install
rm -rf $RPM_BUILD_ROOT

./build install programs $RPM_BUILD_ROOT
./build install man $RPM_BUILD_ROOT
./build install manual $RPM_BUILD_ROOT
./build install macros $RPM_BUILD_ROOT
./build install docs $RPM_BUILD_ROOT

cp -a $RPM_BUILD_ROOT%{_datadir}/doc/yodl-doc .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES README* yodl-doc
%attr(755,root,root) %{_bindir}/yodl*
%{_datadir}/yodl
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
