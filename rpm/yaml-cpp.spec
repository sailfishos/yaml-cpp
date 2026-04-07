%define library_name libyaml-cpp0_9

Name:           yaml-cpp
Version:        0.9.1
Release:        1
Summary:        A YAML parser and emitter for C++
License:        MIT 
URL:            https://github.com/sailfishos/yaml-cpp
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n %{library_name}
Summary:        A YAML parser and emitter for C++

%description -n %{library_name}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{library_name} = %{version}

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

%post -n %{library_name} -p /sbin/ldconfig

%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc CONTRIBUTING.md README.md
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
