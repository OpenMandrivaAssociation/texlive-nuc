# revision 22256
# category Package
# catalog-ctan /macros/latex/contrib/nuc
# catalog-date 2011-04-28 12:45:40 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-nuc
Version:	0.1
Release:	4
Summary:	Notation for nuclear isotopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nuc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nuc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nuc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A simple package providing nuclear sub- and superscripts as
commonly used in radiochemistry, radiation science, and nuclear
physics and engineering applications. Isotopes which have Z
with more digits than A require special spacing to appear
properly; this spacing is supported in the package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nuc/nuc.sty
%doc %{_texmfdistdir}/doc/latex/nuc/README
%doc %{_texmfdistdir}/doc/latex/nuc/nuc.pdf
%doc %{_texmfdistdir}/doc/latex/nuc/nuc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 754447
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719141
- texlive-nuc
- texlive-nuc
- texlive-nuc
- texlive-nuc

