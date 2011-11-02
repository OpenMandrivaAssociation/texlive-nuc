Name:		texlive-nuc
Version:	0.1
Release:	1
Summary:	Notation for nuclear isotopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nuc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nuc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nuc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A simple package providing nuclear sub- and superscripts as
commonly used in radiochemistry, radiation science, and nuclear
physics and engineering applications. Isotopes which have Z
with more digits than A require special spacing to appear
properly; this spacing is supported in the package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
