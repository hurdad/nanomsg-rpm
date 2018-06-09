Name:           nanomsg
Version:	%{VERSION}
Release:        1%{?dist}
Summary:        nanomsg is a socket library that provides several common communication patterns
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/nanomsg/nanomsg
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
The nanomsg library is a simple high-performance implementation of several "scalability protocols". These scalability protocols are light-weight messaging protocols which can be used to solve a number of very common messaging patterns, such as request/reply, publish/subscribe, surveyor/respondent, and so forth. These protocols can run over a variety of transports such as TCP, UNIX sockets, and even WebSocket.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{version}

%build
%cmake .
make %{?_smp_mflags} 

%check
ctest .

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md
%{_bindir}/nanocat
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/*.pc

%changelog

