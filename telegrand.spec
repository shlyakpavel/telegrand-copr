%global commit  f9a5bd88162211846d392f8db72a3bd7aff90220
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200613

%global appname telegrand
%global uuid    com.github.melix99.telegrand.Devel

Name:           %{appname}
Version:        0.0.3
Release:        1
Summary:        Matrix messaging app for GNOME written in Rust

License:        GPLv3+
URL:            https://github.com/melix99/telegrand/
Source:		https://github.com/melix99/telegrand/archive/%{commit}/%{appname}-%{shortcommit}.tar.gz

BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  rust

BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gst-editing-services-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)

Requires:       hicolor-icon-theme

Conflicts:      %{appname}

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its interface is
optimized for collaboration in large groups, such as free software projects.


%prep
%autosetup -n telegrand-%{shortcommit}

%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appname}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{appname}.lang
%license LICENSE.txt
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.3-1
- new package built with tito

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.2-1
- new package built with tito

