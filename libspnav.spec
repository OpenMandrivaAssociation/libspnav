%define oname spnav

%define lib_major 0
%define develname %mklibname -d %{oname}
%define lib_name %mklibname %{oname} %{lib_major}

Name:		libspnav
Version:	0.2.3
Release:	2
Summary:	library to access 3D-input-devices
Group:		System/Libraries
License:	BSD
Url:		http://spacenav.sourceforge.net/
Source0:	http://download.sourceforge.net/spacenav/%{name}-%{version}.tar.gz
Patch0:		libspnav-0.2.3-lib_links.patch
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

%package -n	%lib_name
Group:		System/Libraries
Summary:	Library to access 3D-input-devices
Obsoletes:	%{_lib}libspnav0 < 0.2.2-3

%description -n %lib_name
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

%files -n %lib_name
%{_libdir}/libspnav.so.%{lib_major}*

#--------------------------------------------------------------------

%package -n %develname
Group:         Development/C
Summary:       Static libraries and headers for %{name}
Requires:      %lib_name = %{version}-%{release}
Provides:      %{oname}-devel = %{version}-%{release}
Provides:      lib%{oname} = %{version}-%{release}
Obsoletes:     %{_lib}libspnav-devel < 0.2.2-3

%description -n %develname
libspnav - library to access 3D-input-devices.

This package contains static libraries and header files need for development.

%files -n %develname
%{_includedir}/*.h
%{_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
sed -i "s/libdir=lib/libdir=%{_lib}/g" configure
%configure --disable-static
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make

%install
%makeinstall_std

chmod 755 %{buildroot}%{_libdir}/*.so.*
chmod 644 %{buildroot}%{_includedir}/*.h

# Remove static library
rm -f %{buildroot}%{_libdir}/%{name}.a
