
Summary:	Simple gui for dvd authoring.
Summary(pl.UTF-8):	Prosty program do tworzenia dvd wideo.
Name:		devede
Version:	3.14.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
# Source0-md5:	f7304e9276862758f6e4aa0bdbd0fc49
URL:		http://www.rastersoft.com/programas/devede.html
BuildArch:	noarch
Requires:	python
Requires:	pygtk
Requires:	pyglade
Requires:	mplayer
Requires:	mencoder
Requires:	dvdauthor
Requires:	vcdimager
Requires:	mkisofs

%description
Simple gui for dvd authoring.

%description -l pl.UTF-8
Prosty program do tworzenia dvd wideo.

%prep
%setup -q %{SOURCE0}
echo $RPM_BUILD_ROOT

%build
export DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
./install.sh --targeted=yes --prefix $RPM_BUILD_ROOT%{_prefix} --pkglibdir $RPM_BUILD_ROOT%{_datadir}/devede/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,video) %{_bindir}/devede
%attr(755,root,video) %{_datadir}/devede/scripts/devede_*.py
%{_datadir}/applications/devede.desktop
%{_datadir}/devede/*.ui
%{_datadir}/devede/*.png
%{_datadir}/devede/*.mpg
%{_datadir}/devede/codepages.lst
%{_datadir}/devede/devedesans.ttf
%{_datadir}/devede/devede.svg
%{_datadir}/devede/languages.lst
%{_datadir}/devede/silence.mp3
%{_datadir}/locale
%{_datadir}/pixmaps/*
%doc %{_docdir}/devede/*
