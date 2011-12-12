Summary:	Simple GUI for DVD/CD authoring
Summary(pl.UTF-8):	Prosty interfejs do tworzenia filmów DVD/CD
Name:		devede
Version:	3.20.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
# Source0-md5:	1f98cab95272277a3b78a8e53664880c
URL:		http://www.rastersoft.com/programas/devede.html
Patch0:		%{name}_scriptspath.patch
BuildRequires:	rpm-pythonprov
Requires:	dvdauthor
Requires:	mencoder
Requires:	mkisofs
Requires:	mplayer
Requires:	python-pygtk-glade
Requires:	vcdimager
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple GUI for DVD/CD authoring.

%description -l pl.UTF-8
Prosty interfejs do tworzenia filmów DVD/CD.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

export DESTDIR=$RPM_BUILD_ROOT
./install.sh --targeted=yes \
	--prefix %{_prefix} \
	--pkglibdir %{_datadir}/devede/scripts \
	--pkgdocdir %{_docdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_bindir}/devede[-_]debug

mv $RPM_BUILD_ROOT%{_datadir}/locale/{de_DE,de}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{hu_HU,hu}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{it_IT,it}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{nb_NO,nb}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{pt_PT,pt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc changes.txt docs/*
%attr(755,root,video) %{_bindir}/devede
%dir %{_datadir}/devede
%dir %{_datadir}/devede/scripts
%attr(755,root,video) %{_datadir}/devede/scripts/devede_*.py
%{_datadir}/devede/backgrounds
%{_datadir}/devede/*.ui
%{_datadir}/devede/*.png
%{_datadir}/devede/*.mpg
%{_datadir}/devede/codepages.lst
%{_datadir}/devede/devede.svg
%{_datadir}/devede/devedesans.ttf
%{_datadir}/devede/languages.lst
%{_datadir}/devede/silence.ogg
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.svg
