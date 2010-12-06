Name:			nxtvepg
Version:		2.8.1
Release:		%mkrel 3

Summary:	NexTView EPG decoder and browser
License:	GPLv2+
Group:		Video
URL:		http://nxtvepg.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-icon-16.png
Source2:	%{name}-icon-32.png
Source3:	%{name}-icon-48.png

BuildRequires:	libx11-devel
BuildRequires:	libxmu-devel
BuildRequires:	tk
BuildRequires:	tk-devel
BuildRequires:	tcl
BuildRequires:	tcl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

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

