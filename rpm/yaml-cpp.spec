Name:           yaml-cpp
Version:        0.9.0
Release:        1
Summary:        A YAML parser and emitter for C++
License:        MIT 
URL:            https://github.com/sailfishos/yaml-cpp
Source0:        %{name}-%{version}.tar.gz

# When updating yaml-cpp so that the .so version changes,
# provide libyamp-cpp.so.0.N while building libyaml-cpp.so.0.N+1
# This can be disabled after the update has been completed.
%define yaml_compat 1

%if 0%{?yaml_compat:%yaml_compat}
%define old_so_version 8
%ifarch aarch64 x86-64
BuildRequires: libyaml-cpp.so.0.%{old_so_version}()(64bit)
%else
BuildRequires: libyaml-cpp.so.0.%{old_so_version}
%endif
%endif

BuildRequires:  cmake

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
%cmake_build


%install
%cmake_install

%if %{yaml_compat}
cp -av %{_libdir}/libyaml-cpp.so.0.%{old_so_version}* $RPM_BUILD_ROOT%{_libdir}/
%endif

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
