#
# TODO: link with libnsl only when necessary (Yp.so?),
#       don't link with libbind (if not necessary, which is probably true)
%include	/usr/lib/rpm/macros.perl
Summary:	interpreted, high-level, object oriented language
Summary(pl):	Interpretowalny, obiektowy j�zyk wysokiego poziomu
Name:		pike
Version:	7.2.239
Release:	4
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.roxen.com/pub/pike/latest-stable/%{name}-%{version}.tar.gz
Source1:	http://pike.roxen.com/documentation/tutorial.tar.gz
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-Image-configure.patch
URL:		http://pike.idonex.se/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	bison
BuildRequires:	file
BuildRequires:	findutils
BuildRequires:	freetype >= 2.0
BuildRequires:	gdbm-devel
BuildRequires:	glib-devel
BuildRequires:	glut-devel
BuildRequires:	gmp-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	mysql-devel >= 3.20
BuildRequires:	pdflib-devel
BuildRequires:	perl >= 5.6
BuildRequires:	postgresql-devel >= 7.0
BuildRequires:	sane-backends-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Pike is easily learned, and just as easily used programming language
to develop powerful applications. Pike is designed to be useful and
powerful. As the syntax of Pike is similar to that of C, most
programmers will find it easy to use. As Pike is a high-level,
interpreted and modular object-oriented language, powerful
applications can be rapidly developed. Pike has evolved rather than
been designed. The changes to Pike that have been made have been
guided by its users' needs. In general, the better you get to know
Pike, the more you will appreciate it, from a users perspective.

%description -l pl
Pike jest interpretowalnym, modularnym, obiektowo zorientowanym
j�zykiem wysokiego poziomu. Pike ze sk�adni� podobn� do C jest prosty
w nauce. Pike raczej ewoluowa� ni� by� zaprojektowany. Zmiany w Pike
zosta�y zapocz�tkowane z powodu konkretnych potrzeb u�ytkownik�w.

%package pg
Summary:	Postgres pike module
Summary(pl):	Modu� Postgres dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description pg
This Pike module provides access to Postgres databases.

%description pg -l pl
Modu� dla Pike umo�liwiaj�cy dost�p do baz Postgresa.

%package mysql
Summary:	MySQL pike module
Summary(pl):	Modu� MySQL dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description mysql
This Pike module provides access to MySQL databases.

%description mysql -l pl
Modu� dla Pike umo�liwiaj�cy dost�p do baz MySQL.

%package images
Summary:	Image pike module
Summary(pl):	Modu� obs�ugi grafiki dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description images
This module provides many powerful image processing functions to Pike
programs. Handles GIF, JPEG and PNM.

%description images -l pl
Modu� dla Pike dostarczaj�cy funkcje obr�bki grafiki. Obs�uguje GIF,
JPEG i PNM.

%package gdbm
Summary:	gdb pike module
Summary(pl):	Modu� obs�ugi baz gdbm dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description gdbm
This Pike module provides access to gdbm databases.

%description gdbm -l pl
Modu� dla Pike umo�liwiaj�cy dost�p do baz gdbm.

%package zlib
Summary:	zlib pike module
Summary(pl):	Modu� obs�ugi skompresowanych archiw�w
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description zlib
This Pike module provides access to zlib compression functions.

%description zlib -l pl
Modu� dla Pike umo�liwiaj�cy dost�p do funkcji kompresji biblioteki
zlib.

%package gmp
Summary:	gmp pike module
Summary(pl):	Modu� pike - gmp
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description gmp
This Pike module provides access to gmp functions.

%description gmp -l pl
Modu� Pike umo�liwiaj�cy dost�p do funkcji biblioteki gmp.

%package perl
Summary:	perl pike module
Summary(pl):	Modu� pike - perl
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description perl
This Pike module makes it possible to use Perl code in Pike programs.

%description perl -l pl
Modu� Pike umo�liwiaj�cy u�ywanie kodu Perla w programach Pike.

%package GL
Summary:	GL pike module
Summary(pl):	Modu� pike - GL
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description GL
This Pike module provides access to OpenGL functions.

%description GL -l pl
Modu� Pike umo�liwiaj�cy dost�p do funkcji OpenGL.

%package gtk
Summary:	gtk pike module
Summary(pl):	Modu� pike - gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description gtk
This Pike module provides access to GTK+ functions.

%description gtk -l pl
Modu� Pike umo�liwiaj�cy dost�p do funkcji GTK+.

%package GLUT
Summary:	GLUT pike module
Summary(pl):	Modu� pike - GLUT
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description GLUT
This Pike module provides access to GLUT OpenGL functions.

%description GLUT -l pl
Modu� Pike umo�liwiaj�cy dost�p do funkcji OpenGL biblioteki GLUT.

%package odbc
Summary:	ODBC pike module
Summary(pl):	Modu� pike - ODBC
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description odbc
This Pike module provides access to databases through ODBC driver.

%description odbc -l pl
Modu� Pike umo�liwiaj�cy dost�p do baz danych poprzez sterownik ODBC.

%package pdf
Summary:	PDF pike module
Summary(pl):	Modu� pike - PDF
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description pdf
This Pike module provides PDF processing functions.

%description pdf -l pl
Modu� Pike udost�pniaj�cy funkcje obr�bki dokument�w PDF.

%package sane
Summary:	SANE pike module
Summary(pl):	Modu� pike - SANE
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description sane
This Pike module provides SANE functions.

%description sane -l pl
Ten modu� Pike udost�pnia funkcje SANE.

%prep
%setup -q -n Pike-v%{version} -a1
%patch0 -p1
%patch1 -p1

%build
# TODO
# fix ssl support (link with openssl; add ssl subpackage)
# fix perl support
cd src
LDFLAGS="-L/usr/X11R6/lib %{rpmldflags}"; export LDFLAGS
%configure2_13 \
	--with-double-precision \
	--with-long-double-precision \
	--with-poll \
	--with-max-fd=1024 \
	--with-security \
	--with-gmp \
	--with-zlib \
	--with-pdflib \
	--with-postgres \
	--with-postgres-include-dir=%{_includedir}/pgsql \
	--with-mysql \
	--with-ssleay \
	--with-freetype \
	--with-gif \
	--with-jpeglib \
	--with-tifflib \
	--with-ttflib \
	--with-x \
	--with-lib-GL \
	--with-GLUT \
	--with-sane \
	--without-perl \
	--without-gnome \
	--without-sybase

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
cd src

%{__make} install \
	buildroot=$RPM_BUILD_ROOT

rm -f `find $RPM_BUILD_ROOT -regex '.*\.o' -type f | xargs`

for f in `find $RPM_BUILD_ROOT%{_bindir} -type f` \
	`find $RPM_BUILD_ROOT%{_libdir}/pike/modules -type f`; do
	if (file $f | grep -q "script"); then
		perl -pi -e 's@#\!.*pike@#\!%{_bindir}/pike@' $f;
	fi
done;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README src/{BUGS,Change*} tutorial
%attr(755,root,root) %{_bindir}/*
%{_includedir}/pike

%dir %{_libdir}/pike
%{_libdir}/pike/*.*
%dir %{_libdir}/pike/include
%{_libdir}/pike/include/[^mp]*.h
%{_libdir}/pike/include/m[^y]*.h
%{_libdir}/pike/include/p[^o]*.h
%{_libdir}/pike/tools
%dir %{_libdir}/pike/modules
%{_libdir}/pike/modules/[^_]*.pmod
%{_libdir}/pike/modules/_[^I]*.pmod
%attr(755,root,root) %{_libdir}/pike/modules/C*.so
%attr(755,root,root) %{_libdir}/pike/modules/*_C*.so
%attr(755,root,root) %{_libdir}/pike/modules/Gettext*.so
%attr(755,root,root) %{_libdir}/pike/modules/H*.so
%attr(755,root,root) %{_libdir}/pike/modules/___J*.so
%attr(755,root,root) %{_libdir}/pike/modules/___M*.so
%attr(755,root,root) %{_libdir}/pike/modules/Msql*.so
%attr(755,root,root) %{_libdir}/pike/modules/___O*.so
%attr(755,root,root) %{_libdir}/pike/modules/P[ir]*.so
%attr(755,root,root) %{_libdir}/pike/modules/___R*.so
%attr(755,root,root) %{_libdir}/pike/modules/S[^A]*.so
%attr(755,root,root) %{_libdir}/pike/modules/s*.so
%attr(755,root,root) %{_libdir}/pike/modules/___Y*.so

%files pg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Postgres.so
%{_libdir}/pike/include/postgres.h

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Mysql.so
%{_libdir}/pike/include/mysql.h

%files images
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/*Image*

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Gdbm.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Gz.so

%files gmp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Gmp.so

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Perl.so

%files GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/GL.so

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/*GTK.so

%files GLUT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/GLUT.so

%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Odbc.so

%files pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/PDF.so

%files sane
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/SANE.so
