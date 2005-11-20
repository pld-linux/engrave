Summary:	Edje editing library
Summary(pl):	Biblioteka edycji edje
Name:		engrave
Version:	0.1.0
%define	_snap	20051104
Release:	0.%{_snap}.0.1
License:	BSD
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/libs/%{name}-%{_snap}.tar.bz2
# Source0-md5:	bef0917c80af9c182994994adf8b48a7
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Engrave is an edje editing library.

%description -l pl
Engrave to biblioteka edycji edje.

%package devel
Summary:	Header files for engrave library
Summary(pl):	Pliki nag³ówkowe biblioteki engrave
Group:		Developement/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for engrave library.

%description devel -l pl
Pliki nag³ówkowe biblioteki engrave.

%package static
Summary:	Engrave static library
Summary(pl):	Statyczna biblioteka engrave
Group:		Developement/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Engrave static library.

%description static -l pl
Statyczna biblioteka engrave.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/%{name}*_test
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.a
