%define tclver	8.5	

Name:		nxtvepg
Version:	2.8.0
Release:	%mkrel 3
Summary:	NexTView EPG decoder and browser
License:	GPLv2+
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-icon-16.png
Source2:	%{name}-icon-32.png
Source3:	%{name}-icon-48.png
URL:		http://nxtvepg.sourceforge.net/
Group:		Video	
BuildRequires:	X11-devel 
BuildRequires:	tk
BuildRequires:	tk-devel
BuildRequires:	tcl
BuildRequires:	tcl-devel
Requires:	tcl
Requires:	tk
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
make prefix="%{prefix}" TCL_VER=%{tclver}

%install
rm -rf %{buildroot}
export resdir=%{buildroot}%{_libdir}/X11/
make prefix=%{buildroot}%{_prefix} resdir=%{buildroot}%{_libdir}/X11/ mandir=%{buildroot}%{_mandir}/man1 install 

strip %{buildroot}%{_bindir}/nxtvepg
chmod 644 CHANGES README
install -d -m 755 %{buildroot}%{_mandir}/man1/
install -m 644 nxtvepg.1 %{buildroot}%{_mandir}/man1/

# remove unwanted file
rm -rf %{buildroot}%{_prefix}/man/man1/*

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
%defattr(-,root,root)
%doc README CHANGES COPYRIGHT TODO nxtvepg.pod pod2help.pl manual.html
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_libdir}/X11/app-defaults/*
%attr(644,root,root) %{_mandir}/man1/*

