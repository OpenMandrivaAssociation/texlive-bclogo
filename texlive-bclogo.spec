Name:		texlive-bclogo
Version:	69578
Release:	1
Summary:	Creating colourful boxes with logos
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/bclogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bclogo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bclogo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package facilitates the creation of colorful boxes with a
title and logo. It may use either tikz or PSTricks as graphics
engine.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/bclogo
%{_texmfdistdir}/tex/latex/bclogo
%doc %{_texmfdistdir}/doc/latex/bclogo

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}
