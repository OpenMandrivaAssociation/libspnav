%define oname spnav

%define lib_major 0
%define libname %mklibname %{oname}
%define devname %mklibname %{oname} -d
%define oldlibname %mklibname %{oname} 0

Name:		libspnav
Version:	1.1
Release:	2
Summary:	library to access 3D-input-devices
Group:		System/Libraries
License:	BSD
Url:		https://spacenav.sourceforge.net/
Source0:	https://github.com/FreeSpacenav/libspnav/releases/download/v%{version}/libspnav-%{version}.tar.gz
Patch0:		libspnav-1.1-link-lm.patch
Patch1:		libspnav-1.1-version.patch
BuildRequires:	pkgconfig(x11)
Obsoletes:	spnav < 0.2.2-4

%description
The libspnav library is provided as a replacement of the magellan library. It
provides a cleaner, and more orthogonal interface. libspnav supports both the
original X11 protocol for communicating with the driver, and the new
alternative non-X protocol. Programs that choose to use the X11 protocol, are
automatically compatible with either the free spacenavd driver or the official
3dxserv, as if they were using the magellan SDK.

Also, libspnav provides a magellan API wrapper on top of the new API. So, any
applications that were using the magellan library, can switch to libspnav
without any changes. And programmers that are familliar with the magellan API
can continue using it with a free library without the restrictions of the
official SDK.

#--------------------------------------------------------------------

%package -n	%libname
Group:		System/Libraries
Summary:	Library to access 3D-input-devices
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %libname
The libspnav library is provided as a replacement of the magellan library. It
provides a cleaner, and more orthogonal interface. libspnav supports both the
original X11 protocol for communicating with the driver, and the new
alternative non-X protocol. Programs that choose to use the X11 protocol, are
automatically compatible with either the free spacenavd driver or the official
3dxserv, as if they were using the magellan SDK.

Also, libspnav provides a magellan API wrapper on top of the new API. So, any
applications that were using the magellan library, can switch to libspnav
without any changes. And programmers that are familliar with the magellan API
can continue using it with a free library without the restrictions of the
official SDK.

%files -n %libname
%{_libdir}/libspnav.so.%{lib_major}*

#--------------------------------------------------------------------

%package -n %devname
Group:         Development/C
Summary:       Static libraries and headers for %{name}
Requires:      %libname = %{version}-%{release}
Provides:      %{oname}-devel = %{version}-%{release}
Provides:      lib%{oname} = %{version}-%{release}
Obsoletes:     %{_lib}libspnav-devel < 0.2.2-3

%description -n %devname
libspnav - library to access 3D-input-devices.

This package contains static libraries and header files need for development.

%files -n %devname
%{_includedir}/*.h
%{_libdir}/*.so
%{_datadir}/pkgconfig/*.pc

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
sed -i "s/libdir=lib/libdir=%{_lib}/g" configure
%configure
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make

%install
%make_install

chmod 755 %{buildroot}%{_libdir}/*.so.*
chmod 644 %{buildroot}%{_includedir}/*.h

# Remove static library
rm -f %{buildroot}%{_libdir}/%{name}.a

