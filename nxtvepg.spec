Name:			nxtvepg
Version:		2.8.1
Release:		5

Summary:	NexTView EPG decoder and browser
License:	GPLv2+
Group:		Video
URL:		https://nxtvepg.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-icon-16.png
Source2:	%{name}-icon-32.png
Source3:	%{name}-icon-48.png

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	tk
BuildRequires:	tk-devel
BuildRequires:	tcl
BuildRequires:	tcl-devel

Requires:	tcl
Requires:	tk

%description
This is a decoder and browser for nexTView - an Electronic TV Programme Guide
for the analog domain (as opposed to the various digital EPGs that come with
most digital broadcasts). It allows you to decode and browse TV programme
listings for most of the major networks in Germany, Austria, France and
Switzerland.

Currently Nextview EPG is transmitted by:
- in Germany and Austria: Kabel1, 3Sat, RTL-II.
- in Switzerland: SF1, TSR1, TSI1, EuroNews.
- in France: Canal+, M6.
- in Turkey: TRT.

If you don't receive any of those, then this software unfortunately is
almost useless to you, except for a demo mode. For more details please
refer to the documentation in the "Help" menus or the UNIX manual page.

%prep
%setup -q

%build
make prefix="%{_prefix}" TCL_VER=%{tcl_version} \
 TCL_LIBRARY_PATH=%{_datadir}/tcl%{tcl_version} \
 TK_LIBRARY_PATH=%{_datadir}/tk%{tcl_version}

%install
rm -rf %{buildroot}
make ROOT=%{buildroot} prefix=%{_prefix} resdir=%{buildroot}%{_libdir}/X11 \
 mandir=%{buildroot}%{_mandir}/man1 install

# menu
install %{SOURCE1} -D -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install %{SOURCE2} -D -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install %{SOURCE3} -D -m 644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Nxtvepg
Comment=NexTView EPG decoder and browser
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;Video;AudioVideoEditing;Recorder;
EOF
			
%clean
rm -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc README CHANGES COPYRIGHT TODO nxtvepg.pod pod2help.pl manual.html
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}d
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/%{name}
%{_libdir}/X11/app-defaults/*
%{_mandir}/man1/*



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.1-3mdv2011.0
+ Revision: 613113
- the mass rebuild of 2010.1 packages

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 2.8.1-2mdv2010.1
+ Revision: 541226
- update BR

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 2.8.1-1mdv2009.1
+ Revision: 328705
- Build fixes
- Release 2.8.1

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 2.8.0-4mdv2009.1
+ Revision: 310196
- adjust for new location of tcl stuff
- rebuild for new tcl

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.8.0-3mdv2009.0
+ Revision: 254151
- rebuild

* Sat Jan 12 2008 Adam Williamson <awilliamson@mandriva.org> 2.8.0-1mdv2008.1
+ Revision: 149662
- rebuild for new tcl/tk
- don't manually bzip the manpages
- drop Mandriva-specific category from XDG menu
- fd.o icons
- new license policy
- spec clean
- new release 2.8.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Wed Mar 14 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.7.7-2mdv2007.1
+ Revision: 143565
- Fix XDG menu

* Mon Jan 22 2007 Lenny Cartier <lenny@mandriva.com> 2.7.7-1mdv2007.1
+ Revision: 111752
- Update to 2.7.7
- Import nxtvepg

* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 2.7.6-5mdk
- Requires tk, really fix #21928

* Wed Apr 19 2006 Michael Scherer <misc@mandriva.org> 2.7.6-4mdk
- Requires tcl ( fix #21928 )

* Tue Jan 03 2006 Oden Eriksson <oeriksson@mandriva.com> 2.7.6-3mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps
- added some lib64 fixes

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.7.6-2mdk
- BuildRequires Fix

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.7.6-1mdk
- 2.7.6

* Wed Mar 09 2005 Laurent Culioli <laurent@mandrake.org> 2.7.4-1mdk
- 2.7.4

* Wed Jun 16 2004 Laurent Culioli <laurent@mandrake.org> 2.7.0-1mdk
- 2.7.0

