# _with_opencascade
# _with_nurbs
%define		cvsbuild	cvs20020617
Summary:	MindsEye - 3D modeler
Summary(pl):	MindsEye - modeler 3D
Name:		mindseye
Version:	0.5.38
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://sourceforge.net/%{name}/%{name}-%{cvsbuild}.tar.bz2
URL:		http://mindseye.sourceforge.net/
BuildRequires:	OpenGL-devel
%{?_with_nurbs++:BuildRequires:	nurbs++-devel}
%{?_with_opencascade:BuildRequires:	opencascade-devel}
BuildRequires:	qt-devel >= 3.0.5
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is the MindsEye project. The aim is a complete modeling/animation
package for the Linux operating system. Another goal is to combine
forces when it comes down to 3d programming. There currently exist a
number of specialised packages, which can do specific 3d-tasks. The
idea here is to create a total package which can be configured to do
all the major 3d-tasks you need. It is supposed to run on any X Window
system currently available.

%description -l pl
To jest projekt MindsEye. Jego celem jest stworzenie kompletnego
pakietu do modelowania i animacji dla Linuksa. Innym celem jest
po³±czenie si³ je¶li chodzi o programowanie 3D. Aktualnie istnieje
wiele specjalizowanych pakietów, które mog± wykonywaæ konkretne
zadania 3D. Idea jest taka, by stworzyæ pe³ny pakiet, który mo¿e byæ
skonfigurowany do wykonywania wszystkich g³ównych zadañ 3D. Ma dzia³aæ
na ka¿dym aktualnie dostêpnym systemie X Window.

%prep
%setup -q -n %{name}-%{cvsbuild}

%build
./configure \
	%{?_with_nurbs++:--with-NURBS-prefix= } \
	%{?_with_opencascade:--with-OOC-prefix=}
%{__make} mindseye

# documentation
%{__make} doc-all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
