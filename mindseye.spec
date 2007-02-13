#
# Conditional build:
# _with_opencascade
#
%define		cvsbuild	cvs20020617
Summary:	MindsEye - 3D modeler
Summary(pl.UTF-8):	MindsEye - modeler 3D
Name:		mindseye
Version:	0.5.38
Release:	0.%{cvsbuild}.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{cvsbuild}.tar.bz2
# Source0-md5:	3ff3ecf02ec0adfe28ce7e6e0b075723
Patch0:		%{name}-gcc3.patch
Patch1:		%{name}-qt.patch
Patch2:		%{name}-fix.patch
URL:		http://mindseye.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	nurbs++-devel
%{?_with_opencascade:BuildRequires:	opencascade-devel}
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
This is the MindsEye project. The aim is a complete modeling/animation
package for the Linux operating system. Another goal is to combine
forces when it comes down to 3d programming. There currently exist a
number of specialised packages, which can do specific 3d-tasks. The
idea here is to create a total package which can be configured to do
all the major 3d-tasks you need. It is supposed to run on any X Window
system currently available.

%description -l pl.UTF-8
To jest projekt MindsEye. Jego celem jest stworzenie kompletnego
pakietu do modelowania i animacji dla Linuksa. Innym celem jest
połączenie sił jeśli chodzi o programowanie 3D. Aktualnie istnieje
wiele specjalizowanych pakietów, które mogą wykonywać konkretne
zadania 3D. Idea jest taka, by stworzyć pełny pakiet, który może być
skonfigurowany do wykonywania wszystkich głównych zadań 3D. Ma działać
na każdym aktualnie dostępnym systemie X Window.

%prep
%setup -q -n %{name}-%{cvsbuild}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_13 \
	%{?_with_opencascade:--with-OOC-prefix=}

%{__make} mindseye

# documentation (but no doc dir)
#%{__make} doc-all

%install
rm -rf $RPM_BUILD_ROOT

# no install target yet
#%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_bindir}
install src/MindsEye $RPM_BUILD_ROOT%{_bindir}
# some files missing?

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Bugs ChangeLog Contributors README
%attr(755,root,root) %{_bindir}/*
