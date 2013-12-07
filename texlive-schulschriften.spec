# revision 29803
# category Package
# catalog-ctan /fonts/schulschriften
# catalog-date 2012-11-15 13:07:37 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-schulschriften
Version:	20121115
Release:	5
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
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wedn14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wednsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wela14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/welasl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesa14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesasl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_end.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesu14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesub14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesubsl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wesusl14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_def.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_gr.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_kl.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_lig.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/weva14_sz.mf
%{_texmfdistdir}/fonts/source/public/schulschriften/wevasl14.mf
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wedn14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wednsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wela14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/welasl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesa14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesasl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesu14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesub14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesubsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wesusl14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/weva14.tfm
%{_texmfdistdir}/fonts/tfm/public/schulschriften/wevasl14.tfm
%{_texmfdistdir}/tex/latex/schulschriften/schulschriften_lin.sty
%{_texmfdistdir}/tex/latex/schulschriften/schulschriften_ltx.sty
%{_texmfdistdir}/tex/latex/schulschriften/t1wedn.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1wela.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1wesa.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1wesu.fd
%{_texmfdistdir}/tex/latex/schulschriften/t1weva.fd
%{_texmfdistdir}/tex/latex/schulschriften/wedn.sty
%{_texmfdistdir}/tex/latex/schulschriften/wela.sty
%{_texmfdistdir}/tex/latex/schulschriften/wesa.sty
%{_texmfdistdir}/tex/latex/schulschriften/wesu.sty
%{_texmfdistdir}/tex/latex/schulschriften/weva.sty
%doc %{_texmfdistdir}/doc/fonts/schulschriften/README
%doc %{_texmfdistdir}/doc/fonts/schulschriften/schulschriften.pdf
%doc %{_texmfdistdir}/doc/fonts/schulschriften/schulschriften.tex
%doc %{_texmfdistdir}/doc/fonts/schulschriften/schulschriften_ltx.tex
%doc %{_texmfdistdir}/doc/fonts/schulschriften/schulschriften_xpl.tex
%doc %{_texmfdistdir}/doc/fonts/schulschriften/wedn_fonttabelle.eps
%doc %{_texmfdistdir}/doc/fonts/schulschriften/wela_fonttabelle.eps
%doc %{_texmfdistdir}/doc/fonts/schulschriften/wesa_fonttabelle.eps
%doc %{_texmfdistdir}/doc/fonts/schulschriften/wesu_fonttabelle.eps
%doc %{_texmfdistdir}/doc/fonts/schulschriften/weva_fonttabelle.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
