%undefine __cmake_in_source_build

%global commit      3f54c301ead1bbe6529df4ecfb63c7f645dd181c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20220324
%global gitrel      .%{commit_date}.git%{shortcommit}

Name: tdlib
Version: 1.8.5
Release: 1%{?dist}

License: Boost
URL: https://github.com/%{name}/td
Summary: Cross-platform library for building Telegram clients
Source0: %{url}/archive/%{commit}.tar.gz

BuildRequires: gperftools-devel
BuildRequires: openssl-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: cmake
BuildRequires: gcc

Provides: bundled(sqlite) = 3.31.0

# Building with default settings require at least 16 GB of free RAM.
# Builds on ARM and other low-memory architectures are failing.
ExclusiveArch: x86_64 aarch64

%description
TDLib (Telegram Database library) is a cross-platform library for
building Telegram clients. It can be easily used from almost any
programming language.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n td-%{commit} -p1
sed -e 's/"DEFAULT"/"PROFILE=SYSTEM"/g' -i tdnet/td/net/SslStream.cpp

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DTD_ENABLE_JNI:BOOL=OFF \
    -DTD_ENABLE_DOTNET:BOOL=OFF
%cmake_build --target tdjson

%install
%cmake_install

%files
%license LICENSE_1_0.txt
%doc README.md CHANGELOG.md
%{_libdir}/libtd*.so.%{version}

%files devel
%{_includedir}/td
%{_libdir}/libtd*.so
%{_libdir}/cmake/Td
%{_libdir}/pkgconfig/td*.pc

%changelog
* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 1.8.5-1
- Disable static (shlyakpavel@gmail.com)

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 1.8.4-1
- Fix (shlyakpavel@gmail.com)

* Mon Jun 13 2022 Pavel Shlyak <shlyakpavel@gmail.com> 1.8.3-1
- new package built with tito

* Tue Feb 15 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.8.0-1
- Version 1.8.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.7.0-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.0-1
- Updated to version 1.7.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
