%global commit  f9a5bd88162211846d392f8db72a3bd7aff90220
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200613

%global appname telegrand
%global uuid    com.github.melix99.telegrand.Devel

Name:           %{appname}
Version:        0.0.6
Release:        1
Summary:        Matrix messaging app for GNOME written in Rust

License:        GPLv3+
URL:            https://github.com/melix99/telegrand/
Source0:	https://github.com/melix99/telegrand/archive/%{commit}/%{appname}-%{shortcommit}.tar.gz

BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  rust

BuildRequires: meson
BuildRequires: rust-packaging
BuildRequires: dbus-devel
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: libsecret-devel
BuildRequires: itstool

Requires:       hicolor-icon-theme

%description
Fractal is a Matrix messaging app for GNOME written in Rust. Its interface is
optimized for collaboration in large groups, such as free software projects.


%prep
%autosetup -n %{appname}-%{commit} -p0

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
* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.6-1
- fix (shlyakpavel@gmail.com)

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.5-1
- 

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.4-1
- fix (shlyakpavel@gmail.com)
- fix (shlyakpavel@gmail.com)
- fix (shlyakpavel@gmail.com)

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.3-1
- new package built with tito

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 0.0.2-1
- new package built with tito

