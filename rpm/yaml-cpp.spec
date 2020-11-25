Name:           yaml-cpp
Version:        0.6.3
Release:        1
Summary:        A YAML parser and emitter for C++
License:        MIT 
URL:            https://github.com/jbeder/yaml-cpp
Source0:        %{name}-%{version}.tar.gz

Patch0:         CVE-2017-5950.patch

BuildRequires:  cmake gcc gcc-c++

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream


%build
%cmake \
       -DYAML_CPP_BUILD_TOOLS=OFF \
       -DYAML_BUILD_SHARED_LIBS=ON \
       -DYAML_CPP_BUILD_TESTS=OFF \
       %{nil}
%make_build


%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc CONTRIBUTING.md README.md
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

