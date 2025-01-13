#
# Adapted from https://build.opensuse.org/projects/devel:libraries:c_c++/packages/orcania/files/orcania.spec
#
# <3 OpenSUSE

%define sover 2_3
Name:           orcania
Version:        2.3.3
Release:        0
Summary:        MISC function Library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/babelouest/orcania
Source:         https://github.com/babelouest/orcania/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
Different functions for different purposes but that can be shared
between other projects.

%package -n liborcania%{sover}
Summary:        MISC function library
Group:          System/Libraries

%description -n liborcania%{sover}
Different functions for different purposes but that can be shared
between other projects.

%package devel
Summary:        Header files for orcania
Group:          Development/Libraries/C and C++
Requires:       liborcania%{sover} = %{version}

%description devel
Development and header files for orcania.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post   -n liborcania%{sover} -p /sbin/ldconfig
%postun -n liborcania%{sover} -p /sbin/ldconfig

%files -n liborcania%{sover}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/liborcania.so.*

%files devel
%{_bindir}/base64url
%{_mandir}/man1/base64url.1.gz
%{_includedir}/orcania.h
%{_includedir}/orcania-cfg.h
%{_libdir}/liborcania.so
%{_libdir}/pkgconfig/liborcania.pc
%{_libdir}/cmake/Orcania

%changelog
