# _with_opencascade
# _with_nurbs
%define		cvsbuild	cvs20020617
Summary:	MindsEye - 3D modeler
Summary(pl):	MindsEye - modeler 3D
Name:		mindseye
Version:	0.5.38
Release:	1
Copyright:	GPL
Group:		Graphics
Source0:	http://sourceforge.net/%{name}/%{name}-%{cvsbuild}.tar.bz2
%{?_with_nurbs++:BuildRequires:	nurbs++-devel}
%{?_with_opencascade:BuildRequires:	opencascade-devel}
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	XFree86-OpenGL-devel >= 4.2.0
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%prep
%setup -q -n %{name}-%{cvsbuild}

#%patch

%build
./configure \
	%{?_with_nurbs++:--with-NURBS-prefix= } \
	%{?_with_opencascade:--with-OOC-prefix=}
%{__make} mindseye

#makeing documentation
%{__make} doc-all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
