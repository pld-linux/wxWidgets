#
# Conditional build:
%bcond_with	ansi		# non-unicode packages
%bcond_without	unicode		# unicode packages
%bcond_with	directfb	# wxDFB packages
%bcond_with	gtk2		# wxGTK2 packages
%bcond_without	gtk3		# wxGTK3 packages
%bcond_with	motif		# wxMotif packages
%bcond_without	qt		# qxQT packages
%bcond_without	x11		# wxX11 packages
%bcond_without	sdl		# SDL sound support
%bcond_with	debug		# debug version of libraries (binary incompatible with non-debug)
#
Summary:	wxWidgets library
Summary(pl.UTF-8):	Biblioteka wxWidgets
Name:		wxWidgets
%define	majver	3.2
Version:	3.2.6
Release:	3
License:	wxWindows Library Licence 3.1 (LGPL v2+ with exception)
Group:		X11/Libraries
#Source0Download: https://github.com/wxWidgets/wxWidgets/releases
Source0:	https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	41d54fffc953936bb92ae45d81ded60c
Patch0:		%{name}-samples.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-gifdelay.patch
Patch3:		relax-abicheck.patch
URL:		https://www.wxWidgets.org/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.23}
%{?with_gtk3:BuildRequires:	EGL-devel >= 1.5}
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5.2.1
BuildRequires:	Qt5Gui-devel >= 5.2.1
BuildRequires:	Qt5OpenGL-devel >= 5.2.1
BuildRequires:	Qt5Test-devel >= 5.2.1
BuildRequires:	Qt5Widgets-devel >= 5.2.1
%endif
%{?with_sdl:BuildRequires:	SDL2-devel >= 2.0.0}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
# for m4 files
BuildRequires:	bakefile >= 0.2.12
BuildRequires:	cairo-devel
BuildRequires:	cppunit-devel >= 1.8.0
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	gettext-tools
BuildRequires:	gspell-devel
BuildRequires:	gstreamer-devel >= 1.7.2.1
BuildRequires:	gstreamer-plugins-bad-devel >= 1.7.2.1
BuildRequires:	gstreamer-plugins-base-devel >= 1.7.2.1
%{?with_gtk2:BuildRequires:	gtk+2-devel >= 2:2.20}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0}
%{?with_gtk2:BuildRequires:	gtk-webkit-devel >= 1.3.1}
%{?with_gtk3:BuildRequires:	gtk-webkit4.1-devel}
BuildRequires:	jbigkit-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmspack-devel
BuildRequires:	libnotify-devel >= 0.7
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libsecret-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool
%{?with_motif:BuildRequires:	motif-devel}
%{?with_x11:BuildRequires:	pango-devel}
BuildRequires:	pcre2-32-devel
%{?with_ansi:BuildRequires:	pcre2-8-devel}
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	rpm-build >= 4.6
%{?with_gtk3:BuildRequires:	wayland-egl-devel}
%if %{with x11}
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
%endif
%if %{with gtk2} || %{with gtk3}
BuildRequires:	xorg-lib-libxkbcommon-devel
%endif
BuildRequires:	xz-devel
BuildRequires:	zlib-devel >= 1.1.4
# these are not supported by wxWidgets
Obsoletes:	LDAPExplorerTool <= 0.6-1
Obsoletes:	abridge <= 0.4.0-1
# and these are replaced
Obsoletes:	wxGTK < 2.5.3
Obsoletes:	wxGTK-devel < 2.5.3
Obsoletes:	wxGTK-gl < 2.5.3
Obsoletes:	wxGTK-gl-devel < 2.5.3
Obsoletes:	wxGTK-univ < 2.5.3
Obsoletes:	wxGTK-univ-devel < 2.5.3
Obsoletes:	wxGTK-univ-gl < 2.5.3
Obsoletes:	wxGTK-univ-gl-devel < 2.5.3
Obsoletes:	wxGTK2-univ < 2.5.3
Obsoletes:	wxGTK2-univ-devel < 2.5.3
Obsoletes:	wxGTK2-univ-gl < 2.5.3
Obsoletes:	wxGTK2-univ-gl-devel < 2.5.3
Obsoletes:	wxGTK2-univ-unicode < 2.5.3
Obsoletes:	wxGTK2-univ-unicode-devel < 2.5.3
Obsoletes:	wxGTK2-univ-unicode-gl < 2.5.3
Obsoletes:	wxGTK2-univ-unicode-gl-devel < 2.5.3
%if %{without motif}
Obsoletes:	wxMotif < %{version}-%{release}
Obsoletes:	wxMotif-devel < %{version}-%{release}
Obsoletes:	wxMotif-gl < %{version}-%{release}
Obsoletes:	wxMotif-gl-devel < %{version}-%{release}
%endif
Obsoletes:	wxWidgets-HelpGen < 3
Obsoletes:	wxWidgets-afm < 2.6
Obsoletes:	wxWindows < 2.5
Obsoletes:	wxWindows-HelpGen < 2.5
Obsoletes:	wxWindows-afm < 2.5
Obsoletes:	wxwin-afm < 2.5
Obsoletes:	wxwin-common < 2.5
Conflicts:	wxGTK2 < 2.6.0
Conflicts:	wxGTK2-unicode < 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	%{_datadir}
%define		_noautoreqdep	libGL.so.1 libGLU.so.1

# do not check for unresolved symbols (couldn't fix that)
%define		no_install_post_check_so	1

%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%description -l pl.UTF-8
wxWidgets to wolnodostępna biblioteka napisana w C++ umożliwiająca
rozwijanie wieloplatformowych programów GUI. Przy użyciu wxWidgets
można tworzyć aplikacje dla różnych GUI (GTK+, Motif/LessTif, MS
Windows, Mac) z tego samego kodu źródłowego.

%package devel
Summary:	wxWidgets header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do wxWidgets
Group:		X11/Development/Libraries
Requires:	libstdc++-devel
Obsoletes:	wxWindows-devel < 2.5

%description devel
Header files and development documentation for the wxWidgets
libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek wxWidgets.

%package -n bakefile-wxWidgets
Summary:	Files for Bakefile to generate wxWidgets project files
Summary(pl.UTF-8):	Pliki dla Bakefile generujące pliki projektów wxWidgets
Group:		Development/Tools
Requires:	bakefile

%description -n bakefile-wxWidgets
Additional files for Bakefile to generate wxWidgets project files.

%description -n bakefile-wxWidgets -l pl.UTF-8
Dodatkowe pliki dla programu Bakefile umożliwiające wygenerowanie
projektów opartych na bibliotece wxWidgets.

%package examples
Summary:	wxWidgets example programs
Summary(pl.UTF-8):	Przykładowe programy wxWidgets
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	wxWindows-examples < 2.5
BuildArch:	noarch

%description examples
wxWidgets example programs.

%description examples -l pl.UTF-8
Przykładowe programy wxWidgets.

%package -n wxBase
Summary:	wxBase library - non-GUI support classes of wxWidgets toolkit
Summary(pl.UTF-8):	wxBase - biblioteka klas wxWidgets nie związanych z GUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib >= 1.1.4

%description -n wxBase
wxBase is a collection of C++ classes providing basic data structures
(strings, lists, arrays), powerful wxDateTime class for date
manipulations, portable wrappers around many OS-specific functions
allowing to build the same program under all supported folders,
wxThread class for writing multithreaded programs using either Win32
or POSIX threads and much more. wxBase currently supports the
following platforms: Win32, generic Unix (Linux, FreeBSD, Solaris,
HP-UX, ...) and BeOS.

%description -n wxBase -l pl.UTF-8
wxBase jest zestawem klas C++ obsługujących podstawowe struktury
danych (stringi, listy, tablice), klasę wxDateTime do operacji na
datach, przenośne wrappery do wielu funkcji zależnych od systemu
operacyjnego pozwalające na zbudowanie tego samego programu w różnych
środowiskach, klasę wxThread do pisania programów wielowątkowych
używających wątków Win32 albo POSIX i inne. wxBase obsługuje
platformy: Win32, Unix i BeOS.

%package -n wxBase-devel
Summary:	wxBase headers needed for developping with wxBase
Summary(pl.UTF-8):	Pliki nagłówkowe do wxBase
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase = %{version}-%{release}

%description -n wxBase-devel
Header files for wxBase. You need them to develop programs using
wxBase.

%description -n wxBase-devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki wxBase.

%package -n wxBase-unicode
Summary:	wxBase library - non-GUI support classes of wxWidgets toolkit with UNICODE support
Summary(pl.UTF-8):	wxBase - biblioteka klas wxWidgets nie związanych z GUI ze wsparciem dla UNICODE
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib >= 1.1.4

%description -n wxBase-unicode
wxBase is a collection of C++ classes providing basic data structures
(strings, lists, arrays), powerful wxDateTime class for date
manipulations, portable wrappers around many OS-specific functions
allowing to build the same program under all supported folders,
wxThread class for writing multithreaded programs using either Win32
or POSIX threads and much more. wxBase currently supports the
following platforms: Win32, generic Unix (Linux, FreeBSD, Solaris,
HP-UX, ...) and BeOS. This version is build with UNICODE support.

%description -n wxBase-unicode -l pl.UTF-8
wxBase jest zestawem klas C++ obsługujących podstawowe struktury
danych (stringi, listy, tablice), klasę wxDateTime do operacji na
datach, przenośne wrappery do wielu funkcji zależnych od systemu
operacyjnego pozwalające na zbudowanie tego samego programu w różnych
środowiskach, klasę wxThread do pisania programów wielowątkowych
używających wątków Win32 albo POSIX i inne. wxBase obsługuje
platformy: Win32, Unix i BeOS. Ta wersja jest zbudowana z obsługą
UNICODE.

%package -n wxBase-unicode-devel
Summary:	wxBase headers needed for developping with UNICODE-enabled wxBase
Summary(pl.UTF-8):	Pliki nagłówkowe do wxBase z obsługą UNICODE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-unicode = %{version}-%{release}

%description -n wxBase-unicode-devel
Header files for wxBase. You need them to develop programs using
UNICODE-enabled wxBase.

%description -n wxBase-unicode-devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki wxBase z obsługą UNICODE.

%package -n wxDFB
Summary:	wxUniversal-based wxDFB library
Summary(pl.UTF-8):	Oparta na wxUniversal biblioteka wxDFB
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB >= 0.9.23
Requires:	wxBase = %{version}-%{release}

%description -n wxDFB
wxUniversal-based wxDFB library.

%description -n wxDFB -l pl.UTF-8
Oparta na wxUniversal biblioteka wxDFB.

%package -n wxDFB-devel
Summary:	Header files for wxUniversal-based wxDFB library
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na wxUniversal biblioteki wxDFB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxDFB = %{version}-%{release}

%description -n wxDFB-devel
Header files for wxUniversal-based wxDFB library.

%description -n wxDFB-devel -l pl.UTF-8
Pliki nagłówkowe opartej na wxUniversal biblioteki wxDFB.

%package -n wxDFB-unicode
Summary:	wxUniversal-based wxDFB library with UNICODE support
Summary(pl.UTF-8):	Oparta na wxUniversal biblioteka wxDFB z obsługą UNICODE
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB >= 0.9.23
Requires:	wxBase-unicode = %{version}-%{release}

%description -n wxDFB-unicode
wxUniversal-based wxDFB library with UNICODE support.

%description -n wxDFB-unicode -l pl.UTF-8
Oparta na wxUniversal biblioteka wxDFB z obsługą UNICODE.

%package -n wxDFB-unicode-devel
Summary:	Header files for wxUniversal-based wxDFB library with UNICODE support
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na wxUniversal biblioteki wxDFB z obsługą UNICODE
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxDFB-unicode = %{version}-%{release}

%description -n wxDFB-unicode-devel
Header files for wxUniversal-based wxDFB library with UNICODE support.

%description -n wxDFB-unicode-devel -l pl.UTF-8
Pliki nagłówkowe opartej na wxUniversal biblioteki wxDFB z obsługą
UNICODE.

%package -n wxGTK2
Summary:	wxGTK2 library
Summary(pl.UTF-8):	Biblioteka wxGTK2
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.10
Requires:	gtk-webkit >= 1.3.1
Requires:	wxBase = %{version}-%{release}
Obsoletes:	wxGTK2-univ < 2.5.3

%description -n wxGTK2
wxWidgets library using GTK2 widgets.

%description -n wxGTK2 -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów GTK2.

%package -n wxGTK2-devel
Summary:	Header files for wxGTK2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxGTK2
Group:		X11/Development/Libraries
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxGTK2 = %{version}-%{release}
Obsoletes:	wxGTK2-univ-devel < 2.5.3

%description -n wxGTK2-devel
Header files for wxWidgets library using GTK2 widgets.

%description -n wxGTK2-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki wxWidgets używającej widgetów GTK2.

%package -n wxGTK2-gl
Summary:	GL canvas library for wxGTK2
Summary(pl.UTF-8):	Biblioteka GL dla wxGTK2
Group:		X11/Libraries
Requires:	wxGTK2 = %{version}-%{release}
Obsoletes:	wxGTK2-univ-gl < 2.5.3

%description -n wxGTK2-gl
wxGTK2 GL canvas library.

%description -n wxGTK2-gl -l pl.UTF-8
Biblioteka GL dla wxGTK2.

%package -n wxGTK2-gl-devel
Summary:	Development files for GL canvas library for wxGTK2
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxGTK2
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxGTK2-devel = %{version}-%{release}
Requires:	wxGTK2-gl = %{version}-%{release}
Obsoletes:	wxGTK2-univ-gl-devel < 2.5.3

%description -n wxGTK2-gl-devel
Development files for wxGTK2 GL canvas library.

%description -n wxGTK2-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxGTK2.

%package -n wxGTK2-unicode
Summary:	wxGTK2 library with UNICODE support
Summary(pl.UTF-8):	Biblioteka wxGTK2 z obsługą UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.10
Requires:	gtk-webkit >= 1.3.1
Requires:	wxBase-unicode = %{version}-%{release}
Obsoletes:	wxGTK2-univ-unicode < 2.5.3

%description -n wxGTK2-unicode
wxWidgets library using GTK2 widgets with UNICODE support.

%description -n wxGTK2-unicode -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów GTK2 z obsługą UNICODE.

%package -n wxGTK2-unicode-devel
Summary:	Header files for wxGTK2 library with UNICODE support
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxGTK2 z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxGTK2-unicode = %{version}-%{release}
Obsoletes:	wxGTK2-univ-unicode-devel < 2.5.3

%description -n wxGTK2-unicode-devel
Header files for wxWidgets library using GTK2 widgets with UNICODE
support.

%description -n wxGTK2-unicode-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxWidgets używającej widgetów GTK2 z
obsługą UNICODE.

%package -n wxGTK2-unicode-gl
Summary:	GL canvas library for wxGTK2 with UNICODE support
Summary(pl.UTF-8):	Biblioteka GL dla wxGTK2 z obsługą UNICODE
Group:		X11/Libraries
Requires:	wxGTK2-unicode = %{version}-%{release}
Obsoletes:	wxGTK2-univ-unicode-gl < 2.5.3

%description -n wxGTK2-unicode-gl
GL canvas library for wxGTK2 with UNICODE support.

%description -n wxGTK2-unicode-gl -l pl.UTF-8
Biblioteka GL dla wxGTK2 z obsługą UNICODE.

%package -n wxGTK2-unicode-gl-devel
Summary:	Development files for GL canvas library for wxGTK2 with UNICODE support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxGTK2 z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxGTK2-unicode-devel = %{version}-%{release}
Requires:	wxGTK2-unicode-gl = %{version}-%{release}
Obsoletes:	wxGTK2-univ-unicode-gl-devel < 2.5.3

%description -n wxGTK2-unicode-gl-devel
Development files for GL canvas library for wxGTK2 with UNICODE
support.

%description -n wxGTK2-unicode-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxGTK2 z obsługą UNICODE.

%package -n wxGTK3
Summary:	wxGTK3 library
Summary(pl.UTF-8):	Biblioteka wxGTK3
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxBase = %{version}-%{release}

%description -n wxGTK3
wxWidgets library using GTK3 widgets.

%description -n wxGTK3 -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów GTK3.

%package -n wxGTK3-devel
Summary:	Header files for wxGTK3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxGTK3
Group:		X11/Development/Libraries
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxGTK3 = %{version}-%{release}

%description -n wxGTK3-devel
Header files for wxWidgets library using GTK3 widgets.

%description -n wxGTK3-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki wxWidgets używającej widgetów GTK3.

%package -n wxGTK3-gl
Summary:	GL canvas library for wxGTK3
Summary(pl.UTF-8):	Biblioteka GL dla wxGTK3
Group:		X11/Libraries
Requires:	wxGTK3 = %{version}-%{release}

%description -n wxGTK3-gl
wxGTK3 GL canvas library.

%description -n wxGTK3-gl -l pl.UTF-8
Biblioteka GL dla wxGTK3.

%package -n wxGTK3-gl-devel
Summary:	Development files for GL canvas library for wxGTK3
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxGTK3
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxGTK3-devel = %{version}-%{release}
Requires:	wxGTK3-gl = %{version}-%{release}

%description -n wxGTK3-gl-devel
Development files for wxGTK3 GL canvas library.

%description -n wxGTK3-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxGTK3.

%package -n wxGTK3-unicode
Summary:	wxGTK3 library with UNICODE support
Summary(pl.UTF-8):	Biblioteka wxGTK3 z obsługą UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxBase-unicode = %{version}-%{release}

%description -n wxGTK3-unicode
wxWidgets library using GTK3 widgets with UNICODE support.

%description -n wxGTK3-unicode -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów GTK3 z obsługą UNICODE.

%package -n wxGTK3-unicode-devel
Summary:	Header files for wxGTK3 library with UNICODE support
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxGTK3 z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxGTK3-unicode = %{version}-%{release}

%description -n wxGTK3-unicode-devel
Header files for wxWidgets library using GTK3 widgets with UNICODE
support.

%description -n wxGTK3-unicode-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxWidgets używającej widgetów GTK3 z
obsługą UNICODE.

%package -n wxGTK3-unicode-gl
Summary:	GL canvas library for wxGTK3 with UNICODE support
Summary(pl.UTF-8):	Biblioteka GL dla wxGTK3 z obsługą UNICODE
Group:		X11/Libraries
Requires:	wxGTK3-unicode = %{version}-%{release}

%description -n wxGTK3-unicode-gl
GL canvas library for wxGTK3 with UNICODE support.

%description -n wxGTK3-unicode-gl -l pl.UTF-8
Biblioteka GL dla wxGTK3 z obsługą UNICODE.

%package -n wxGTK3-unicode-gl-devel
Summary:	Development files for GL canvas library for wxGTK3 with UNICODE support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxGTK3 z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxGTK3-unicode-devel = %{version}-%{release}
Requires:	wxGTK3-unicode-gl = %{version}-%{release}

%description -n wxGTK3-unicode-gl-devel
Development files for GL canvas library for wxGTK3 with UNICODE
support.

%description -n wxGTK3-unicode-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxGTK3 z obsługą UNICODE.

%package -n wxMotif
Summary:	wxMotif library
Summary(pl.UTF-8):	Biblioteka wxMotif
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxBase = %{version}-%{release}

%description -n wxMotif
wxWidgets library using Motif widgets.

%description -n wxMotif -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów Motif.

%package -n wxMotif-devel
Summary:	Header files for wxMotif library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxMotif
Group:		X11/Development/Libraries
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxMotif = %{version}-%{release}

%description -n wxMotif-devel
Header files for wxWidgets library using Motif widgets.

%description -n wxMotif-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki wxWidgets używającej widgetów Motif.

%package -n wxMotif-gl
Summary:	GL canvas library for wxMotif
Summary(pl.UTF-8):	Biblioteka GL dla wxMotif
Group:		X11/Libraries
Requires:	wxMotif = %{version}-%{release}

%description -n wxMotif-gl
wxMotif GL canvas library.

%description -n wxMotif-gl -l pl.UTF-8
Biblioteka GL dla wxMotif.

%package -n wxMotif-gl-devel
Summary:	Development files for GL canvas library for wxMotif
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxMotif
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxMotif-devel = %{version}-%{release}
Requires:	wxMotif-gl = %{version}-%{release}

%description -n wxMotif-gl-devel
Development files for wxMotif GL canvas library.

%description -n wxMotif-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxMotif.

%package -n wxMotif-unicode
Summary:	wxMotif library with UNICODE support
Summary(pl.UTF-8):	Biblioteka wxMotif z obsługą UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxBase-unicode = %{version}-%{release}
Obsoletes:	wxMotif-univ-unicode < 2.5.3

%description -n wxMotif-unicode
wxWidgets library using Motif widgets with UNICODE support.

%description -n wxMotif-unicode -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów Motif z obsługą UNICODE.

%package -n wxMotif-unicode-devel
Summary:	Header files for wxMotif library with UNICODE support
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxMotif z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxMotif-unicode = %{version}-%{release}
Obsoletes:	wxMotif-univ-unicode-devel < 2.5.3

%description -n wxMotif-unicode-devel
Header files for wxWidgets library using Motif widgets with UNICODE
support.

%description -n wxMotif-unicode-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxWidgets używającej widgetów Motif z
obsługą UNICODE.

%package -n wxMotif-unicode-gl
Summary:	GL canvas library for wxMotif with UNICODE support
Summary(pl.UTF-8):	Biblioteka GL dla wxMotif z obsługą UNICODE
Group:		X11/Libraries
Requires:	wxMotif-unicode = %{version}-%{release}
Obsoletes:	wxMotif-univ-unicode-gl < 2.5.3

%description -n wxMotif-unicode-gl
GL canvas library for wxMotif with UNICODE support.

%description -n wxMotif-unicode-gl -l pl.UTF-8
Biblioteka GL dla wxMotif z obsługą UNICODE.

%package -n wxMotif-unicode-gl-devel
Summary:	Development files for GL canvas library for wxMotif with UNICODE support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxMotif z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxMotif-unicode-devel = %{version}-%{release}
Requires:	wxMotif-unicode-gl = %{version}-%{release}
Obsoletes:	wxMotif-univ-unicode-gl-devel < 2.5.3

%description -n wxMotif-unicode-gl-devel
Development files for GL canvas library for wxMotif with UNICODE
support.

%description -n wxMotif-unicode-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxMotif z obsługą UNICODE.

%package -n wxQT
Summary:	wxQT library
Summary(pl.UTF-8):	Biblioteka wxQT
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= 5.2.1
Requires:	Qt5Gui >= 5.2.1
Requires:	Qt5OpenGL >= 5.2.1
Requires:	Qt5Test >= 5.2.1
Requires:	Qt5Widgets >= 5.2.1
Requires:	wxBase = %{version}-%{release}

%description -n wxQT
wxWidgets library using QT widgets.

%description -n wxQT -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów QT.

%package -n wxQT-devel
Summary:	Header files for wxQT library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxQT
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= 5.2.1
Requires:	Qt5Gui-devel >= 5.2.1
Requires:	Qt5OpenGL-devel >= 5.2.1
Requires:	Qt5Test-devel >= 5.2.1
Requires:	Qt5Widgets-devel >= 5.2.1
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxQT = %{version}-%{release}

%description -n wxQT-devel
Header files for wxWidgets library using QT widgets.

%description -n wxQT-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki wxWidgets używającej widgetów QT.

%package -n wxQT-gl
Summary:	GL canvas library for wxQT
Summary(pl.UTF-8):	Biblioteka GL dla wxQT
Group:		X11/Libraries
Requires:	wxQT = %{version}-%{release}

%description -n wxQT-gl
wxQT GL canvas library.

%description -n wxQT-gl -l pl.UTF-8
Biblioteka GL dla wxQT.

%package -n wxQT-gl-devel
Summary:	Development files for GL canvas library for wxQT
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxQT
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxQT-devel = %{version}-%{release}
Requires:	wxQT-gl = %{version}-%{release}

%description -n wxQT-gl-devel
Development files for wxQT GL canvas library.

%description -n wxQT-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxQT.

%package -n wxQT-unicode
Summary:	wxQT library with UNICODE support
Summary(pl.UTF-8):	Biblioteka wxQT z obsługą UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core >= 5.2.1
Requires:	Qt5Gui >= 5.2.1
Requires:	Qt5OpenGL >= 5.2.1
Requires:	Qt5Test >= 5.2.1
Requires:	Qt5Widgets >= 5.2.1
Requires:	gtk-webkit3 >= 1.3.1
Requires:	wxBase-unicode = %{version}-%{release}

%description -n wxQT-unicode
wxWidgets library using QT widgets with UNICODE support.

%description -n wxQT-unicode -l pl.UTF-8
Biblioteka wxWidgets używająca widgetów QT z obsługą UNICODE.

%package -n wxQT-unicode-devel
Summary:	Header files for wxQT library with UNICODE support
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wxQT z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= 5.2.1
Requires:	Qt5Gui-devel >= 5.2.1
Requires:	Qt5OpenGL-devel >= 5.2.1
Requires:	Qt5Test-devel >= 5.2.1
Requires:	Qt5Widgets-devel >= 5.2.1
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxQT-unicode = %{version}-%{release}

%description -n wxQT-unicode-devel
Header files for wxWidgets library using QT widgets with UNICODE
support.

%description -n wxQT-unicode-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wxWidgets używającej widgetów QT z obsługą
UNICODE.

%package -n wxQT-unicode-gl
Summary:	GL canvas library for wxQT with UNICODE support
Summary(pl.UTF-8):	Biblioteka GL dla wxQT z obsługą UNICODE
Group:		X11/Libraries
Requires:	wxQT-unicode = %{version}-%{release}

%description -n wxQT-unicode-gl
GL canvas library for wxQT with UNICODE support.

%description -n wxQT-unicode-gl -l pl.UTF-8
Biblioteka GL dla wxQT z obsługą UNICODE.

%package -n wxQT-unicode-gl-devel
Summary:	Development files for GL canvas library for wxQT with UNICODE support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxQT z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxQT-unicode-devel = %{version}-%{release}
Requires:	wxQT-unicode-gl = %{version}-%{release}

%description -n wxQT-unicode-gl-devel
Development files for GL canvas library for wxQT with UNICODE support.

%description -n wxQT-unicode-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla wxQT z obsługą UNICODE.

%package utils
Summary:	Misc utils from wxWidgets project
Summary(pl.UTF-8):	Różne narzędzia z projektu wxWidgets
Group:		X11/Development/Tools
%if %{with unicode}
Requires:	wxX11-unicode = %{version}-%{release}
%else
Requires:	wxX11 = %{version}-%{release}
%endif
Obsoletes:	wxWindows-utils < 2.5

%description utils
Misc utils from wxWidgets project: wxemulator, wxrc, etc.

%description utils -l pl.UTF-8
Różne narzędzia z projektu wxWidgets: wxemulator, wxrc itp.

%package -n wxX11
Summary:	wxUniversal-based wxX11 library
Summary(pl.UTF-8):	Oparta na wxUniversal biblioteka wxX11
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxBase = %{version}-%{release}
Obsoletes:	wxX11-univ < 2.5.3

%description -n wxX11
wxUniversal-based wxX11 library.

%description -n wxX11 -l pl.UTF-8
Oparta na wxUniversal biblioteka wxX11.

%package -n wxX11-devel
Summary:	Header files for wxUniversal-based wxX11 library
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na wxUniversal biblioteki wxX11
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-devel = %{version}-%{release}
Requires:	wxX11 = %{version}-%{release}
Obsoletes:	wxX11-univ-devel < 2.5.3

%description -n wxX11-devel
Header files for wxUniversal-based wxX11 library.

%description -n wxX11-devel -l pl.UTF-8
Pliki nagłówkowe opartej na wxUniversal biblioteki wxX11.

%package -n wxX11-gl
Summary:	GL canvas library for wxUniversal-based wxX11
Summary(pl.UTF-8):	Biblioteka GL dla opartej na wxUniversal wxX11
Group:		X11/Libraries
Requires:	wxX11 = %{version}-%{release}
Obsoletes:	wxX11-univ-gl < 2.5.3

%description -n wxX11-gl
GL canvas library for wxUniversal-based wxX11.

%description -n wxX11-gl -l pl.UTF-8
Biblioteka GL dla opartej na wxUniversal wxX11.

%package -n wxX11-gl-devel
Summary:	Development files for GL canvas library for wxUniversal-based wxX11
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxX11-devel = %{version}-%{release}
Requires:	wxX11-gl = %{version}-%{release}
Obsoletes:	wxX11-univ-gl-devel < 2.5.3

%description -n wxX11-gl-devel
Development files for GL canvas library for wxUniversal-based wxX11.

%description -n wxX11-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11.

%package -n wxX11-unicode
Summary:	wxUniversal-based wxX11 library with UNICODE support
Summary(pl.UTF-8):	Oparta na wxUniversal biblioteka wxX11 z obsługą UNICODE
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxBase-unicode = %{version}-%{release}
Obsoletes:	wxX11-univ-unicode < 2.5.3

%description -n wxX11-unicode
wxUniversal-based wxX11 library with UNICODE support.

%description -n wxX11-unicode -l pl.UTF-8
Oparta na wxUniversal biblioteka wxX11 z obsługą UNICODE.

%package -n wxX11-unicode-devel
Summary:	Header files for wxUniversal-based wxX11 library with UNICODE support
Summary(pl.UTF-8):	Pliki nagłówkowe opartej na wxUniversal biblioteki wxX11 z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxBase-unicode-devel = %{version}-%{release}
Requires:	wxX11-unicode = %{version}-%{release}
Obsoletes:	wxX11-univ-unicode-devel < 2.5.3

%description -n wxX11-unicode-devel
Header files for wxUniversal-based wxX11 library with UNICODE support.

%description -n wxX11-unicode-devel -l pl.UTF-8
Pliki nagłówkowe opartej na wxUniversal biblioteki wxX11 z obsługą
UNICODE.

%package -n wxX11-unicode-gl
Summary:	GL canvas library for wxUniversal-based wxX11 with UNICODE support
Summary(pl.UTF-8):	Biblioteka GL dla opartej na wxUniversal wxX11 z obsługą UNICODE
Group:		X11/Libraries
Requires:	wxX11-unicode = %{version}-%{release}
Obsoletes:	wxX11-univ-unicode-gl < 2.5.3

%description -n wxX11-unicode-gl
GL canvas library for wxUniversal-based wxX11 with UNICODE support.

%description -n wxX11-unicode-gl -l pl.UTF-8
Biblioteka GL dla opartej na wxUniversal wxX11 z obsługą UNICODE.

%package -n wxX11-unicode-gl-devel
Summary:	Development files for GL canvas library for wxX11 with UNICODE support
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GL dla wxX11 z obsługą UNICODE
Group:		X11/Development/Libraries
Requires:	OpenGL-GLU-devel
Requires:	wxX11-unicode-devel = %{version}-%{release}
Requires:	wxX11-unicode-gl = %{version}-%{release}
Obsoletes:	wxX11-univ-unicode-gl-devel < 2.5.3

%description -n wxX11-unicode-gl-devel
Development files for GL canvas library for wxUniversal-based wxX11
with UNICODE support.

%description -n wxX11-unicode-gl-devel -l pl.UTF-8
Pliki programistyczne biblioteki GL dla opartej na wxUniversal wxX11 z
obsługą UNICODE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__rm} build/aclocal/bakefile*.m4

%build
%if "%(rpm -q bakefile --qf '%%{VERSION}')" != "0.2.13"
cd build/bakefiles
bakefile_gen -f autoconf
cd ../..
%endif
%{__aclocal} -I build/aclocal
%{__autoconf}

CPPFLAGS="%{rpmcppflags} %{rpmcflags} -Wno-narrowing -fPIC -I`pwd`/include"; export CPPFLAGS
# avoid adding -s to LDFLAGS
LDFLAGS=" "; export LDFLAGS
LDFLAGS=" "; export LDFLAGS
args="PYTHON=%{__python3} \
	%{?with_debug:--enable-debug}%{!?with_debug:--disable-debug} \
	--enable-ipv6 \
	--enable-calendar \
	--enable-controls \
	--enable-plugins \
	--enable-std_iostreams \
	--with-libmspack \
	--with-liblzma \
	--with-libpng \
	--with-libjpeg \
	--with-libtiff \
	%{?with_sdl:--with-sdl} \
	--with-opengl"

for gui in %{?with_gtk2:'--with-gtk=2'} %{?with_gtk3:'--with-gtk=3'} %{?with_motif:'--with-motif'} %{?with_qt:'--with-qt'} ; do
for unicode in %{?with_ansi:'--disable-unicode'} %{?with_unicode:'--enable-unicode'} ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	mkdir -p $objdir
	cd $objdir
	../%configure \
		${args} \
		${gui} \
		--enable-graphics_ctx \
		--disable-universal \
		${unicode} \
		--enable-printarch
	%{__make}
	cd ..
done
done

%if %{with x11} || %{with directfb}
for gui in %{?with_x11:'--with-x11'} %{?with_directfb:--with-directfb} ; do
for unicode in %{?with_ansi:'--disable-unicode'} %{?with_unicode:'--enable-unicode'} ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	mkdir -p $objdir
	cd $objdir
	../%configure \
		${args} \
		${gui} \
		--enable-universal \
		${unicode}
	%{__make}
	if echo $objdir| grep -q 'with-x11--%{?with_unicode:enable}%{!?with_unicode:disable}-unicode' ; then
		%{__make} -C utils
		%{__make} -C utils/emulator
		%{__make} -C utils/hhp2cached
	fi
	cd ..
done
done
%endif

%{__make} -C locale allmo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for gui in %{?with_gtk2:'--with-gtk=2'} %{?with_gtk3:'--with-gtk=3'} %{?with_motif:'--with-motif'} %{?with_qt:'--with-qt'} ; do
for unicode in %{?with_ansi:'--disable-unicode'} %{?with_unicode:'--enable-unicode'} ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	%{__make} -C $objdir install \
		DESTDIR=$RPM_BUILD_ROOT \
		LOCALE_MSW_LINGUAS=
done
done

%if %{with x11} || %{with directfb}
for gui in %{?with_x11:'--with-x11'} %{?with_directfb:--with-directfb} ; do
for unicode in %{?with_ansi:'--disable-unicode'} %{?with_unicode:'--enable-unicode'} ; do
	objdir=`echo obj${gui}${unicode}|sed 's/ /_/g'`
	cd $objdir
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT \
		LOCALE_MSW_LINGUAS=
	if echo $objdir| grep -q 'with-x11--%{?with_unicode:enable}%{!?with_unicode:disable}-unicode' ; then
		# TODO: install default config files and default backgrouds
		install utils/emulator/src/wxemulator $RPM_BUILD_ROOT%{_bindir}
		install utils/hhp2cached/hhp2cached $RPM_BUILD_ROOT%{_bindir}
	fi
	cd ..
done
done
%endif

# public headers include from wx/private
cp -a include/wx/private $RPM_BUILD_ROOT%{_includedir}/wx-%{majver}/wx/
cp -a include/wx/unix/private $RPM_BUILD_ROOT%{_includedir}/wx-%{majver}/wx/unix/

%if %{without gtk3}
install -d $RPM_BUILD_ROOT%{_libdir}/wx/%{majver}/web-extensions
%endif

for i in $RPM_BUILD_ROOT%{_libdir}/wx/config/*
do
	b=`basename $i`
	c=`echo $b|sed -e 's/\(.*\)-%{majver}/\1/'`
	if [ "$b" = "$c" ]; then
		echo "Something is not right... Sed rule failed"
		exit 1
	fi
	cp $i $RPM_BUILD_ROOT%{_bindir}/wx-${c}-config
done

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -f docs/x11/readme.txt docs/wxX11-readme.txt

%{__rm} $RPM_BUILD_ROOT%{_bindir}/wx-config

%find_lang wxstd-%{majver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n wxBase -p /sbin/ldconfig
%postun	-n wxBase -p /sbin/ldconfig

%post	-n wxBase-unicode -p /sbin/ldconfig
%postun	-n wxBase-unicode -p /sbin/ldconfig

%post	-n wxDFB -p /sbin/ldconfig
%postun	-n wxDFB -p /sbin/ldconfig

%post	-n wxDFB-unicode -p /sbin/ldconfig
%postun	-n wxDFB-unicode -p /sbin/ldconfig

%post	-n wxGTK2 -p /sbin/ldconfig
%postun	-n wxGTK2 -p /sbin/ldconfig

%post	-n wxGTK2-gl -p /sbin/ldconfig
%postun	-n wxGTK2-gl -p /sbin/ldconfig

%post	-n wxGTK2-unicode -p /sbin/ldconfig
%postun	-n wxGTK2-unicode -p /sbin/ldconfig

%post	-n wxGTK2-unicode-gl -p /sbin/ldconfig
%postun	-n wxGTK2-unicode-gl -p /sbin/ldconfig

%post	-n wxGTK3 -p /sbin/ldconfig
%postun	-n wxGTK3 -p /sbin/ldconfig

%post	-n wxGTK3-gl -p /sbin/ldconfig
%postun	-n wxGTK3-gl -p /sbin/ldconfig

%post	-n wxGTK3-unicode -p /sbin/ldconfig
%postun	-n wxGTK3-unicode -p /sbin/ldconfig

%post	-n wxGTK3-unicode-gl -p /sbin/ldconfig
%postun	-n wxGTK3-unicode-gl -p /sbin/ldconfig

%post	-n wxMotif -p /sbin/ldconfig
%postun	-n wxMotif -p /sbin/ldconfig

%post	-n wxMotif-gl -p /sbin/ldconfig
%postun	-n wxMotif-gl -p /sbin/ldconfig

%post	-n wxMotif-unicode -p /sbin/ldconfig
%postun	-n wxMotif-unicode -p /sbin/ldconfig

%post	-n wxMotif-unicode-gl -p /sbin/ldconfig
%postun	-n wxMotif-unicode-gl -p /sbin/ldconfig

%post	-n wxQT -p /sbin/ldconfig
%postun	-n wxQT -p /sbin/ldconfig

%post	-n wxQT-gl -p /sbin/ldconfig
%postun	-n wxQT-gl -p /sbin/ldconfig

%post	-n wxQT-unicode -p /sbin/ldconfig
%postun	-n wxQT-unicode -p /sbin/ldconfig

%post	-n wxQT-unicode-gl -p /sbin/ldconfig
%postun	-n wxQT-unicode-gl -p /sbin/ldconfig

%post	-n wxX11 -p /sbin/ldconfig
%postun	-n wxX11 -p /sbin/ldconfig

%post	-n wxX11-gl -p /sbin/ldconfig
%postun	-n wxX11-gl -p /sbin/ldconfig

%post	-n wxX11-unicode -p /sbin/ldconfig
%postun	-n wxX11-unicode -p /sbin/ldconfig

%post	-n wxX11-unicode-gl -p /sbin/ldconfig
%postun	-n wxX11-unicode-gl -p /sbin/ldconfig

%define libflag %{?with_debug:d}

%files -f wxstd-%{majver}.lang
%defattr(644,root,root,755)
%doc docs/{changes,licence,licendoc,preamble,readme}.txt
%dir %{_libdir}/wx
%dir %{_libdir}/wx/%{majver}
%dir %{_libdir}/wx/%{majver}/web-extensions

%files devel
%defattr(644,root,root,755)
%doc docs/tech docs/univ
%{_includedir}/wx-%{majver}
%dir %{_libdir}/wx/include
%dir %{_libdir}/wx/config
%{_aclocaldir}/wxwin.m4

%files -n bakefile-wxWidgets
%defattr(644,root,root,755)
%{_datadir}/bakefile/presets/wx*.bkl
%{_datadir}/bakefile/presets/wx_presets.py

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%if %{with ansi}
%files -n wxBase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_base%{libflag}-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_base%{libflag}-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_base%{libflag}_net-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_base%{libflag}_net-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_base%{libflag}_xml-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_base%{libflag}_xml-%{majver}.so.0
%if %{with sdl}
%attr(755,root,root) %{_libdir}/wx/%{majver}/sound_sdl%{libflag}-%{majver}.so
%endif

%files -n wxBase-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_base%{libflag}-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_base%{libflag}_net-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_base%{libflag}_xml-%{majver}.so
%endif

%if %{with unicode}
%files -n wxBase-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_baseu%{libflag}-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_baseu%{libflag}-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_baseu%{libflag}_net-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_baseu%{libflag}_net-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_baseu%{libflag}_xml-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_baseu%{libflag}_xml-%{majver}.so.0
%if %{with sdl}
%attr(755,root,root) %{_libdir}/wx/%{majver}/sound_sdlu%{libflag}-%{majver}.so
%endif

%files -n wxBase-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_baseu%{libflag}-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_baseu%{libflag}_net-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_baseu%{libflag}_xml-%{majver}.so
%endif

%if %{with directfb}
%if %{with ansi}
%files -n wxDFB
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbuniv%{libflag}_xrc-%{majver}.so.0

%files -n wxDFB-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbuniv%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/dfbuniv-ansi-%{majver}
%{_libdir}/wx/include/dfbuniv-ansi-%{majver}
%attr(755,root,root) %{_bindir}/wx-dfbuniv-ansi-config
%endif

%if %{with unicode}
%files -n wxDFB-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_dfbunivu%{libflag}_xrc-%{majver}.so.0

%files -n wxDFB-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_dfbunivu%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/dfbuniv-unicode-%{majver}
%{_libdir}/wx/include/dfbuniv-unicode-%{majver}
%attr(755,root,root) %{_bindir}/wx-dfbuniv-unicode-config
%endif
%endif

%if %{with gtk2}
%if %{with ansi}
%files -n wxGTK2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_webview-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_webview-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_xrc-%{majver}.so.0

%files -n wxGTK2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_webview-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/gtk2-ansi-%{majver}
%{_libdir}/wx/include/gtk2-ansi-%{majver}
%attr(755,root,root) %{_bindir}/wx-gtk2-ansi-config

%files -n wxGTK2-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2%{libflag}_gl-%{majver}.so.0

%files -n wxGTK2-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2%{libflag}_gl-%{majver}.so
%endif

%if %{with unicode}
%files -n wxGTK2-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_webview-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_webview-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_xrc-%{majver}.so.0

%files -n wxGTK2-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_webview-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/gtk2-unicode-%{majver}
%{_libdir}/wx/include/gtk2-unicode-%{majver}
%attr(755,root,root) %{_bindir}/wx-gtk2-unicode-config

%files -n wxGTK2-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk2u%{libflag}_gl-%{majver}.so.0

%files -n wxGTK2-unicode-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk2u%{libflag}_gl-%{majver}.so
%endif
%endif

%if %{with gtk3}
%if %{with ansi}
%files -n wxGTK3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_webview-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_webview-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_xrc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/wx/%{majver}/web-extensions/webkit2_ext-%{majver}.so

%files -n wxGTK3-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_webview-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/gtk3-ansi-%{majver}
%{_libdir}/wx/include/gtk3-ansi-%{majver}
%attr(755,root,root) %{_bindir}/wx-gtk3-ansi-config

%files -n wxGTK3-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3%{libflag}_gl-%{majver}.so.0

%files -n wxGTK3-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3%{libflag}_gl-%{majver}.so
%endif

%if %{with unicode}
%files -n wxGTK3-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_webview-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_webview-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_xrc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/wx/%{majver}/web-extensions/webkit2_extu-%{majver}.so

%files -n wxGTK3-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_webview-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/gtk3-unicode-%{majver}
%{_libdir}/wx/include/gtk3-unicode-%{majver}
%attr(755,root,root) %{_bindir}/wx-gtk3-unicode-config

%files -n wxGTK3-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_gtk3u%{libflag}_gl-%{majver}.so.0

%files -n wxGTK3-unicode-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_gtk3u%{libflag}_gl-%{majver}.so
%endif
%endif

%if %{with motif}
%if %{with ansi}
%files -n wxMotif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_xrc-%{majver}.so.0

%files -n wxMotif-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/motif-ansi-%{majver}
%{_libdir}/wx/include/motif-ansi-%{majver}
%attr(755,root,root) %{_bindir}/wx-motif-ansi-config

%files -n wxMotif-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motif%{libflag}_gl-%{majver}.so.0

%files -n wxMotif-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motif%{libflag}_gl-%{majver}.so
%endif

%if %{with unicode}
%files -n wxMotif-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_xrc-%{majver}.so.0

%files -n wxMotif-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/motif-unicode-%{majver}
%{_libdir}/wx/include/motif-unicode-%{majver}
%attr(755,root,root) %{_bindir}/wx-motif-unicode-config

%files -n wxMotif-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_motifu%{libflag}_gl-%{majver}.so.0

%files -n wxMotif-unicode-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_motifu%{libflag}_gl-%{majver}.so
%endif
%endif

%if %{with qt}
%if %{with ansi}
%files -n wxQT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_xrc-%{majver}.so.0

%files -n wxQT-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/qt-ansi-%{majver}
%{_libdir}/wx/include/qt-ansi-%{majver}
%attr(755,root,root) %{_bindir}/wx-qt-ansi-config

%files -n wxQT-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qt%{libflag}_gl-%{majver}.so.0

%files -n wxQT-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qt%{libflag}_gl-%{majver}.so
%endif

%if %{with unicode}
%files -n wxQT-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_xrc-%{majver}.so.0

%files -n wxQT-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/qt-unicode-%{majver}
%{_libdir}/wx/include/qt-unicode-%{majver}
%attr(755,root,root) %{_bindir}/wx-qt-unicode-config

%files -n wxQT-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_qtu%{libflag}_gl-%{majver}.so.0

%files -n wxQT-unicode-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_qtu%{libflag}_gl-%{majver}.so
%endif
%endif

%if %{with x11}
%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hhp2cached
%attr(755,root,root) %{_bindir}/wxemulator
%attr(755,root,root) %{_bindir}/wxrc
%attr(755,root,root) %{_bindir}/wxrc-%{majver}

%if %{with ansi}
%files -n wxX11
%defattr(644,root,root,755)
%doc docs/wxX11-readme.txt
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_xrc-%{majver}.so.0

%files -n wxX11-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/x11univ-ansi-%{majver}
%{_libdir}/wx/include/x11univ-ansi-%{majver}
%attr(755,root,root) %{_bindir}/wx-x11univ-ansi-config

%files -n wxX11-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univ%{libflag}_gl-%{majver}.so.0

%files -n wxX11-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univ%{libflag}_gl-%{majver}.so
%endif

%if %{with unicode}
%files -n wxX11-unicode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_adv-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_adv-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_aui-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_aui-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_core-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_core-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_html-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_html-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_media-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_media-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_propgrid-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_propgrid-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_qa-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_qa-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_ribbon-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_ribbon-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_richtext-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_richtext-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_stc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_stc-%{majver}.so.0
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_xrc-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_xrc-%{majver}.so.0

%files -n wxX11-unicode-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_adv-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_aui-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_core-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_html-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_media-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_propgrid-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_qa-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_ribbon-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_richtext-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_stc-%{majver}.so
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_xrc-%{majver}.so
%attr(755,root,root) %{_libdir}/wx/config/x11univ-unicode-%{majver}
%{_libdir}/wx/include/x11univ-unicode-%{majver}
%attr(755,root,root) %{_bindir}/wx-x11univ-unicode-config

%files -n wxX11-unicode-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_gl-%{majver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwx_x11univu%{libflag}_gl-%{majver}.so.0

%files -n wxX11-unicode-gl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwx_x11univu%{libflag}_gl-%{majver}.so
%endif
%endif
