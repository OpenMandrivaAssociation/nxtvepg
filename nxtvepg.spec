%define name	nxtvepg
%define Name	Nxtvepg
%define summary NexTView EPG decoder and browser	
%define version 2.7.7
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icon-16.png
Source2:	%{name}-icon-32.png
Source3:	%{name}-icon-48.png
URL:		http://prdownloads.sourceforge.net/nxtvepg/%{name}-%{version}.tar.bz2
Group:		Video	
BuildRequires:	X11-devel 
BuildRequires:  tk tk-devel
BuildRequires:  tcl tcl-devel
Requires: tcl tk
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

# lib64 fix
perl -pi -e "s|%{_prefix}/X11R6/lib|%{_prefix}/X11R6/%{_lib}|g" Makefile

%build
make prefix="%{prefix}"

%install
rm -rf $RPM_BUILD_ROOT

export resdir=$RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/

make prefix=$RPM_BUILD_ROOT%_prefix resdir=$RPM_BUILD_ROOT%{_prefix}/X11R6/%{_lib}/X11/ mandir=$RPM_BUILD_ROOT%_mandir/man1 install 

strip  %{buildroot}%{_bindir}/nxtvepg
chmod 644 CHANGES README
install -d -m 755 %{buildroot}%{_mandir}/man1/
install -m 644 nxtvepg.1 %{buildroot}%{_mandir}/man1/
bzip2 $RPM_BUILD_ROOT%_mandir/man1/*

# remove unwanted file
rm -rf $RPM_BUILD_ROOT%_prefix/man/man1/*

# menu
install %{SOURCE1} -D -m 644 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install %{SOURCE2} -D -m 644 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install %{SOURCE3} -D -m 644 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Nxtvepg
Comment=NexTView EPG decoder and browser
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;AudioVideo;Video;AudioVideoEditing;Recorder;
EOF
			
%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README CHANGES COPYRIGHT TODO nxtvepg.pod pod2help.pl manual.html
%{_bindir}/nxtvepg
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_prefix}/X11R6/%{_lib}/X11/app-defaults/*
%attr(644,root,root) %{_mandir}/man1/*


