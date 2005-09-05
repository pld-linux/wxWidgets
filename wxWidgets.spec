#
# Conditional build:
%bcond_without	ansi			# only unicode packages
%bcond_without	odbc			# without ODBC support
%bcond_without	x11			# don't build wxX11 packages
%bcond_with	debug			# build with \--enable-debug
					# (binary incompatible with non-debug)

Summary:	wxWidgets library
Summary(pl):	Biblioteka wxWidgets
Name:		wxWidgets
Version:	2.6.1
Release:	2
License:	wxWidgets Licence (LGPL with exception)
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/wxwindows/%{name}-%{version}.tar.bz2
# Source0-md5:	045f0edad0988620a4aa36096bb16e28
Patch0:		%{name}-samples.patch
Patch1:		%{name}-ogl.patch
Patch2:		%{name}-ac.patch
Patch3:		%{name}-gif0delay.patch
Patch4:		%{name}-pangox.patch
URL:		http://www.wxWidgets.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	bakefile >= 0.1.8
BuildRequires:	cppunit-devel
BuildRequires:	esound-devel
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
# these are not supported by wxWidgets
Obsoletes:	LDAPExplorerTool <= 0.6-1
Obsoletes:	abridge <= 0.4.0-1
# and these are replaced
Obsoletes:	wxGTK
Obsoletes:	wxGTK-devel
Obsoletes:	wxGTK-gl
Obsoletes:	wxGTK-gl-devel
Obsoletes:	wxGTK-univ
Obsoletes:	wxGTK-univ-devel
Obsoletes:	wxGTK-univ-gl
Obsoletes:	wxGTK-univ-gl-devel
Obsoletes:	wxGTK2-univ
Obsoletes:	wxGTK2-univ-devel
Obsoletes:	wxGTK2-univ-gl
Obsoletes:	wxGTK2-univ-gl-devel
Obsoletes:	wxGTK2-univ-unicode
Obsoletes:	wxGTK2-univ-unicode-devel
Obsoletes:	wxGTK2-univ-unicode-gl
Obsoletes:	wxGTK2-univ-unicode-gl-devel
Obsoletes:	wxMotif
Obsoletes:	wxMotif-devel
Obsoletes:	wxMotif-gl
Obsoletes:	wxMotif-gl-devel
Obsoletes:	wxWidgets-afm
Obsoletes:	wxWindows
Obsoletes:	wxWindows-afm
Obsoletes:	wxwin-afm
Obsoletes:	wxwin-common
Conflicts:	wxGTK2 < 2.6.0
Conflicts:	wxGTK2-unicode < 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%{_datadir}

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%description -l pl
wxWidgets to wolnodostêpna biblioteka napisana w C++ umo¿liwiaj±ca
rozwijanie wieloplatformowych programów GUI. Przy u¿yciu wxWidgets
mo¿na tworzyæ aplikacje dla ró¿nych GUI (GTK+, Motif/LessTif, MS
Windows, Mac) z tego samego kodu ¼ród³owego.

%package devel
Summary:	wxWidgets header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do wxWidgets
Group:		X11/Development/Libraries
Requires:	libstdc++-devel
Obsoletes:	wxWindows-devel

%description devel
Header files and development documentation for the wxWidgets
libraries.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek wxWidgets.

%package examples
Summary:	wxWidgets example programs
Summary(pl):	Przyk³adowe programy wxWidgets
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	wxWindows-examples

%description examples
wxWidgets example programs.

%description examples -l pl
Przyk³adowe programy wxWidgets.

%package HelpGen
Summary:	Help file generator for wxWidgets programs
Summary(pl):	Generator plików pomocy dla programów wxWidgets
Group:		Development/Tools
Requires:	wxBase = %{version}-%{release}
Obsoletes:	wxWindows-HelpGen

%description HelpGen
Help file generator for wxWidgets programs.

%description HelpGen -l pl
Generator plików pomocy dla programów wxWidgets.

%package -n wxBase
Summary:	wxBase library - non-GUI support classes of wxWidgets toolkit
Summary(pl):	wxBase - biblioteka klas wxWidgets nie zwi±zanych z GUI
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n wxBase
wxBase is a collection of C++ classes providing basic data structures
(strings, lists, arrays), powerful wxDateTime class for date
manipulations, portable wrappers around many OS-specific functions
allowing to build the same program under all supported folders,
wxThread class for writing multithreaded programs using either Win32
or POSIX threads and much more. wxBase currently supports the
following platforms: Win32, generic Unix (Linux, FreeBSD, Solaris,
HP-UX, ...) and BeOS.

%description -n wxBase -l pl
wxBase jest zestawem klas C++ obs³uguj±cych podstawowe struktury
danych (stringi, listy, tablice), klasê wxDateTime do operacji na
datach, przeno¶ne wrappery do wielu funkcji zale¿nych od systemu
operacyjnego pozwalaj±ce na zbudowanie tego samego programu w ró¿nych
¶rodowiskach, klasê wxThread do pisania programów wielow±tkowych
u¿ywaj±cych w±tków Win32 albo POSIX i inne. wxBase obs³uguje
platformy: Win32, Unix i BeOS.

%package -n wxBase-devel
Summary:	wxBase headers needed for developping with wxBase
Summary(pl):	Pliki nag³ówkowe do wxBase
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase = %{version}-%{release}

%description -n wxBase-devel
Header files for wxBase. You need them to develop programs using
wxBase.

%description -n wxBase-devel -l pl
Pliki nag³ówkowe do biblioteki wxBase.

%package -n wxBase-unicode
Summary:	wxBase library - non-GUI support classes of wxWidgets toolkit with UNICODE support
Summary(pl):	wxBase - biblioteka klas wxWidgets nie zwi±zanych z GUI ze wsparciem dla UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n wxBase-unicode
wxBase is a collection of C++ classes providing basic data structures
(strings, lists, arrays), powerful wxDateTime class for date
manipulations, portable wrappers around many OS-specific functions
allowing to build the same program under all supported folders,
wxThread class for writing multithreaded programs using either Win32
or POSIX threads and much more. wxBase currently supports the
following platforms: Win32, generic Unix (Linux, FreeBSD, Solaris,
HP-UX, ...) and BeOS. This version is build with UNICODE support.

%description -n wxBase-unicode -l pl
wxBase jest zestawem klas C++ obs³uguj±cych podstawowe struktury
danych (stringi, listy, tablice), klasê wxDateTime do operacji na
datach, przeno¶ne wrappery do wielu funkcji zale¿nych od systemu
operacyjnego pozwalaj±ce na zbudowanie tego samego programu w ró¿nych
¶rodowiskach, klasê wxThread do pisania programów wielow±tkowych
u¿ywaj±cych w±tków Win32 albo POSIX i inne. wxBase obs³uguje
platformy: Win32, Unix i BeOS. Ta wersja jest zbudowana z obs³ug±
UNICODE.

%package -n wxBase-unicode-devel
Summary:	wxBase headers needed for developping with UNICODE-enabled wxBase
Summary(pl):	Pliki nag³ówkowe do wxBase z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-unicode = %{version}-%{release}

%description -n wxBase-unicode-devel
Header files for wxBase. You need them to develop programs using
UNICODE-enabled wxBase.

%description -n wxBase-unicode-devel -l pl
Pliki nag³ówkowe do biblioteki wxBase z obs³ug± UNICODE.

%package -n wxGTK2
Summary:	wxGTK2 library
Summary(pl):	Biblioteka wxGTK2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	wxGTK2-univ

%description -n wxGTK2
wxWidgets library using GTK2 widgets.

%description -n wxGTK2 -l pl
Biblioteka wxWidgets u¿ywaj±ca widgetów GTK2.

%package -n wxGTK2-devel
Summary:	Header files for wxGTK2 library
Summary(pl):	Pliki nag³ówkowe biblioteki wxGTK2
Group:		X11/Development/Libraries
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxGTK2 = %{version}-%{release}
Obsoletes:	wxGTK2-univ-devel

%description -n wxGTK2-devel
Header files for wxWidgets library using GTK2 widgets.

%description -n wxGTK2-devel -l pl
Pliki nag³ówkowe dla biblioteki wxWidgets u¿ywaj±cej widgetów GTK2.

%package -n wxGTK2-gl
Summary:	GL canvas library for wxGTK2
Summary(pl):	Biblioteka GL dla wxGTK2
Group:		X11/Libraries
Requires:	wxGTK2 = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	wxGTK2-univ-gl

%description -n wxGTK2-gl
wxGTK2 GL canvas library.

%description -n wxGTK2-gl -l pl
Biblioteka GL dla wxGTK2.

%package -n wxGTK2-gl-devel
Summary:	Development files for GL canvas library for wxGTK2
Summary(pl):	Pliki programistyczne biblioteki GL dla wxGTK2
Group:		X11/Development/Libraries
Requires:	wxGTK2-devel = %{version}-%{release}
Requires:	wxGTK2-gl = %{version}-%{release}
Requires:	OpenGL-devel
Obsoletes:	wxGTK2-univ-gl-devel

%description -n wxGTK2-gl-devel
Development files for wxGTK2 GL canvas library.

%description -n wxGTK2-gl-devel -l pl
Pliki programistyczne biblioteki GL dla wxGTK2.

%package -n wxGTK2-unicode
Summary:	wxGTK2 library with UNICODE support
Summary(pl):	Biblioteka wxGTK2 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	wxGTK2-univ-unicode

%description -n wxGTK2-unicode
wxWidgets library using GTK2 widgets with UNICODE support.

%description -n wxGTK2-unicode -l pl
Biblioteka wxWidgets u¿ywaj±ca widgetów GTK2 z obs³ug± UNICODE.

%package -n wxGTK2-unicode-devel
Summary:	Header files for wxGTK2 library with UNICODE support
Summary(pl):	Pliki nag³ówkowe biblioteki wxGTK2 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxGTK2-unicode = %{version}-%{release}
Obsoletes:	wxGTK2-univ-unicode-devel

%description -n wxGTK2-unicode-devel
Header files for wxWidgets library using GTK2 widgets with UNICODE
support.

%description -n wxGTK2-unicode-devel -l pl
Pliki nag³ówkowe biblioteki wxWidgets u¿ywaj±cej widgetów GTK2 z
obs³ug± UNICODE.

%package -n wxGTK2-unicode-gl
Summary:	GL canvas library for wxGTK2 with UNICODE support
Summary(pl):	Biblioteka GL dla wxGTK2 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	wxGTK2-unicode = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	wxGTK2-univ-unicode-gl

%description -n wxGTK2-unicode-gl
GL canvas library for wxGTK2 with UNICODE support.

%description -n wxGTK2-unicode-gl -l pl
Biblioteka GL dla wxGTK2 z obs³ug± UNICODE.

%package -n wxGTK2-unicode-gl-devel
Summary:	Development files for GL canvas library for wxGTK2 with UNICODE support
Summary(pl):	Pliki programistyczne biblioteki GL dla wxGTK2 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	wxGTK2-unicode-devel = %{version}-%{release}
Requires:	wxGTK2-unicode-gl = %{version}-%{release}
Requires:	OpenGL-devel
Obsoletes:	wxGTK2-univ-unicode-gl-devel

%description -n wxGTK2-unicode-gl-devel
Development files for GL canvas library for wxGTK2 with UNICODE
support.

%description -n wxGTK2-unicode-gl-devel -l pl
Pliki programistyczne biblioteki GL dla wxGTK2 z obs³ug± UNICODE.

%package utils
Summary:	Misc utils from wxWidgets project
Summary(pl):	Ró¿ne narzêdzia z projektu wxWidgets
Group:		X11/Development/Tools
Requires:	wxX11 = %{version}-%{release}
Obsoletes:	wxWindows-utils

%description utils
Misc utils from wxWidgets project: helpviewer, makegen, etc.

%description utils -l pl
Ró¿ne narzêdzia z projektu wxWidgets: helpviewer, makegen itp.

%package -n wxX11
Summary:	wxUniversal-based wxX11 library
Summary(pl):	Oparta na wxUniversal biblioteka wxX11
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	wxX11-univ

%description -n wxX11
wxUniversal-based wxX11 library.

%description -n wxX11 -l pl
Oparta na wxUniversal biblioteka wxX11.

%package -n wxX11-devel
Summary:	Header files for wxUniversal-based wxX11 library
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxX11 = %{version}-%{release}
Obsoletes:	wxX11-univ-devel

%description -n wxX11-devel
Header files for wxUniversal-based wxX11 library.

%description -n wxX11-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11.

%package -n wxX11-gl
Summary:	GL canvas library for wxUniversal-based wxX11
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxX11
Group:		X11/Libraries
Requires:	wxX11 = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	wxX11-univ-gl

%description -n wxX11-gl
GL canvas library for wxUniversal-based wxX11.

%description -n wxX11-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxX11.

%package -n wxX11-gl-devel
Summary:	Development files for GL canvas library for wxUniversal-based wxX11
Summary(pl):	Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11
Group:		X11/Development/Libraries
Requires:	wxX11-gl = %{version}-%{release}
Requires:	wxX11-devel = %{version}-%{release}
Requires:	OpenGL-devel
Obsoletes:	wxX11-univ-gl-devel

%description -n wxX11-gl-devel
Development files for GL canvas library for wxUniversal-based wxX11.

%description -n wxX11-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11.

%package -n wxX11-unicode
Summary:	wxUniversal-based wxX11 library with UNICODE support
Summary(pl):	Oparta na wxUniversal biblioteka wxX11 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	wxX11-univ-unicode

%description -n wxX11-unicode
wxUniversal-based wxX11 library with UNICODE support.

%description -n wxX11-unicode -l pl
Oparta na wxUniversal biblioteka wxX11 z obs³ug± UNICODE.

%package -n wxX11-unicode-devel
Summary:	Header files for wxUniversal-based wxX11 library with UNICODE support
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxX11-unicode = %{version}-%{release}
Obsoletes:	wxX11-univ-unicode-devel

%description -n wxX11-unicode-devel
Header files for wxUniversal-based wxX11 library with UNICODE support.

%description -n wxX11-unicode-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11 z obs³ug± UNICODE.

%package -n wxX11-unicode-gl
Summary:	GL canvas library for wxUniversal-based wxX11 with UNICODE support
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxX11 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	wxX11-unicode = %{version}-%{release}
Requires:	OpenGL
Obsoletes:	wxX11-univ-unicode-gl

%description -n wxX11-unicode-gl
GL canvas library for wxUniversal-based wxX11 with UNICODE support.

%description -n wxX11-unicode-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxX11 z obs³ug± UNICODE.

%package -n wxX11-unicode-gl-devel
Summary:	Development files for GL canvas library for wxX11 with UNICODE support
Summary(pl):	Pliki programistyczne biblioteki GL dla wxX11 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	wxX11-unicode-gl = %{version}-%{release}
Requires:	wxX11-unicode-devel = %{version}-%{release}
Requires:	OpenGL-devel
Obsoletes:	wxX11-univ-unicode-gl-devel

%description -n wxX11-unicode-gl-devel
Development files for GL canvas library for wxUniversal-based wxX11
with UNICODE support.

%description -n wxX11-unicode-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11 z
obs³ug± UNICODE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

echo 'AC_DEFUN([AM_PATH_GTK],[:])' > fake-am_path_gtk.m4

# bakefile.m4 from 0.1.8
tail -n +1518 aclocal.m4 | head -n 1397 > bakefile.m4
# AC_BAKEFILE_PROG_* macros
tail -n +721 aclocal.m4 | head -n 142 >> bakefile.m4

%build
# if bakefiles rebuild is needed:
#%if "%(rpm -q bakefile --qf '%%{VERSION}')" != "0.1.8"
#cd build/bakefiles
#bakefile_gen -f autoconf
#cd ../..
#%endif
cp -f /usr/share/automake/config.sub .
%{__aclocal} -I .
%{__autoconf}

CPPFLAGS="%{rpmcflags} -I`pwd`/include -I/usr/X11R6/include"; export CPPFLAGS
# avoid adding -s to LDFLAGS
LDFLAGS=" "; export LDFLAGS
args="%{?with_debug:--enable-debug}%{!?with_debug:--disable-debug} \
	--enable-plugins \
	--enable-std_iostreams \
	--without-sdl \
	--with-opengl \
	--enable-calendar \
	--enable-controls \
	--enable-tabdialog"

gui='--with-gtk'
for unicode in %{?with_ansi:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	'--enable-unicode' ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	mkdir $objdir
	cd $objdir
	../%configure \
		${args} \
		${gui} \
		--disable-universal \
		${unicode}
	%{__make}
	%{__make} -C contrib/src
	cd ..
done

%if %{with x11}
gui='--with-x11'
for unicode in %{?with_ansi:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	'--enable-unicode' ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	mkdir $objdir
	cd $objdir
	../%configure \
		${args} \
		${gui} \
		--enable-universal \
		${unicode}
	%{__make}
	%{__make} -C contrib/src
	if echo $objdir| grep -q disable-unicode ; then
		%{__make} -C utils
		%{__make} -C utils/emulator
		%{__make} -C utils/hhp2cached
		%{__make} -C contrib/utils
	fi
	cd ..
done
%endif

cd locale
%{__make} allmo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

gui='--with-gtk'
for unicode in %{?with_ansi:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	'--enable-unicode' ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	cd $objdir
	%{__make} install \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		datadir=$RPM_BUILD_ROOT%{_datadir} \
		libdir=$RPM_BUILD_ROOT%{_libdir} \
		mandir=$RPM_BUILD_ROOT%{_mandir} \
		includedir=$RPM_BUILD_ROOT%{_includedir}

	%{__make} -C contrib/src install \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		datadir=$RPM_BUILD_ROOT%{_datadir} \
		libdir=$RPM_BUILD_ROOT%{_libdir} \
		mandir=$RPM_BUILD_ROOT%{_mandir} \
		includedir=$RPM_BUILD_ROOT%{_includedir}
	cd ..
done

%if %{with x11}
gui='--with-x11'
for unicode in %{?with_ansi:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	'--enable-unicode' ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	cd $objdir
	%{__make} install \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		datadir=$RPM_BUILD_ROOT%{_datadir} \
		libdir=$RPM_BUILD_ROOT%{_libdir} \
		mandir=$RPM_BUILD_ROOT%{_mandir} \
		includedir=$RPM_BUILD_ROOT%{_includedir}
	if echo $objdir| grep -q disable-unicode ; then
#		install utils/dialoged/src/DialogEd $RPM_BUILD_ROOT%{_bindir}
		# TODO: install default config files and default backgrouds
		install utils/HelpGen/src/HelpGen $RPM_BUILD_ROOT%{_bindir}
		install utils/emulator/src/wxemulator $RPM_BUILD_ROOT%{_bindir}
		install utils/tex2rtf/src/tex2rtf $RPM_BUILD_ROOT%{_bindir}
		install utils/hhp2cached/hhp2cached $RPM_BUILD_ROOT%{_bindir}
#		install utils/makegen/makegen $RPM_BUILD_ROOT%{_bindir}
		install utils/wxrc/wxrc $RPM_BUILD_ROOT%{_bindir}
#		install -d $RPM_BUILD_ROOT%{_datadir}/wx/makegen/templates
#		install -m644 utils/makegen/templates/* \
#			$RPM_BUILD_ROOT%{_datadir}/wx/makegen/templates
#		install contrib/utils/wxrcedit/wxrcedit $RPM_BUILD_ROOT%{_bindir}
#		install -d $RPM_BUILD_ROOT%{_datadir}/wx/wxrcedit
#		install contrib/utils/wxrcedit/df/* \
#			$RPM_BUILD_ROOT%{_datadir}/wx/wxrcedit/
	fi

	%{__make} -C contrib/src install \
		prefix=$RPM_BUILD_ROOT%{_prefix} \
		exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
		bindir=$RPM_BUILD_ROOT%{_bindir} \
		datadir=$RPM_BUILD_ROOT%{_datadir} \
		libdir=$RPM_BUILD_ROOT%{_libdir} \
		mandir=$RPM_BUILD_ROOT%{_mandir} \
		includedir=$RPM_BUILD_ROOT%{_includedir}

	cd ..
done
%endif

set -x

for i in $RPM_BUILD_ROOT%{_libdir}/wx/config/*
do
	b=`basename $i`
	cp $i $RPM_BUILD_ROOT%{_bindir}/wx-`echo $b|sed -e 's/\(.*\)-release-.*/\1/'`-config
done

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -f docs/x11/readme.txt docs/wxX11-readme.txt

%find_lang wxstd

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n wxBase -p /sbin/ldconfig
%postun -n wxBase -p /sbin/ldconfig

%post	-n wxBase-unicode -p /sbin/ldconfig
%postun -n wxBase-unicode -p /sbin/ldconfig

%post	-n wxGTK2 -p /sbin/ldconfig
%postun -n wxGTK2 -p /sbin/ldconfig

%post	-n wxGTK2-gl -p /sbin/ldconfig
%postun -n wxGTK2-gl -p /sbin/ldconfig

%post	-n wxGTK2-unicode -p /sbin/ldconfig
%postun -n wxGTK2-unicode -p /sbin/ldconfig

%post	-n wxGTK2-unicode-gl -p /sbin/ldconfig
%postun -n wxGTK2-unicode-gl -p /sbin/ldconfig

%post	-n wxX11 -p /sbin/ldconfig
%postun -n wxX11 -p /sbin/ldconfig

%post	-n wxX11-unicode -p /sbin/ldconfig
%postun -n wxX11-unicode -p /sbin/ldconfig

%define _libf %{?with_debug:d}
%define _configf %{?with_debug:-debug-2.6}


%files -f wxstd.lang
%defattr(644,root,root,755)
%doc docs/{changes,licence,licendoc,preamble,readme,todo}.txt

%files devel
%defattr(644,root,root,755)
%doc docs/html
%doc docs/tech docs/univ
%{_includedir}/wx*
%dir %{_libdir}/wx
%dir %{_libdir}/wx/include
%dir %{_libdir}/wx/config
%{_aclocaldir}/*.m4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with x11}
%files HelpGen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/HelpGen
%endif

%if %{with ansi}
%files -n wxBase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_base%{_libf}-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_base%{_libf}_*.so.*.*
#%attr(755,root,root) %{_libdir}/wx/%{version}/sound_sdl-*.so

%files -n wxBase-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_base%{_libf}-*.so
%{_libdir}/libwx_base%{_libf}_*.so
%endif

%files -n wxBase-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_baseu%{_libf}-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_baseu%{_libf}_*.so.*.*
#%attr(755,root,root) %{_libdir}/wx/%{version}/sound_sdlu-*.so

%files -n wxBase-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_baseu%{_libf}-*.so
%{_libdir}/libwx_baseu%{_libf}_*.so

%if %{with ansi}
%files -n wxGTK2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2%{_libf}_*.so.*.*
%exclude %{_libdir}/libwx_gtk2%{_libf}_ogl-*.so.*.*

%files -n wxGTK2-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2%{_libf}_*-*.so
%exclude %{_libdir}/libwx_gtk2%{_libf}_ogl-*.so
%{_libdir}/wx/config/gtk2-ansi-*
%{_libdir}/wx/include/gtk2-ansi-*
%attr(755,root,root) %{_bindir}/wx-gtk2-ansi%{_configf}-config

%files -n wxGTK2-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2%{_libf}_ogl-*.so.*.*

%files -n wxGTK2-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2%{_libf}_ogl-*.so
%endif

%files -n wxGTK2-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{_libf}_*-*.so.*.*
%exclude %{_libdir}/libwx_gtk2u%{_libf}_ogl-*.so.*.*

%files -n wxGTK2-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2u%{_libf}_*-*.so
%exclude %{_libdir}/libwx_gtk2u%{_libf}_ogl-*.so
%{_libdir}/wx/config/gtk2-unicode-*
%{_libdir}/wx/include/gtk2-unicode-*
%attr(755,root,root) %{_bindir}/wx-gtk2-unicode%{_configf}-config

%files -n wxGTK2-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{_libf}_ogl-*.so.*.*

%files -n wxGTK2-unicode-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2u%{_libf}_ogl-*.so

%if %{with x11}
%if %{with ansi}
%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/HelpGen
%exclude %{_bindir}/wx*-config

%files -n wxX11
%defattr(644,root,root,755)
%doc docs/wxX11-readme.txt
%attr(755,root,root) %{_libdir}/libwx_x11univ%{_libf}_*-*.so.*.*
%exclude %{_libdir}/libwx_x11univ%{_libf}_ogl-*.so.*.*

%files -n wxX11-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univ%{_libf}_*-*.so
%exclude %{_libdir}/libwx_x11univ%{_libf}_ogl-*.so
%{_libdir}/wx/config/x11univ-ansi-*
%{_libdir}/wx/include/x11univ-ansi-*
%attr(755,root,root) %{_bindir}/wx-x11univ-ansi%{_configf}-config

%files -n wxX11-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univ%{_libf}_ogl-*.so.*.*

%files -n wxX11-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univ%{_libf}_ogl-*.so
%endif

%files -n wxX11-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu%{_libf}_*-*.so.*.*
%exclude %{_libdir}/libwx_x11univu%{_libf}_ogl-*.so.*.*

%files -n wxX11-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univu%{_libf}_*-*.so
%exclude %{_libdir}/libwx_x11univu%{_libf}_ogl-*.so
%{_libdir}/wx/config/x11univ-unicode-*
%{_libdir}/wx/include/x11univ-unicode-*
%attr(755,root,root) %{_bindir}/wx-x11univ-unicode%{_configf}-config

%files -n wxX11-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu%{_libf}_ogl-*.so.*.*

%files -n wxX11-unicode-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univu%{_libf}_ogl-*.so
%endif
