#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : font-util
Version  : 1.3.1
Release  : 3
URL      : http://xorg.freedesktop.org/releases/individual/font/font-util-1.3.1.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/font/font-util-1.3.1.tar.gz
Summary  : Font utilities dirs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: font-util-bin
Requires: font-util-data
Requires: font-util-doc
BuildRequires : pkgconfig(xorg-macros)

%description
X.Org font package creation/installation utilities
If the --with-fontrootdir option is specified when configuring this
package, it will be recorded in the fontutil pkg-config file to be used
as the default parent directory for font modules built using the fontutil
macros from version 1.1 or later of this package.

%package bin
Summary: bin components for the font-util package.
Group: Binaries
Requires: font-util-data

%description bin
bin components for the font-util package.


%package data
Summary: data components for the font-util package.
Group: Data

%description data
data components for the font-util package.


%package dev
Summary: dev components for the font-util package.
Group: Development
Requires: font-util-bin
Requires: font-util-data

%description dev
dev components for the font-util package.


%package doc
Summary: doc components for the font-util package.
Group: Documentation

%description doc
doc components for the font-util package.


%prep
%setup -q -n font-util-1.3.1

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bdftruncate
/usr/bin/ucs2any

%files data
%defattr(-,root,root,-)
/usr/share/fonts/X11/util/map-ISO8859-1
/usr/share/fonts/X11/util/map-ISO8859-10
/usr/share/fonts/X11/util/map-ISO8859-11
/usr/share/fonts/X11/util/map-ISO8859-13
/usr/share/fonts/X11/util/map-ISO8859-14
/usr/share/fonts/X11/util/map-ISO8859-15
/usr/share/fonts/X11/util/map-ISO8859-16
/usr/share/fonts/X11/util/map-ISO8859-2
/usr/share/fonts/X11/util/map-ISO8859-3
/usr/share/fonts/X11/util/map-ISO8859-4
/usr/share/fonts/X11/util/map-ISO8859-5
/usr/share/fonts/X11/util/map-ISO8859-6
/usr/share/fonts/X11/util/map-ISO8859-7
/usr/share/fonts/X11/util/map-ISO8859-8
/usr/share/fonts/X11/util/map-ISO8859-9
/usr/share/fonts/X11/util/map-JISX0201.1976-0
/usr/share/fonts/X11/util/map-KOI8-R

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
