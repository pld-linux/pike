%include	/usr/lib/rpm/macros.perl
Summary:	Interpreted, high-level, object oriented language
Summary(pl):	Interpretowalny, obiektowy jêzyk wysokiego poziomu
Name:		pike
Version:	7.4.28
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	ftp://pike.ida.liu.se/pub/pike/latest-stable/Pike-v%{version}.tar.gz
# Source0-md5:	98a7944cea94c7255a24f2cba7d15ec1
Source1:	http://pike.roxen.com/documentation/tutorial.tar.gz
# Source1-md5:	0991ac8e4079cfa374e68c978bae9d59
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-Image-configure.patch
Patch2:		%{name}-nolibs.patch
#Patch3:		%{name}-acfix.patch
URL:		http://pike.ida.liu.se/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	file
BuildRequires:	findutils
BuildRequires:	freetype >= 2.0
BuildRequires:	gdbm-devel
BuildRequires:	glib-devel
BuildRequires:	glut-devel
BuildRequires:	gmp-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	mysql-devel >= 3.20
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pdflib-devel
BuildRequires:	perl >= 5.6
BuildRequires:	postgresql-devel >= 7.2
BuildRequires:	postgresql-backend-devel >= 7.2
BuildRequires:	sane-backends-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
Obsoletes:	pike-gmp
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
jêzykiem wysokiego poziomu. Pike ze sk³adni± podobn± do C jest prosty
w nauce. Pike raczej ewoluowa³ ni¿ by³ zaprojektowany. Zmiany w Pike
zosta³y zapocz±tkowane z powodu konkretnych potrzeb u¿ytkowników.

%package pg
Summary:	Postgres pike module
Summary(pl):	Modu³ Postgres dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description pg
This Pike module provides access to Postgres databases.

%description pg -l pl
Modu³ dla Pike umo¿liwiaj±cy dostêp do baz Postgresa.

%package mysql
Summary:	MySQL pike module
Summary(pl):	Modu³ MySQL dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description mysql
This Pike module provides access to MySQL databases.

%description mysql -l pl
Modu³ dla Pike umo¿liwiaj±cy dostêp do baz MySQL.

%package images
Summary:	Image pike module
Summary(pl):	Modu³ obs³ugi grafiki dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description images
This module provides many powerful image processing functions to Pike
programs. Handles GIF, JPEG and PNM.

%description images -l pl
Modu³ dla Pike dostarczaj±cy funkcje obróbki grafiki. Obs³uguje GIF,
JPEG i PNM.

%package gdbm
Summary:	gdb pike module
Summary(pl):	Modu³ obs³ugi baz gdbm dla pike
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description gdbm
This Pike module provides access to gdbm databases.

%description gdbm -l pl
Modu³ dla Pike umo¿liwiaj±cy dostêp do baz gdbm.

%package zlib
Summary:	zlib pike module
Summary(pl):	Modu³ obs³ugi skompresowanych archiwów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description zlib
This Pike module provides access to zlib compression functions.

%description zlib -l pl
Modu³ dla Pike umo¿liwiaj±cy dostêp do funkcji kompresji biblioteki
zlib.

%package perl
Summary:	Perl pike module
Summary(pl):	Modu³ pike do Perla
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description perl
This Pike module makes it possible to use Perl code in Pike programs.

%description perl -l pl
Modu³ Pike umo¿liwiaj±cy u¿ywanie kodu Perla w programach Pike.

%package GL
Summary:	GL pike module
Summary(pl):	Modu³ pike - GL
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description GL
This Pike module provides access to OpenGL functions.

%description GL -l pl
Modu³ Pike umo¿liwiaj±cy dostêp do funkcji OpenGL.

%package SDL
Summary:	SDL pike module
Summary(pl):	Modu³ pike - SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description SDL
This Pike module provides access to SDL functions.

%description SDL -l pl
Modu³ Pike umo¿liwiaj±cy dostêp do funkcji SDL.

%package gtk
Summary:	gtk pike module
Summary(pl):	Modu³ pike - gtk
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description gtk
This Pike module provides access to GTK+ functions.

%description gtk -l pl
Modu³ Pike umo¿liwiaj±cy dostêp do funkcji GTK+.

%package GLUT
Summary:	GLUT pike module
Summary(pl):	Modu³ pike - GLUT
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description GLUT
This Pike module provides access to GLUT OpenGL functions.

%description GLUT -l pl
Modu³ Pike umo¿liwiaj±cy dostêp do funkcji OpenGL biblioteki GLUT.

%package odbc
Summary:	ODBC pike module
Summary(pl):	Modu³ pike - ODBC
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description odbc
This Pike module provides access to databases through ODBC driver.

%description odbc -l pl
Modu³ Pike umo¿liwiaj±cy dostêp do baz danych poprzez sterownik ODBC.

%package pdf
Summary:	PDF pike module
Summary(pl):	Modu³ pike - PDF
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description pdf
This Pike module provides PDF processing functions.

%description pdf -l pl
Modu³ Pike udostêpniaj±cy funkcje obróbki dokumentów PDF.

%package sane
Summary:	SANE pike module
Summary(pl):	Modu³ pike - SANE
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description sane
This Pike module provides SANE functions.

%description sane -l pl
Ten modu³ Pike udostêpnia funkcje SANE.

%prep
%setup -q -n Pike-v%{version} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

%build
# TODO
# fix ssl support (link with openssl; add ssl subpackage)
# fix perl support
cd src
%{__autoconf}
cd modules
for m in system spider files sybase Msql Mysql Odbc ; do
	cd $m
	%{__autoconf} -I ../..
	cd ..
done
cd ..
# workaround - don't try to rebuild other configures
# (or all Makefile.in files must be patched with s/--localdir/-I/)
touch */configure */*/configure */*/*/configure
LDFLAGS="-L/usr/X11R6/lib %{rpmldflags}"; export LDFLAGS
CPPFLAGS="-I/usr/include/postgresql/internal -I/usr/include/postgresql/server"
%configure \
	--with-double-precision \
	--with-long-double-precision \
	--with-poll \
	--with-max-fd=1024 \
	--with-security \
	--with-gmp \
	--with-zlib \
	--with-pdflib \
	--with-postgres \
	--with-postgres-include-dir=%{_includedir}/postgresql \
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
	`find $RPM_BUILD_ROOT%{_libdir}/pike/modules -type f` \
	`find $RPM_BUILD_ROOT%{_libdir}/pike/7.2/modules -type f` \
	`find $RPM_BUILD_ROOT%{_includedir}/pike -type f` ; do
	if (file $f | grep -q "script"); then
		perl -pi -e 's@#\!.*pike@#\!%{_bindir}/pike@' $f;
	fi
done;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README tutorial
%attr(755,root,root) %{_bindir}/*
%{_includedir}/pike

%dir %{_libdir}/pike
%{_libdir}/pike/*.*
%dir %{_libdir}/pike/include
%{_libdir}/pike/include/[^mp]*.h
%{_libdir}/pike/include/m[^y]*.h
%{_libdir}/pike/include/p[^o]*.h
%dir %{_libdir}/pike/modules
%{_libdir}/pike/modules/[^_]*.pmod
%{_libdir}/pike/modules/_[^I]*.pmod
%dir %{_libdir}/pike/modules/Crypto
%{_libdir}/pike/modules/Crypto/*.p*
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
%attr(755,root,root) %{_libdir}/pike/modules/S[!AD]*.so
%attr(755,root,root) %{_libdir}/pike/modules/s*.so
%attr(755,root,root) %{_libdir}/pike/modules/___Y*.so
%attr(755,root,root) %{_libdir}/pike/modules/Gmp.so
%attr(755,root,root) %{_libdir}/pike/modules/Unicode.so
%attr(755,root,root) %{_libdir}/pike/modules/DVB.so
%attr(755,root,root) %{_libdir}/pike/modules/_Ffmpeg.so
%attr(755,root,root) %{_libdir}/pike/modules/_Roxen.so

%{_mandir}/man1/*

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
%attr(755,root,root) %{_libdir}/pike/modules/*Gz*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Perl.so

%files GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/GL.so

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/SDL.so

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
