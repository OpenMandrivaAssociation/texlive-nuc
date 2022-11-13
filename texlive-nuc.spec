Name:		texlive-nuc
Version:	22256
Release:	1
Summary:	Notation for nuclear isotopes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nuc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nuc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nuc.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
