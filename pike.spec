#
# Conditional build:
%bcond_without	opengl	# don't build GL and GLUT modules
#
# TODO:
# - update DVB (not ready for version 3 API in Linux 2.6.x)
# - PDF.Panda?
%include	/usr/lib/rpm/macros.perl
Summary:	Interpreted, high-level, object oriented language
Summary(pl.UTF-8):	Interpretowalny, obiektowy język wysokiego poziomu
Name:		pike
Version:	7.6.112
Release:	0.1
License:	GPL v2, LGPL v2.1, MPL 1.1
Group:		Development/Languages
#Source0Download: http://pike.ida.liu.se/download/pub/pike/latest-stable/
Source0:	http://pike.ida.liu.se/pub/pike/latest-stable/Pike-v%{version}.tar.gz
# Source0-md5:	3ba03096741d6df839d32a940f4a865c
Source1:	http://pike.ida.liu.se/generated/manual/pike_modref.tar.gz
# Source1-md5:	fbe7595e28d7c220dd6f237efe7b7d68
Source2:	http://pike.ida.liu.se/generated/manual/pike_ref.tar.gz
# Source2-md5:	2ad4c65cd9475f92dfcba0bc13be0923
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-acfix.patch
Patch3:		%{name}-freetype-includes.patch
Patch4:		%{name}-ssl.patch
Patch5:		%{name}-sparc.patch
Patch6:		%{name}-pkgconfig.patch
URL:		http://pike.ida.liu.se/
BuildRequires:	Mird-devel
%{?with_opengl:BuildRequires:	OpenGL-devel}
%{?with_opengl:BuildRequires:	OpenGL-glut-devel}
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	file
BuildRequires:	freetds-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	gdbm-devel
BuildRequires:	glib-devel
BuildRequires:	gmp-devel
BuildRequires:	gtkglarea1-devel
BuildRequires:	gtk+-devel
BuildRequires:	krb5-devel
BuildRequires:	libglade-devel
BuildRequires:	libjpeg-devel
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libtiff-devel
BuildRequires:	mysql-devel >= 3.20
BuildRequires:	nettle-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pdflib-devel
BuildRequires:	perl-base >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel >= 7.2
BuildRequires:	postgresql-backend-devel >= 7.2
BuildRequires:	sane-backends-devel
BuildRequires:	unixODBC-devel
BuildRequires:	xorg-lib-libXext-devel
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

%description -l pl.UTF-8
Pike jest interpretowalnym, modularnym, obiektowo zorientowanym
językiem wysokiego poziomu. Pike ze składnią podobną do C jest prosty
w nauce. Pike raczej ewoluował niż był zaprojektowany. Zmiany w Pike
zostały zapoczątkowane z powodu konkretnych potrzeb użytkowników.

%package GL
Summary:	GL module for Pike
Summary(pl.UTF-8):	Moduł GL dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL

%description GL
This Pike module provides access to OpenGL functions.

%description GL -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do funkcji OpenGL.

%package GLUT
Summary:	GLUT module for Pike
Summary(pl.UTF-8):	Moduł GLUT dla języka Pike
Group:		Libraries
Requires:	%{name}-GL = %{version}-%{release}

%description GLUT
This Pike module provides access to GLUT OpenGL functions.

%description GLUT -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do funkcji OpenGL
biblioteki GLUT.

%package SDL
Summary:	SDL module for Pike
Summary(pl.UTF-8):	Moduł SDL dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description SDL
This Pike module provides access to SDL functions.

%description SDL -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do funkcji biblioteki SDL.

%package ffmpeg
Summary:	Ffmpeg module for Pike
Summary(pl.UTF-8):	Moduł Ffmpeg dla języka pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ffmpeg
This Pike module provides access to ffmpeg libraries functions
(libavcodec, libavformat).

%description ffmpeg -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do funkcji bibliotek ffmpeg
(libavcodec, libavformat).

%package gdbm
Summary:	Gdbm module pike module
Summary(pl.UTF-8):	Moduł obsługi baz danych Gdbm dla języka pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gdbm
This Pike module provides access to GDBM databases.

%description gdbm -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do baz GDBM.

%package gtk
Summary:	GTK+ pike module
Summary(pl.UTF-8):	Moduł GTK+ dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
This Pike module provides access to GTK+ functions.

%description gtk -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do funkcji GTK+.

%package images
Summary:	Image-related modules for Pike
Summary(pl.UTF-8):	Moduły obsługi grafiki dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description images
This module provides many powerful image processing functions to Pike
programs. Handles GIF, JPEG and PNM.

%description images -l pl.UTF-8
Moduł dla języka Pike dostarczający funkcje obróbki grafiki. Obsługuje
GIF, JPEG i PNM.

%package mysql
Summary:	MySQL module for Pike
Summary(pl.UTF-8):	Moduł MySQL dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
This Pike module provides access to MySQL databases.

%description mysql -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do baz danych MySQL.

%package odbc
Summary:	ODBC module for Pike
Summary(pl.UTF-8):	Moduł ODBC dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description odbc
This Pike module provides access to databases through ODBC driver.

%description odbc -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do baz danych poprzez
sterownik ODBC.

%package pdf
Summary:	PDF module for Pike
Summary(pl.UTF-8):	Moduł PDF dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pdf
This Pike module provides PDF processing functions.

%description pdf -l pl.UTF-8
Moduł dla języka Pike udostępniający funkcje obróbki dokumentów PDF.

%package perl
Summary:	Perl module for Pike
Summary(pl.UTF-8):	Moduł Perl dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
This Pike module makes it possible to use Perl code in Pike programs.

%description perl -l pl.UTF-8
Moduł dla języka Pike umożliwiający używanie kodu Perla w programach
napisanych w Pike'u.

%package pg
Summary:	Postgres module for Pike
Summary(pl.UTF-8):	Moduł Postgres dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pg
This Pike module provides access to PostgreSQL databases.

%description pg -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do baz danych PostgreSQL.

%package sane
Summary:	SANE module for Pike
Summary(pl.UTF-8):	Moduł SANE dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sane
This Pike module provides SANE (scanner access) functions.

%description sane -l pl.UTF-8
Moduł dla języka Pike udostępniający funkcje SANE (służące do dostępu
do skanera).

%package ssl
Summary:	Ssleay module for Pike
Summary(pl.UTF-8):	Moduł Ssleay dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ssl
This Pike module provides OpenSSL functions.

%description ssl -l pl.UTF-8
Moduł dla języka Pike udostępniający funkcje biblioteki OpenSSL.

%package sybase
Summary:	Sybase module for Pike
Summary(pl.UTF-8):	Moduł Sybase dla języka Pike
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sybase
This Pike module provides access to Sybase or MS SQL databases.

%description sybase -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do baz danych Sybase i MS
SQL.

%package zlib
Summary:	Gz module for Pike
Summary(pl.UTF-8):	Moduł Gz dla języka Pike
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description zlib
This Pike module provides access to zlib compression functions.

%description zlib -l pl.UTF-8
Moduł dla języka Pike umożliwiający dostęp do funkcji kompresji
biblioteki zlib.

%prep
%setup -q -n Pike-v%{version} -a1 -a2
%patch0 -p1
%patch1 -p1
# not needed?
#%patch2 -p1
%patch3 -p1
%patch4 -p1
# issue fixed (s/\*/+/)? needs check if pike works on sparc now
#%patch5 -p1
%patch6 -p1

%build
# TODO
# fix perl support
cd src
%{__autoconf}
touch stamp-h.in
cd modules
for m in system spider files sybase Msql Mysql Odbc Ssleay _Image_FreeType ; do
	cd $m
	%{__autoconf} -I ../..
	cd ..
done
cd ../post_modules/_Image_SVG
%{__autoconf} -I ../..
cd ../..
# workaround - don't try to rebuild other configures
# (or all Makefile.in files must be patched with s/--localdir/-I/)
touch */configure */*/configure */*/*/configure
CPPFLAGS="-I/usr/include/postgresql/internal -I/usr/include/postgresql/server"
%configure \
	GTK_CONFIG=/usr/bin/gtk-config \
	LIBGLADE_CONFIG=/usr/bin/libglade-config \
	SDL_CONFIG=/usr/bin/sdl-config \
	--with-double-precision \
	--with-freetype \
	--with-gif \
	--with-gmp \
	--with-jpeglib \
	--with-long-double-precision \
	--with-max-fd=1024 \
	--with-mysql \
	--with-pdflib \
	--with-poll \
	--with-postgres \
	--with-postgres-include-dir=%{_includedir}/postgresql \
	--with-sane \
	--with-security \
	--with-sybase \
	--with-ssleay \
	--with-tifflib \
	--with-ttflib \
	--with-x \
	--with-zlib \
	%{?with_opengl:--with-lib-GL} \
	%{!?with_opengl:--without-GL --without-GLUT} \
	--without-perl \
	--without-gnome

%{__make}
# "doc" fails

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} -C src install \
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
%doc ANNOUNCE CHANGES COMMITTERS COPYRIGHT README
# tutorial
%attr(755,root,root) %{_bindir}/*
%{_includedir}/pike

%dir %{_libdir}/pike
%{_libdir}/pike/*.*
%dir %{_libdir}/pike/include
%{_libdir}/pike/include/[!mop]*.h
%{_libdir}/pike/include/p[!o]*.h
%dir %{_libdir}/pike/modules
%{_libdir}/pike/modules/[!_P]*.pmod
%dir %{_libdir}/pike/modules/Parser.pmod
%{_libdir}/pike/modules/Parser.pmod/*.p*
%attr(755,root,root) %{_libdir}/pike/modules/Parser.pmod/_parser.so
%{_libdir}/pike/modules/P[!a]*.pmod
%{_libdir}/pike/modules/_[!I]*.pmod
# R: bzip2-libs
%attr(755,root,root) %{_libdir}/pike/modules/Bz2.so
# dummy
%attr(755,root,root) %{_libdir}/pike/modules/COM.so
%attr(755,root,root) %{_libdir}/pike/modules/CommonLog.so
# currently dummy
%attr(755,root,root) %{_libdir}/pike/modules/DVB.so
%attr(755,root,root) %{_libdir}/pike/modules/Gettext.so
# R: gmp
%attr(755,root,root) %{_libdir}/pike/modules/Gmp.so
%attr(755,root,root) %{_libdir}/pike/modules/HTTPAccept.so
# R: krb5-libs
%attr(755,root,root) %{_libdir}/pike/modules/Kerberos.so
# dummy
%attr(755,root,root) %{_libdir}/pike/modules/Msql.so
# R: nettle
%attr(755,root,root) %{_libdir}/pike/modules/Nettle.so
%attr(755,root,root) %{_libdir}/pike/modules/Pipe.so
%attr(755,root,root) %{_libdir}/pike/modules/Shuffler.so
%attr(755,root,root) %{_libdir}/pike/modules/Unicode.so
%attr(755,root,root) %{_libdir}/pike/modules/_ADT.so
%attr(755,root,root) %{_libdir}/pike/modules/_Roxen.so
%attr(755,root,root) %{_libdir}/pike/modules/___Java.so
%attr(755,root,root) %{_libdir}/pike/modules/___MIME.so
%attr(755,root,root) %{_libdir}/pike/modules/___Math.so
# R: Mird
%attr(755,root,root) %{_libdir}/pike/modules/___Mird.so
%attr(755,root,root) %{_libdir}/pike/modules/___Oracle.so
%attr(755,root,root) %{_libdir}/pike/modules/___Regexp.so
%attr(755,root,root) %{_libdir}/pike/modules/___Yp.so
%attr(755,root,root) %{_libdir}/pike/modules/____Charset.so
%attr(755,root,root) %{_libdir}/pike/modules/____Regexp_PCRE.so
%attr(755,root,root) %{_libdir}/pike/modules/spider.so

%{_mandir}/man1/*

%if %{with opengl}
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
