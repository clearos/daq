Name: daq
Summary: Data acquisition library
Version: 2.0.2
Release: 2%{?dist}
License: GPLv2
Group: System Environment/Libraries
Source: daq-%{version}.tar.gz
Requires: libpcap >= 1.0
BuildRequires: autoconf, automake, flex, bison, libpcap-devel >= 1.0

%description
Snort 2.9 introduced the DAQ, or Data Acquisition library, for packet I/O.  The
DAQ replaces direct calls to PCAP functions with an abstraction layer that
facilitates operation on a variety of hardware and software interfaces without
requiring changes to Snort.  It is possible to select the DAQ type and mode
when invoking Snort to perform PCAP readback or inline operation, etc.  The
DAQ library may be useful for other packet processing applications and the
modular nature allows you to build new modules for other platforms.

%package devel
Summary: Data acquisition headers
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Devel package for daq.

%package static
Summary: Data acquisition static libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description static
Static libraries for daq.

%prep
%setup -q

%build
%configure \
    --disable-nfq-module \
    --disable-ipfw-module \
    --disable-ipq-module 

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/daq/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libdaq.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libsfbpf.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libdaq_static.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libdaq_static_modules.la

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/daq.h
%{_includedir}/daq_api.h
%{_includedir}/daq_common.h
%{_includedir}/sfbpf_dlt.h
%{_includedir}/sfbpf.h
%{_libdir}/libdaq.a
%{_libdir}/libsfbpf.a

%files static
%defattr(-,root,root,-)
%{_libdir}/libdaq_static.a
%{_libdir}/libdaq_static_modules.a

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{_libdir}/libdaq.so
%{_libdir}/libdaq.so.2
%{_libdir}/libdaq.so.2.0.2
%{_libdir}/libsfbpf.so
%{_libdir}/libsfbpf.so.0
%{_libdir}/libsfbpf.so.0.0.1
%dir %{_libdir}/daq
%{_libdir}/daq/*.so
%{_libdir}/daq/daq_dump.so
%{_libdir}/daq/daq_pcap.so
%{_libdir}/daq/daq_afpacket.so
%{_bindir}/daq-modules-config

%changelog
* Tue Oct 21 2014 ClearFoundation <developer@clearfoundation.com> 2.0.2-1
- Updated to 2.0.2

* Wed Feb 19 2014 ClearFoundation <developer@clearfoundation.com> 2.0.1-2
- Disabled Netfilter Queue support.

* Fri Sep 13 2013 ClearFoundation <developer@clearfoundation.com> 2.0.1-1
- Updated to 2.0.1

* Fri Feb 11 2011 ClearFoundation <developer@clearfoundation.com> 0.5-1.1
- First build
