#
# Conditional build:
%bcond_without	GL	# don't build GL and GLUT modules
#
%include	/usr/lib/rpm/macros.perl
Summary:	Interpreted, high-level, object oriented language
Summary(pl):	Interpretowalny, obiektowy jêzyk wysokiego poziomu
Name:		pike
Version:	7.6.24
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	http://pike.ida.liu.se/pub/pike/latest-stable/Pike-v%{version}.tar.gz
# Source0-md5:	4e39c43a00c6566a9638ef48499bbc82
Source1:	http://pike.ida.liu.se/generated/manual/pike_modref.tar.gz
# Source1-md5:	fbe7595e28d7c220dd6f237efe7b7d68
Source2:	http://pike.ida.liu.se/generated/manual/pike_ref.tar.gz
# Source2-md5:	2ad4c65cd9475f92dfcba0bc13be0923
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-Image-configure.patch
Patch2:		%{name}-nolibs.patch
Patch3:		%{name}-acfix.patch
Patch4:		%{name}-freetype-includes.patch
Patch5:		%{name}-ssl.patch
Patch6:		%{name}-ffmpeg.patch
Patch7:		%{name}-sparc.patch
URL:		http://pike.ida.liu.se/
%{?with_GL:BuildRequires:	OpenGL-devel}
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	file
BuildRequires:	freetds-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	gdbm-devel
BuildRequires:	glib-devel
%{?with_GL:BuildRequires:	glut-devel}
BuildRequires:	gmp-devel
BuildRequires:	gtkglarea1-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	mysql-devel >= 3.20
BuildRequires:	nettle-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pdflib-devel
BuildRequires:	perl-base >= 5.6
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

%package GL
Summary:	GL module for Pike
Summary(pl):	Modu³ GL dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL

%description GL
This Pike module provides access to OpenGL functions.

%description GL -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do funkcji OpenGL.

%package GLUT
Summary:	GLUT module for Pike
Summary(pl):	Modu³ GLUT dla jêzyka Pike
Group:		Libraries
Requires:	%{name}-GL = %{version}-%{release}

%description GLUT
This Pike module provides access to GLUT OpenGL functions.

%description GLUT -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do funkcji OpenGL
biblioteki GLUT.

%package SDL
Summary:	SDL module for Pike
Summary(pl):	Modu³ SDL dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description SDL
This Pike module provides access to SDL functions.

%description SDL -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do funkcji biblioteki SDL.

%package ffmpeg
Summary:	Ffmpeg module for Pike
Summary(pl):	Modu³ Ffmpeg dla jêzyka pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ffmpeg
This Pike module provides access to ffmpeg libraries functions
(libavcodec, libavformat).

%description ffmpeg -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do funkcji bibliotek ffmpeg
(libavcodec, libavformat).

%package gdbm
Summary:	Gdbm module pike module
Summary(pl):	Modu³ obs³ugi baz danych Gdbm dla jêzyka pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gdbm
This Pike module provides access to GDBM databases.

%description gdbm -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do baz GDBM.

%package gtk
Summary:	GTK+ pike module
Summary(pl):	Modu³ GTK+ dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
This Pike module provides access to GTK+ functions.

%description gtk -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do funkcji GTK+.

%package images
Summary:	Image-related modules for Pike
Summary(pl):	Modu³y obs³ugi grafiki dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description images
This module provides many powerful image processing functions to Pike
programs. Handles GIF, JPEG and PNM.

%description images -l pl
Modu³ dla jêzyka Pike dostarczaj±cy funkcje obróbki grafiki. Obs³uguje
GIF, JPEG i PNM.

%package mysql
Summary:	MySQL module for Pike
Summary(pl):	Modu³ MySQL dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
This Pike module provides access to MySQL databases.

%description mysql -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do baz danych MySQL.

%package odbc
Summary:	ODBC module for Pike
Summary(pl):	Modu³ ODBC dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description odbc
This Pike module provides access to databases through ODBC driver.

%description odbc -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do baz danych poprzez
sterownik ODBC.

%package pdf
Summary:	PDF module for Pike
Summary(pl):	Modu³ PDF dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pdf
This Pike module provides PDF processing functions.

%description pdf -l pl
Modu³ dla jêzyka Pike udostêpniaj±cy funkcje obróbki dokumentów PDF.

%package perl
Summary:	Perl module for Pike
Summary(pl):	Modu³ Perl dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
This Pike module makes it possible to use Perl code in Pike programs.

%description perl -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy u¿ywanie kodu Perla w programach
napisanych w Pike'u.

%package pg
Summary:	Postgres module for Pike
Summary(pl):	Modu³ Postgres dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pg
This Pike module provides access to PostgreSQL databases.

%description pg -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do baz danych PostgreSQL.

%package sane
Summary:	SANE module for Pike
Summary(pl):	Modu³ SANE dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sane
This Pike module provides SANE (scanner access) functions.

%description sane -l pl
Modu³ dla jêzyka Pike udostêpniaj±cy funkcje SANE (s³u¿±ce do dostêpu
do skanera).

%package ssl
Summary:	Ssleay module for Pike
Summary(pl):	Modu³ Ssleay dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ssl
This Pike module provides OpenSSL functions.

%description ssl -l pl
Modu³ dla jêzyka Pike udostêpniaj±cy funkcje biblioteki OpenSSL.

%package sybase
Summary:	Sybase module for Pike
Summary(pl):	Modu³ Sybase dla jêzyka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sybase
This Pike module provides access to Sybase or MS SQL databases.

%description sybase -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do baz danych Sybase i MS
SQL.

%package zlib
Summary:	Gz module for Pike
Summary(pl):	Modu³ Gz dla jêzyka Pike
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description zlib
This Pike module provides access to zlib compression functions.

%description zlib -l pl
Modu³ dla jêzyka Pike umo¿liwiaj±cy dostêp do funkcji kompresji
biblioteki zlib.

%prep
%setup -q -n Pike-v%{version} -a1 -a2
%patch0 -p1
# huh?
#%patch1 -p1
%patch2 -p1
# not needed?
#%patch3 -p1
# seems not needed, there is autodetection now
#%patch4 -p1
%patch5 -p1
#obsolete
#%patch6 -p1
# original source is different now than it was before this patch
#%patch7 -p1

%build
# TODO
# fix perl support
cd src
%{__autoconf}
cd modules
for m in system spider files sybase Msql Mysql Odbc Ssleay _Image_FreeType ; do
	cd $m
	%{__autoconf} -I ../..
	cd ..
done
cd ..
# workaround - don't try to rebuild other configures
# (or all Makefile.in files must be patched with s/--localdir/-I/)
touch */configure */*/configure */*/*/configure
LDFLAGS="-L/usr/X11R6/%{_lib} %{rpmldflags}"; export LDFLAGS
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
	%{?with_GL:--with-lib-GL} \
	%{?with_GL:--with-GLUT} \
	--with-sane \
	--without-perl \
	--without-gnome \
	--with-sybase

%{__make} || :
# remake forced by pike?
%{__make} all doc

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
%{_libdir}/pike/include/[!mop]*.h
%{_libdir}/pike/include/m[!y]*.h
%{_libdir}/pike/include/p[!o]*.h
%dir %{_libdir}/pike/modules
%{_libdir}/pike/modules/[!_P]*.pmod
%dir %{_libdir}/pike/modules/Parser.pmod
%{_libdir}/pike/modules/Parser.pmod/*.p*
%attr(755,root,root) %{_libdir}/pike/modules/Parser.pmod/_parser.so
%{_libdir}/pike/modules/P[!a]*.pmod
%{_libdir}/pike/modules/_[!I]*.pmod
%dir %{_libdir}/pike/modules/Crypto
%{_libdir}/pike/modules/Crypto/*.p*
%attr(755,root,root) %{_libdir}/pike/modules/CommonLog.so
%attr(755,root,root) %{_libdir}/pike/modules/DVB.so
%attr(755,root,root) %{_libdir}/pike/modules/Gettext.so
%attr(755,root,root) %{_libdir}/pike/modules/Gmp.so
%attr(755,root,root) %{_libdir}/pike/modules/HTTPLoop.so
%attr(755,root,root) %{_libdir}/pike/modules/Msql.so
%attr(755,root,root) %{_libdir}/pike/modules/Pipe.so
%attr(755,root,root) %{_libdir}/pike/modules/Shuffler.so
%attr(755,root,root) %{_libdir}/pike/modules/Unicode.so
%attr(755,root,root) %{_libdir}/pike/modules/_Crypto.so
%attr(755,root,root) %{_libdir}/pike/modules/_Roxen.so
%attr(755,root,root) %{_libdir}/pike/modules/___Java.so
%attr(755,root,root) %{_libdir}/pike/modules/___MIME.so
%attr(755,root,root) %{_libdir}/pike/modules/___Math.so
%attr(755,root,root) %{_libdir}/pike/modules/___Mird.so
%attr(755,root,root) %{_libdir}/pike/modules/___Oracle.so
%attr(755,root,root) %{_libdir}/pike/modules/___Regexp.so
%attr(755,root,root) %{_libdir}/pike/modules/___Yp.so
%attr(755,root,root) %{_libdir}/pike/modules/____Charset.so
%attr(755,root,root) %{_libdir}/pike/modules/spider.so

%{_mandir}/man1/*

%if %{with GL}
%files GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/GL.so
%{_libdir}/pike/include/opengl.h

%files GLUT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/GLUT.so
%endif

%files SDL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/SDL.so

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Gdbm.so

%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/_Ffmpeg.so

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/___GTK.so

%files images
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Image.so
%attr(755,root,root) %{_libdir}/pike/modules/_Image*.so
%{_libdir}/pike/modules/_Image*.pmod

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Mysql.so
%{_libdir}/pike/include/mysql.h

%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Odbc.so

%files pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/PDF.so

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Perl.so

%files pg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Postgres.so
%{_libdir}/pike/include/postgres.h

%files sane
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/SANE.so

%files ssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/Ssleay.so

%files sybase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/sybase.so

%files zlib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pike/modules/___Gz.so
