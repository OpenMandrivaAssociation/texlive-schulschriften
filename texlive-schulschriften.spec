Name:		texlive-schulschriften
Version:	20190228
Release:	1
Summary:	German "school scripts" from Suetterlin to the present day
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/schulschriften
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schulschriften.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schulschriften.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Das Paket enthalt im wesentlichen die METAFONT-Quellfiles fur
die folgenden Schulausgangsschriften: Suetterlinschrift,
Deutsche Normalschrift, Lateinische Ausgangsschrift,
Schulausgangsschrift, Vereinfachte Ausgangsschrift. Damit ist
es moglich, beliebige deutsche Texte in diesen Schreibschriften
zu schreiben.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/schulschriften
%{_texmfdistdir}/fonts/tfm/public/schulschriften
%{_texmfdistdir}/tex/latex/schulschriften
%doc %{_texmfdistdir}/doc/fonts/schulschriften

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
