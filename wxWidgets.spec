#
# Conditional build:
%bcond_without	odbc			# without ODBC support
%bcond_without	gtk			# without wxGTK packages
%bcond_without	gtk2			# without wxGTK2 packages
%bcond_without	x11			# without wxX11 packages
%bcond_without	motif			# without wxMotif packages
%bcond_without	gl			# without *-gl* packages
%bcond_without	unicode			# without *-unicode* packages
%bcond_without	nounicode		# only unicode packages
%bcond_without	univ			# without *-univ* packages
%bcond_without	nouniv			# only univ packages
%bcond_with	debug			# build with \--enable-debug
					# (binary incompatible with non-debug)
#
# TODO:
# - review all bconds
# - use external stc for contrib/src/stc
# - use system iODBC or unixODBC (--with-odbc=sys but this prefer iODBC and if not found uses unixODBC)
# - check ODBC in unicode build
# - separate contrib extensions
# - review all Summary and %%description
# - fix %%_with_debug build (filenames with 'd')
# - mspack BR
# - build demos for X11,unicode,univ (smallest deps)
# misc notes:
# contrib/utils/wxrc build fine with gtk2-nounicode
# contrib/utils/wxrcedit segvfaults on gtk2-nounicode (wxPen::operator==)
# utils/HelpGen build fine on gtk2-nounicode (depend only on base lib)
# utils/configtool does not build (missing source file)
# utils/emulator build and work fine on gtk2-nounicode
# utils/helpview build and work fine on gtk2-nounicode
# utils/hhp2cached build fine on gtk2-nounicode
# utils/tex2rtf build fine on gtk2-nounicode (depend only on base lib)
#   but not in gtk2-unicode 
#   ../../../.././utils/tex2rtf/src/tex2any.cpp:2716:1: converting to execution character set: Invalid or incomplete multibyte or wide character
#   this line contains £ aka POUNDS, probably changing it to octal value fix this issue
Summary:	wxWidgets library
Summary(pl):	Biblioteka wxWidgets
Name:		wxWidgets
Version:	2.5.2
Release:	0.1
License:	wxWidgets Licence
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/wxwindows/wxAll-%{version}.tar.gz
# Source0-md5:	468d900fa4b34e2341879471c7631ed8
Source1:	ftp://biolpc22.york.ac.uk/pub/2.5.2/wxWidgets-2.5.2-Patch01.tar.gz
# Source1-md5:	22f8177c509c058685146b295d9de866
Patch0:		%{name}-samples.patch
URL:		http://www.wxWidgets.org/
%{?with_gl:BuildRequires:	OpenGL-devel}
# FIXME: only for sdl.m4
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bakefile >= 0.1.4
BuildRequires:	bison
BuildRequires:	cppunit-devel
BuildRequires:	esound-devel
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
%{?with_gtk2:BuildRequires:	gtk+2-devel}
%{?with_motif:BuildRequires:	motif-devel}
%{?with_unicode:BuildRequires:	pango-devel}
Obsoletes:	wxwin-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%{_datadir}

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

# detect bcond conflicts (don't move this)
%{!?with_unicode:%{!?with_nounicode:%{error: --without unicode + --without nounicode = NULL} exit 1}}
%{!?with_univ:%{!?with_nouniv:%{error: --without univ + --without nouniv = NULL} exit 1}}
%{!?with_motif:%{!?with_x11:%{!?with_gtk:%{!?with_gtk2:%{error:bconds conflit detected} exit 1}}}}

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%description -l pl
wxWidgets to wolnodostêpna biblioteka napisana w C++ umo¿liwiaj±ca
rozwijanie wieloplatformowych programów GUI. Przy u¿yciu wxWidgets
mo¿na tworzyæ aplikacje dla ró¿nych GUI (GTK+, Motif/LessTif, MS
Windows, Mac) z tego samego kodu ¼ród³owego.

%package afm
Summary:	Font metrics common for wxGTK, wxGTK2, wxMotif i wxX11
Summary(pl):	Metryki fontów wspólne dla wxGTK, wxGTK2, wxMotif i wxX11
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	wxwin-afm

%description afm
Font metrics (in AFM format) common for wxGTK, wxGTK2, wxMotif and
wxX11 libraries.

%description afm -l pl
Metryki fontów (w formacie AFM) wspólne dla bibliotek wxGTK, wxGTK2,
wxMotif i wxX11.

%package devel
Summary:	wxWidgets header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do wxWidgets
Group:		X11/Development/Libraries
Requires:	libstdc++-devel

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

%description examples
wxWidgets example programs.

%description examples -l pl
Przyk³adowe programy wxWidgets.

%package HelpGen
Summary:	Help file generator for wxWidgets programs
Summary(pl):	Generator plików pomocy dla programów wxWidgets
Group:		Development/Tools
Requires:	wxBase = %{version}-%{release}

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

%package -n wxGTK
Summary:	wxGTK library
Summary(pl):	Biblioteka wxGTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxGTK
wxWidgets library using GTK widgets.

%description -n wxGTK -l pl
Biblioteka wxWidgets u¿ywaj±ca widgetów GTK.

%package -n wxGTK-devel
Summary:	Header files for wxGTK library
Summary(pl):	Pliki nag³ówkowe biblioteki wxGTK
Group:		X11/Development/Libraries
Requires:	wxGTK = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description -n wxGTK-devel
Header files for wxWidgets library using GTK widgets.

%description -n wxGTK-devel -l pl
Pliki nag³ówkowe dla biblioteki wxWidgets u¿ywaj±cej widgetów GTK.

%package -n wxGTK-gl
Summary:	GL canvas library for wxGTK
Summary(pl):	Biblioteka GL dla wxGTK
Group:		X11/Libraries
Requires:	wxGTK = %{version}-%{release}
Requires:	OpenGL

%description -n wxGTK-gl
GL canvas library for wxGTK.

%description -n wxGTK-gl -l pl
Biblioteka GL dla wxGTK.

%package -n wxGTK-gl-devel
Summary:	Development files for GL canvas library for wxGTK
Summary(pl):	Pliki programistyczne biblioteki GL dla wxGTK
Group:		X11/Development/Libraries
Requires:	wxGTK-devel = %{version}-%{release}
Requires:	wxGTK-gl = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxGTK-gl-devel
Development files for GL canvas library for wxGTK.

%description -n wxGTK-gl-devel -l pl
Pliki programistyczne biblioteki GL dla wxGTK.

%package -n wxGTK-univ
Summary:	wxUniversal-based wxGTK library
Summary(pl):	Oparta na wxUniversal biblioteka wxGTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxGTK-univ
wxUniversal-based wxWidgets library using GTK widgets.

%description -n wxGTK-univ -l pl
Oparta na wxUniversal biblioteka wxWidgets u¿ywaj±ca widgetów GTK.

%package -n wxGTK-univ-devel
Summary:	Header files for wxUniversal-based wxGTK library
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxGTK
Group:		X11/Development/Libraries
Requires:	wxGTK-univ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description -n wxGTK-univ-devel
Header files for wxUniversal-based wxWidgets library using GTK
widgets.

%description -n wxGTK-univ-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxWidgets
u¿ywaj±cej widgetów GTK.

%package -n wxGTK-univ-gl
Summary:	GL canvas library for wxUniversal-based wxGTK
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxGTK
Group:		X11/Libraries
Requires:	wxGTK-univ = %{version}-%{release}
Requires:	OpenGL

%description -n wxGTK-univ-gl
GL canvas library for wxUniversal-based wxGTK.

%description -n wxGTK-univ-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxGTK.

%package -n wxGTK-univ-gl-devel
Summary:	Development files for GL canvas library for wxUniversal-based wxGTK2
Summary(pl):	Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxGTK2
Group:		X11/Development/Libraries
Requires:	wxGTK-univ-devel = %{version}-%{release}
Requires:	wxGTK-univ-gl = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxGTK-univ-gl-devel
Development files for GL canvas library for wxUniversal-based wxGTK2.

%description -n wxGTK-univ-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxGTK2.

%package -n wxGTK2
Summary:	wxGTK2 library
Summary(pl):	Biblioteka wxGTK2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxGTK2
wxWidgets library using GTK2 widgets.

%description -n wxGTK2 -l pl
Biblioteka wxWidgets u¿ywaj±ca widgetów GTK2.

%package -n wxGTK2-devel
Summary:	Header files for wxGTK2 library
Summary(pl):	Pliki nag³ówkowe biblioteki wxGTK2
Group:		X11/Development/Libraries
Requires:	wxGTK2 = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

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

%description -n wxGTK2-gl-devel
Development files for wxGTK2 GL canvas library.

%description -n wxGTK2-gl-devel -l pl
Pliki programistyczne biblioteki GL dla wxGTK2.

%package -n wxGTK2-unicode
Summary:	wxGTK2 library with UNICODE support
Summary(pl):	Biblioteka wxGTK2 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxGTK2-unicode
wxWidgets library using GTK2 widgets with UNICODE support.

%description -n wxGTK2-unicode -l pl
Biblioteka wxWidgets u¿ywaj±ca widgetów GTK2 z obs³ug± UNICODE.

%package -n wxGTK2-unicode-devel
Summary:	Header files for wxGTK2 library with UNICODE support
Summary(pl):	Pliki nag³ówkowe biblioteki wxGTK2 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	wxGTK2-unicode = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

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

%description -n wxGTK2-unicode-gl-devel
Development files for GL canvas library for wxGTK2 with UNICODE
support.

%description -n wxGTK2-unicode-gl-devel -l pl
Pliki programistyczne biblioteki GL dla wxGTK2 z obs³ug± UNICODE.

%package -n wxGTK2-univ
Summary:	wxUniversal-based wxGTK2 library
Summary(pl):	Oparta na wxUniversal biblioteka wxGTK2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxGTK2-univ
wxUniversal-based wxWidgets library using GTK2 widgets.

%description -n wxGTK2-univ -l pl
Oparta na wxUniversal biblioteka wxWidgets u¿ywaj±ca widgetów GTK2.

%package -n wxGTK2-univ-devel
Summary:	Header files for wxUniversal-based wxGTK2 library
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxGTK2
Group:		X11/Development/Libraries
Requires:	wxGTK2-univ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description -n wxGTK2-univ-devel
Header files for wxUniversal-based wxWidgets library using GTK2
widgets.

%description -n wxGTK2-univ-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxWidgets
u¿ywaj±cej widgetów GTK2.

%package -n wxGTK2-univ-gl
Summary:	GL canvas library for wxUniversal-based wxGTK2
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxGTK2
Group:		X11/Libraries
Requires:	wxGTK2-univ = %{version}-%{release}
Requires:	OpenGL

%description -n wxGTK2-univ-gl
GL canvas library for wxUniversal-based wxGTK2.

%description -n wxGTK2-univ-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxGTK2.

%package -n wxGTK2-univ-gl-devel
Summary:	Development files for GL canvas library for wxUniversal-based wxGTK2
Summary(pl):	Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxGTK2
Summary:	wxGTK
Group:		X11/Development/Libraries
Requires:	wxGTK2-univ-devel = %{version}-%{release}
Requires:	wxGTK2-univ-gl = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxGTK2-univ-gl-devel
Development files for GL canvas library for wxUniversal-based wxGTK2.

%description -n wxGTK2-univ-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxGTK2.

%package -n wxGTK2-univ-unicode
Summary:	wxUniversal-based wxGTK2 library with UNICODE support
Summary(pl):	Oparta na wxUniversal biblioteka wxGTK2 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxGTK2-univ-unicode
wxUniversal-based wxWidgets library using GTK2 widgets with UNICODE
support.

%description -n wxGTK2-univ-unicode -l pl
Oparta na wxUniversal biblioteka wxWidgets u¿ywaj±ca widgetów GTK2 z
obs³ug± UNICODE.

%package -n wxGTK2-univ-unicode-devel
Summary:	Header files for wxUniversal-based wxGTK2 library with UNICODE support
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxGTK2 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	wxGTK2-univ-unicode = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description -n wxGTK2-univ-unicode-devel
Header files for wxUniversal-based wxWidgets library using GTK2
widgets with UNICODE support.

%description -n wxGTK2-univ-unicode-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxWidgets
u¿ywaj±cej widgetów GTK2 z obs³ug± UNICODE.

%package -n wxGTK2-univ-unicode-gl
Summary:	GL canvas library for wxUniversal-based wxGTK2 with UNICODE support
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxGTK2 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	wxGTK2-univ-unicode = %{version}-%{release}
Requires:	OpenGL

%description -n wxGTK2-univ-unicode-gl
GL canvas library for wxUniversal-based wxGTK2 with UNICODE support.

%description -n wxGTK2-univ-unicode-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxGTK2 z obs³ug± UNICODE.

%package -n wxGTK2-univ-unicode-gl-devel
Summary:	Development files for GL canvas library for wxGTK2-univ with UNICODE support
Summary(pl):	Pliki programistyczne biblioteki GL dla wxGTK2-univ z obs³ug± UNICODE
Summary:	wxGTK
Group:		X11/Development/Libraries
Requires:	wxGTK2-univ-unicode-devel = %{version}-%{release}
Requires:	wxGTK2-univ-unicode-gl = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxGTK2-univ-unicode-gl-devel
Development files for GL canvas library for wxUnicode-based wxGTK2
with UNICODE support.

%description -n wxGTK2-univ-unicode-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUnicode wxGTK2 z
obs³ug± UNICODE.

%package -n wxMotif
Summary:	wxWidgets library - Motif port
Summary(pl):	biblioteka wxWidgets - port Motif
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxMotif
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code. This
package contains wxWidgets library using Motif widgets.

%description -n wxMotif -l pl
wxWidgets to darmowa biblioteka napisana w C++ umi¿liwiaj±ca
rozwijanie wielo-platformowych programów GUI. Z wxWidgets mo¿esz
tworzyæ aplikacje dla ró¿nych GUI (GTK+, Motif/LessTif, MS Windows,
Mac) z tego samego kodu ¼ród³owego. Ten pakiet zawiera bibliotekê
wxWidgets u¿ywaj±c± widgetów Motif.

%package -n wxMotif-devel
Summary:	wxMotif header files and development documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do wxMotif
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxMotif = %{version}-%{release}

%description -n wxMotif-devel
Header files and development documentation for the wxMotif library.

%description -n wxMotif-devel -l pl
Pliki nag³ówkowe i dokumentacja do biblioteki wxMotif.

%package -n wxMotif-gl
Summary:	GL canvas library for wxMotif
Summary(pl):	Biblioteka GL dla wxMotif
Group:		X11/Libraries
Requires:	wxMotif = %{version}-%{release}
Requires:	OpenGL

%description -n wxMotif-gl
GL canvas library for wxMotif.

%description -n wxMotif-gl -l pl
Biblioteka GL dla wxMotif.

%package -n wxMotif-gl-devel
Summary:	Development files for GL canvas library for wxMotif
Summary(pl):	Pliki programistyczne biblioteki GL dla wxMotif
Group:		X11/Libraries
Requires:	wxMotif-devel = %{version}-%{release}
Requires:	wxMotif-gl = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxMotif-gl-devel
Development files for GL canvas library for wxMotif.

%description -n wxMotif-gl-devel -l pl
Pliki programistyczne biblioteki GL dla wxMotif.

%package utils
Summary:	Misc utils from wxWidgets project
Summary(pl):	Ró¿ne narzêdzia z projektu wxWidgets
Group:		X11/Development/Tools
Requires:	wxX11-univ = %{version}-%{release}

%description utils
Misc utils from wxWidgets project: helpviewer, makegen, etc.

%description utils -l pl
Ró¿ne narzêdzia z projektu wxWidgets: helpviewer, makegen itp.

%package -n wxX11-univ
Summary:	wxUniversal-based wxX11 library
Summary(pl):	Oparta na wxUniversal biblioteka wxX11
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxX11-univ
wxUniversal-based wxX11 library.

%description -n wxX11-univ -l pl
Oparta na wxUniversal biblioteka wxX11.

%package -n wxX11-univ-devel
Summary:	Header files for wxUniversal-based wxX11 library
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11
Group:		X11/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxX11-univ = %{version}-%{release}

%description -n wxX11-univ-devel
Header files for wxUniversal-based wxX11 library.

%description -n wxX11-univ-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11.

%package -n wxX11-univ-gl
Summary:	GL canvas library for wxUniversal-based wxX11
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxX11
Group:		X11/Libraries
Requires:	wxX11-univ = %{version}-%{release}
Requires:	OpenGL

%description -n wxX11-univ-gl
GL canvas library for wxUniversal-based wxX11.

%description -n wxX11-univ-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxX11.

%package -n wxX11-univ-gl-devel
Summary:	Development files for GL canvas library for wxUniversal-based wxX11
Summary(pl):	Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11
Group:		X11/Development/Libraries
Requires:	wxX11-univ-gl = %{version}-%{release}
Requires:	wxX11-univ-devel = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxX11-univ-gl-devel
Development files for GL canvas library for wxUniversal-based wxX11.

%description -n wxX11-univ-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11.

%package -n wxX11-univ-unicode
Summary:	wxUniversal-based wxX11 library with UNICODE support
Summary(pl):	Oparta na wxUniversal biblioteka wxX11 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-afm = %{version}-%{release}

%description -n wxX11-univ-unicode
wxUniversal-based wxX11 library with UNICODE support.

%description -n wxX11-univ-unicode -l pl
Oparta na wxUniversal biblioteka wxX11 z obs³ug± UNICODE.

%package -n wxX11-univ-unicode-devel
Summary:	Header files for wxUniversal-based wxX11 library with UNICODE support
Summary(pl):	Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11 z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxX11-univ-unicode = %{version}-%{release}

%description -n wxX11-univ-unicode-devel
Header files for wxUniversal-based wxX11 library with UNICODE support.

%description -n wxX11-univ-unicode-devel -l pl
Pliki nag³ówkowe opartej na wxUniversal biblioteki wxX11 z obs³ug± UNICODE.

%package -n wxX11-univ-unicode-gl
Summary:	GL canvas library for wxUniversal-based wxX11 with UNICODE support
Summary(pl):	Biblioteka GL dla opartej na wxUniversal wxX11 z obs³ug± UNICODE
Group:		X11/Libraries
Requires:	wxX11-univ-unicode = %{version}-%{release}
Requires:	OpenGL

%description -n wxX11-univ-unicode-gl
GL canvas library for wxUniversal-based wxX11 with UNICODE support.

%description -n wxX11-univ-unicode-gl -l pl
Biblioteka GL dla opartej na wxUniversal wxX11 z obs³ug± UNICODE.

%package -n wxX11-univ-unicode-gl-devel
Summary:	Development files for GL canvas library for wxX11-univ with UNICODE support
Summary(pl):	Pliki programistyczne biblioteki GL dla wxX11-univ z obs³ug± UNICODE
Group:		X11/Development/Libraries
Requires:	wxX11-univ-unicode-gl = %{version}-%{release}
Requires:	wxX11-univ-unicode-devel = %{version}-%{release}
Requires:	OpenGL-devel

%description -n wxX11-univ-unicode-gl-devel
Development files for GL canvas library for wxUniversal-based wxX11
with UNICODE support.

%description -n wxX11-univ-unicode-gl-devel -l pl
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11 z
obs³ug± UNICODE.

%prep
%setup -q -a 1
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1
#%patch10 -p1
#%patch11 -p1
#%patch12 -p1
#%patch13 -p1
#%patch14 -p1
#%patch15 -p1
#%ifarch amd64
#%patch16 -p1
#%endif
#%patch17 -p1
#%patch18 -p1


%build
cp /usr/share/automake/config.sub .
%{__aclocal} -I .
%{__autoconf}
#cd contrib
#%{__aclocal} -I ..
#%{__autoconf}
#cd ../demos
#%{__aclocal} -I ..
#%{__autoconf}
#cd ../samples
#%{__aclocal} -I ..
#%{__autoconf}
#cd ../utils
#%{__aclocal} -I ..
#%{__autoconf}
#cd ..

CPPFLAGS="-I`pwd`/include -I/usr/X11R6/include"; export CPPFLAGS
# avoid adding -s to LDFLAGS
LDFLAGS=" "; export LDFLAGS
common_args="%{?with_debug:--enable-debug}%{!?with_debug:--disable-debug} \
	--disable-monolithic \
	--enable-plugins \
	--with-zlib=sys \
	--with-regex=sys \
	--disable-compat20 \
	--enable-compat22 \
	--enable-permissive \
	--enable-shared \
	--enable-soname \
	--enable-std_iostreams \
	--enable-timedate \
	--enable-wave"

gui_args="--with-libjpeg=sys \
	--with-libpng=sys \
	--with-libtiff=sys \
	%{?with_gl:--with-opengl} \
	--with-x \
	--enable-calendar \
	--enable-commondlg \
	--enable-controls \
	--enable-fraction \
	--enable-iff \
	--enable-tabdialog"

%if %{with gtk2}
gui='--with-gtk --enable-gtk2'
for unicode in %{?with_nounicode:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	%{?with_unicode:'--enable-unicode'} ; do
	for univ in %{?with_univ:'--enable-universal'} %{?with_nouniv:'--disable-universal'}; do
		objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
		mkdir $objdir
		cd $objdir
		../%configure \
			${common_args} \
			${gui_args} \
			${gui} \
			${univ} \
			${unicode}
		%{__make}
		%{__make} -C contrib/src
		cd ..
	done
done
%endif

%if %{with x11} && %{with univ}
univ='--enable-universal'
gui='--with-x11'
for unicode in %{?with_nounicode:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	%{?with_unicode:'--enable-unicode'} ; do
	objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
	mkdir $objdir
	cd $objdir
	../%configure \
		${common_args} \
		${gui_args} \
		${gui} \
		${univ} \
		${unicode}
	%{__make}
	%{__make} -C contrib/src
	if echo $objdir| grep -q disable-unicode ; then
		%{__make} -C utils
		%{__make} -C utils/emulator
		%{__make} -C contrib/utils
	fi
	cd ..
done
%endif

%if %{with gtk} && %{with nounicode}
unicode='--disable-unicode %{?with_odbc:--with-odbc}'
gui="--with-gtk"
for univ in %{?with_univ:'--enable-universal'} %{?with_nouniv:'--disable-universal'}; do
	# think about wine and nanox
	objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
	mkdir $objdir
	cd $objdir
	../%configure \
		${common_args} \
		${gui_args} \
		${gui} \
		${univ} \
		${unicode}
	%{__make}
	%{__make} -C contrib/src
	cd ..
done
%endif

%if %{with motif} && %{with nounicode} && %{with nouniv}
unicode='--disable-unicode %{?with_odbc:--with-odbc}'
gui='--with-motif'
univ='--disable-universal'
objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
mkdir $objdir
cd $objdir
../%configure \
	${common_args} \
	${gui_args} \
	${gui} \
	${univ} \
	${unicode}
%{__make}
%{__make} -C contrib/src
cd ..
%endif

cd locale
%{__make} allmo
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%if %{with gtk2}
gui='--with-gtk --enable-gtk2'
for unicode in %{?with_nounicode:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	%{?with_unicode:'--enable-unicode'} ; do
	for univ in %{?with_univ:'--enable-universal'} %{?with_nouniv:'--disable-universal'}; do
		objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
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
done
%endif

%if %{with x11} && %{with univ}
univ='--enable-universal'
gui='--with-x11'
for unicode in %{?with_nounicode:'--disable-unicode %{?with_odbc:--with-odbc}'} \
	%{?with_unicode:'--enable-unicode'} ; do
	objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
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
		install utils/dialoged/src/DialogEd $RPM_BUILD_ROOT%{_bindir}
		# TODO: install default config files and default backgrouds
		install utils/emulator/src/emulator $RPM_BUILD_ROOT%{_bindir}
		install utils/tex2rtf/src/tex2rtf $RPM_BUILD_ROOT%{_bindir}
		install utils/hhp2cached/hhp2cached $RPM_BUILD_ROOT%{_bindir}
		install utils/makegen/makegen $RPM_BUILD_ROOT%{_bindir}
		install -d $RPM_BUILD_ROOT%{_datadir}/wx/makegen/templates
		install -m644 utils/makegen/templates/* \
			$RPM_BUILD_ROOT%{_datadir}/wx/makegen/templates
		install contrib/utils/wxrc/wxrc $RPM_BUILD_ROOT%{_bindir}
		install contrib/utils/wxrcedit/wxrcedit $RPM_BUILD_ROOT%{_bindir}
		install -d $RPM_BUILD_ROOT%{_datadir}/wx/wxrcedit
		install contrib/utils/wxrcedit/df/* \
			$RPM_BUILD_ROOT%{_datadir}/wx/wxrcedit/
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

%if %{with gtk} && %{with nounicode}
unicode='--disable-unicode %{?with_odbc:--with-odbc}'
gui="--with-gtk"
for univ in %{?with_univ:'--enable-universal'} %{?with_nouniv:'--disable-universal'}; do
	# think about wine and nanox
	objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
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
%endif

%if %{with motif} && %{with nounicode} && %{with nouniv}
unicode='--disable-unicode %{?with_odbc:--with-odbc}'
gui='--with-motif'
univ='--disable-universal'
objdir=`echo obj${gui}${unicode}${univ}|sed 's/ /_/g'`
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
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for file in todo.txt readme.txt changes.txt ; do
	cp -f docs/gtk/$file docs/wxGTK-$file
done
for file in issues.txt readme.txt todo.txt ; do
	cp -f docs/motif/$file docs/wxMotif-$file
done
cp -f docs/x11/readme.txt docs/wxX11-readme.txt

%find_lang wxstd

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n wxBase -p /sbin/ldconfig
%postun -n wxBase -p /sbin/ldconfig

%post   -n wxBase-unicode -p /sbin/ldconfig
%postun -n wxBase-unicode -p /sbin/ldconfig

%post   -n wxGTK -p /sbin/ldconfig
%postun -n wxGTK -p /sbin/ldconfig

%post   -n wxGTK-gl -p /sbin/ldconfig
%postun -n wxGTK-gl -p /sbin/ldconfig

%post   -n wxGTK-univ -p /sbin/ldconfig
%postun -n wxGTK-univ -p /sbin/ldconfig

%post   -n wxGTK-univ-gl -p /sbin/ldconfig
%postun -n wxGTK-univ-gl -p /sbin/ldconfig

%post   -n wxGTK2 -p /sbin/ldconfig
%postun -n wxGTK2 -p /sbin/ldconfig

%post   -n wxGTK2-gl -p /sbin/ldconfig
%postun -n wxGTK2-gl -p /sbin/ldconfig

%post   -n wxGTK2-univ -p /sbin/ldconfig
%postun -n wxGTK2-univ -p /sbin/ldconfig

%post   -n wxGTK2-univ-gl -p /sbin/ldconfig
%postun -n wxGTK2-univ-gl -p /sbin/ldconfig

%post   -n wxGTK2-unicode -p /sbin/ldconfig
%postun -n wxGTK2-unicode -p /sbin/ldconfig

%post   -n wxGTK2-unicode-gl -p /sbin/ldconfig
%postun -n wxGTK2-unicode-gl -p /sbin/ldconfig

%post   -n wxGTK2-univ-unicode -p /sbin/ldconfig
%postun -n wxGTK2-univ-unicode -p /sbin/ldconfig

%post   -n wxGTK2-univ-unicode-gl -p /sbin/ldconfig
%postun -n wxGTK2-univ-unicode-gl -p /sbin/ldconfig

%post   -n wxMotif -p /sbin/ldconfig
%postun -n wxMotif -p /sbin/ldconfig

%post   -n wxMotif-gl -p /sbin/ldconfig
%postun -n wxMotif-gl -p /sbin/ldconfig

%post   -n wxX11-univ -p /sbin/ldconfig
%postun -n wxX11-univ -p /sbin/ldconfig

%post   -n wxX11-univ-unicode -p /sbin/ldconfig
%postun -n wxX11-univ-unicode -p /sbin/ldconfig

%files -f wxstd.lang
%defattr(644,root,root,755)
%doc docs/{changes,licence,licendoc,preamble,readme,todo}.txt
%doc docs/wxGTK-{todo,readme,changes}.txt
%doc docs/wxMotif-{issues,readme,todo}.txt
%doc docs/wxX11-readme.txt
%dir %{_datadir}/wx
%dir %{_datadir}/wx/2.4

%if %{with x11} || %{with gtk} || %{with gtk2} || %{with motif}
%files -n wxWidgets-afm
%defattr(644,root,root,755)
%{_datadir}/wx/2.4/afm
%{_datadir}/wx/2.4/gs_afm
%endif

%files devel
%defattr(644,root,root,755)
%doc docs/html
%doc docs/pdf/dialoged.pdf docs/tech docs/univ
%{_includedir}/wx
%dir %{_libdir}/wx
%dir %{_libdir}/wx/include
%{_aclocaldir}/*.m4

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with nounicode}
%files HelpGen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/HelpGen

%files -n wxBase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_base-*.so.*.*

%files -n wxBase-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_base-*.so
%{_libdir}/wx/include/base-*
%attr(755,root,root) %{_bindir}/wxbase-*-config
%endif

%if %{with unicode}
%files -n wxBase-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_baseu-*.so.*.*

%files -n wxBase-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_baseu-*.so
%{_libdir}/wx/include/baseu-*
%attr(755,root,root) %{_bindir}/wxbaseu-*-config
%endif

%if %{with gtk} && %{with nouniv} && %{with nounicode}
%files -n wxGTK
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_gtk_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_gtk_gl-*.so.*.*}

%files -n wxGTK-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk-*.so
%{_libdir}/libwx_gtk_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_gtk_gl-*.so}
%{_libdir}/wx/include/gtk-*
%attr(755,root,root) %{_bindir}/wxgtk-*-config
%endif

%if %{with gtk} && %{with nouniv} && %{with nounicode} && %{with gl}
%files -n wxGTK-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk_gl-*.so.*.*

%files -n wxGTK-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk_gl-*.so
%endif

%if %{with gtk} && %{with univ} && %{with nounicode}
%files -n wxGTK-univ
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtkuniv-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_gtkuniv_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_gtkuniv_gl-*.so.*.*}

%files -n wxGTK-univ-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtkuniv-*.so
%{_libdir}/libwx_gtkuniv_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_gtkuniv_gl-*.so}
%{_libdir}/wx/include/gtkuniv-*
%attr(755,root,root) %{_bindir}/wxgtkuniv-*-config
%endif

%if %{with gtk} && %{with univ} && %{with nounicode} && %{with gl}
%files -n wxGTK-univ-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtkuniv_gl-*.so.*.*

%files -n wxGTK-univ-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtkuniv_gl-*.so
%endif

%if %{with gtk2} && %{with nouniv} && %{with nounicode}
%files -n wxGTK2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_gtk2_*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_gtk2_gl-*.so.*.*}

%files -n wxGTK2-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2-*.so
%{_libdir}/libwx_gtk2_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_gtk2_gl-*.so}
%{_libdir}/wx/include/gtk2-*
%attr(755,root,root) %{_bindir}/wxgtk2-*-config
%endif

%if %{with gtk2} && %{with nouniv} && %{with nounicode} && %{with gl}
%files -n wxGTK2-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2_gl-*.so.*.*

%files -n wxGTK2-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2_gl-*.so
%endif

%if %{with gtk2} && %{with nouniv} && %{with unicode}
%files -n wxGTK2-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_gtk2u_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_gtk2u_gl-*.so.*.*}

%files -n wxGTK2-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2u-*.so
%{_libdir}/libwx_gtk2u_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_gtk2u_gl-*.so}
%{_libdir}/wx/include/gtk2u-*
%attr(755,root,root) %{_bindir}/wxgtk2u-*-config
%endif

%if %{with gtk2} && %{with nouniv} && %{with unicode} && %{with gl}
%files -n wxGTK2-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u_gl-*.so.*.*

%files -n wxGTK2-unicode-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2u_gl-*.so
%endif

%if %{with gtk2} && %{with univ} && %{with nounicode}
%files -n wxGTK2-univ
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2univ-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_gtk2univ_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_gtk2univ_gl-*.so.*.*}

%files -n wxGTK2-univ-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2univ-*.so
%{_libdir}/libwx_gtk2univ_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_gtk2univ_gl-*.so}
%{_libdir}/wx/include/gtk2univ-*
%attr(755,root,root) %{_bindir}/wxgtk2univ-*-config
%endif

%if %{with gtk2} && %{with univ} && %{with nounicode} && %{with gl}
%files -n wxGTK2-univ-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2univ_gl-*.so.*.*

%files -n wxGTK2-univ-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2univ_gl-*.so
%endif

%if %{with gtk2} && %{with univ} && %{with unicode}
%files -n wxGTK2-univ-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2univu-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_gtk2univu_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_gtk2univu_gl-*.so.*.*}

%files -n wxGTK2-univ-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2univu-*.so
%{_libdir}/libwx_gtk2univu_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_gtk2univu_gl-*.so}
%{_libdir}/wx/include/gtk2univu-*
%attr(755,root,root) %{_bindir}/wxgtk2univu-*-config
%endif

%if %{with gtk2} && %{with univ} && %{with unicode} && %{with gl}
%files -n wxGTK2-univ-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2univu_gl-*.so.*.*

%files -n wxGTK2-univ-unicode-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_gtk2univu_gl-*.so
%endif

%if %{with motif} && %{with nouniv} && %{with nounicode}
%files -n wxMotif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motif-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_motif_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_motif_gl-*.so.*.*}

%files -n wxMotif-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_motif-*.so
%{_libdir}/libwx_motif_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_motif_gl-*.so}
%{_libdir}/wx/include/motif-*
%attr(755,root,root) %{_bindir}/wxmotif-*-config
%endif

%if %{with motif} && %{with nouniv} && %{with nounicode} && %{with gl}
%files -n wxMotif-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motif_gl-*.so.*.*

%files -n wxMotif-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_motif_gl-*.so
%endif

%if %{with x11} && %{with univ} && %{with nounicode}
%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/HelpGen
%exclude %{_bindir}/wx*-config
%{_datadir}/wx/makegen
%{_datadir}/wx/wxrcedit

%files -n wxX11-univ
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univ-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_x11univ_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_x11univ_gl-*.so.*.*}

%files -n wxX11-univ-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univ-*.so
%{_libdir}/libwx_x11univ_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_x11univ_gl-*.so}
%{_libdir}/wx/include/x11univ-*
%attr(755,root,root) %{_bindir}/wxx11univ-*-config
%endif

%if %{with x11} && %{with univ} && %{with nounicode} && %{with gl}
%files -n wxX11-univ-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univ_gl-*.so.*.*

%files -n wxX11-univ-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univ_gl-*.so
%endif

%if %{with x11} && %{with univ} && %{with unicode}
%files -n wxX11-univ-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu-*.so.*.*
%attr(755,root,root) %{_libdir}/libwx_x11univu_*-*.so.*.*
%{?with_gl:%exclude %{_libdir}/libwx_x11univu_gl-*.so.*.*}

%files -n wxX11-univ-unicode-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univu-*.so
%{_libdir}/libwx_x11univu_*-*.so
%{?with_gl:%exclude %{_libdir}/libwx_x11univu_gl-*.so}
%{_libdir}/wx/include/x11univu-*
%attr(755,root,root) %{_bindir}/wxx11univu-*-config
%endif

%if %{with x11} && %{with univ} && %{with unicode} && %{with gl}
%files -n wxX11-univ-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu_gl-*.so.*.*

%files -n wxX11-univ-unicode-gl-devel
%defattr(644,root,root,755)
%{_libdir}/libwx_x11univu_gl-*.so
%endif
