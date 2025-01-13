#
# Adapted from https://build.opensuse.org/projects/devel:libraries:c_c++/packages/yder/files/yder.spec
#
# <3 OpenSUSE

%define sover 1_4
Name:           yder
Version:        1.4.20
Release:        0
Summary:        Logging library written in C
# Example programs in subfolder examples/ are licensed under MIT
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/babelouest/yder
Source:         https://github.com/babelouest/yder/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liborcania) >= 2.0.0
BuildRequires:  pkgconfig(libsystemd)

%description
Yder is a logging library where messages can be logged to console,
files, syslog or journald.

Yder is single-threaded, which means that only one instance of yder
logging can be used at the same time in a program.

%package -n libyder%{sover}
Summary:        Logging library written in C
Group:          System/Libraries

%description -n libyder%{sover}
Yder is a logging library where messages can be logged to console,
files, syslog or journald.

Yder is single-threaded, which means that only one instance of yder
logging can be used at the same time in a program.

%package devel
Summary:        Header files for yder
Group:          Development/Libraries/C and C++
Requires:       libyder%{sover} = %{version}

%description devel
Development and header files for yder.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc/

%post   -n libyder%{sover} -p /sbin/ldconfig
%postun -n libyder%{sover} -p /sbin/ldconfig

%files -n libyder%{sover}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/libyder.so.*

%files devel
%{_includedir}/yder.h
%{_includedir}/yder-cfg.h
%{_libdir}/libyder.so
%{_libdir}/cmake/Yder
%{_libdir}/pkgconfig/libyder.pc

%changelog
