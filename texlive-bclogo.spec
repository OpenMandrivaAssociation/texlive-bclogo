# revision 23305
# category Package
# catalog-ctan /graphics/bclogo
# catalog-date 2011-08-01 12:18:46 +0200
# catalog-license lppl
# catalog-version 2.26
Name:		texlive-bclogo
Version:	2.26
Release:	5
Summary:	Creating colourful boxes with logos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/bclogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bclogo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bclogo.doc.tar.xz
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
%{_texmfdistdir}/metapost/bclogo/bc-attention.mp
%{_texmfdistdir}/metapost/bclogo/bc-aux-301.mp
%{_texmfdistdir}/metapost/bclogo/bc-bombe.mp
%{_texmfdistdir}/metapost/bclogo/bc-book.mp
%{_texmfdistdir}/metapost/bclogo/bc-calendrier.mp
%{_texmfdistdir}/metapost/bclogo/bc-cle.mp
%{_texmfdistdir}/metapost/bclogo/bc-clefa.mp
%{_texmfdistdir}/metapost/bclogo/bc-clesol.mp
%{_texmfdistdir}/metapost/bclogo/bc-coeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-crayon.mp
%{_texmfdistdir}/metapost/bclogo/bc-cube.mp
%{_texmfdistdir}/metapost/bclogo/bc-dallemagne.mp
%{_texmfdistdir}/metapost/bclogo/bc-danger.mp
%{_texmfdistdir}/metapost/bclogo/bc-dautriche.mp
%{_texmfdistdir}/metapost/bclogo/bc-dbelgique.mp
%{_texmfdistdir}/metapost/bclogo/bc-dbulgarie.mp
%{_texmfdistdir}/metapost/bclogo/bc-dfrance.mp
%{_texmfdistdir}/metapost/bclogo/bc-ditalie.mp
%{_texmfdistdir}/metapost/bclogo/bc-dluxembourg.mp
%{_texmfdistdir}/metapost/bclogo/bc-dodecaedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-dpaysbas.mp
%{_texmfdistdir}/metapost/bclogo/bc-dz.mp
%{_texmfdistdir}/metapost/bclogo/bc-eclaircie.mp
%{_texmfdistdir}/metapost/bclogo/bc-etoile.mp
%{_texmfdistdir}/metapost/bclogo/bc-femme.mp
%{_texmfdistdir}/metapost/bclogo/bc-feujaune.mp
%{_texmfdistdir}/metapost/bclogo/bc-feurouge.mp
%{_texmfdistdir}/metapost/bclogo/bc-feutricolore.mp
%{_texmfdistdir}/metapost/bclogo/bc-feuvert.mp
%{_texmfdistdir}/metapost/bclogo/bc-fleur.mp
%{_texmfdistdir}/metapost/bclogo/bc-homme.mp
%{_texmfdistdir}/metapost/bclogo/bc-horloge.mp
%{_texmfdistdir}/metapost/bclogo/bc-icosaedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-info.mp
%{_texmfdistdir}/metapost/bclogo/bc-inter.mp
%{_texmfdistdir}/metapost/bclogo/bc-interdit.mp
%{_texmfdistdir}/metapost/bclogo/bc-lampe.mp
%{_texmfdistdir}/metapost/bclogo/bc-loupe.mp
%{_texmfdistdir}/metapost/bclogo/bc-neige.mp
%{_texmfdistdir}/metapost/bclogo/bc-note.mp
%{_texmfdistdir}/metapost/bclogo/bc-nucleaire.mp
%{_texmfdistdir}/metapost/bclogo/bc-octaedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-oeil.mp
%{_texmfdistdir}/metapost/bclogo/bc-orne.mp
%{_texmfdistdir}/metapost/bclogo/bc-ours.mp
%{_texmfdistdir}/metapost/bclogo/bc-outil.mp
%{_texmfdistdir}/metapost/bclogo/bc-peaceandlove.mp
%{_texmfdistdir}/metapost/bclogo/bc-pluie.mp
%{_texmfdistdir}/metapost/bclogo/bc-plume.mp
%{_texmfdistdir}/metapost/bclogo/bc-poisson.mp
%{_texmfdistdir}/metapost/bclogo/bc-recyclage.mp
%{_texmfdistdir}/metapost/bclogo/bc-rosevents.mp
%{_texmfdistdir}/metapost/bclogo/bc-smiley-bonnehumeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-smiley-mauvaisehumeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-soleil.mp
%{_texmfdistdir}/metapost/bclogo/bc-stop.mp
%{_texmfdistdir}/metapost/bclogo/bc-takecare.mp
%{_texmfdistdir}/metapost/bclogo/bc-tetraedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-trefle.mp
%{_texmfdistdir}/metapost/bclogo/bc-trombone.mp
%{_texmfdistdir}/metapost/bclogo/bc-valetcoeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-velo.mp
%{_texmfdistdir}/metapost/bclogo/bc-yin.mp
%{_texmfdistdir}/metapost/bclogo/brace.mp
%{_texmfdistdir}/metapost/bclogo/losanges.mp
%{_texmfdistdir}/metapost/bclogo/spir.mp
%{_texmfdistdir}/tex/latex/bclogo/bc-attention.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-aux-301.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-bombe.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-book.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-calendrier.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-cle.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-clefa.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-clesol.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-coeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-crayon.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-cube.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dallemagne.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-danger.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dautriche.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dbelgique.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dbulgarie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dfrance.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-ditalie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dluxembourg.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dodecaedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dpaysbas.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dz.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-eclaircie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-etoile.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-femme.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feujaune.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feurouge.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feutricolore.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feuvert.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-fleur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-homme.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-horloge.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-icosaedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-info.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-inter.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-interdit.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-lampe.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-loupe.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-neige.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-note.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-nucleaire.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-octaedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-oeil.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-orne.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-ours.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-outil.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-peaceandlove.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-pluie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-plume.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-poisson.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-recyclage.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-rosevents.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-smiley-bonnehumeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-smiley-mauvaisehumeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-soleil.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-stop.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-takecare.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-tetraedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-trefle.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-trombone.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-valetcoeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-velo.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-yin.mps
%{_texmfdistdir}/tex/latex/bclogo/bclogo.sty
%doc %{_texmfdistdir}/doc/latex/bclogo/LISEZ-MOI.doc
%doc %{_texmfdistdir}/doc/latex/bclogo/LISEZ-MOI.latex
%doc %{_texmfdistdir}/doc/latex/bclogo/README.doc
%doc %{_texmfdistdir}/doc/latex/bclogo/README.latex
%doc %{_texmfdistdir}/doc/latex/bclogo/bclogo-doc.pdf
%doc %{_texmfdistdir}/doc/latex/bclogo/bclogo-doc.tex
%doc %{_texmfdistdir}/doc/latex/bclogo/brace.mps
%doc %{_texmfdistdir}/doc/latex/bclogo/losanges.mps
%doc %{_texmfdistdir}/doc/latex/bclogo/spir.mps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.26-2
+ Revision: 749525
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.26-1
+ Revision: 717893
- texlive-bclogo
- texlive-bclogo
- texlive-bclogo
- texlive-bclogo
- texlive-bclogo

