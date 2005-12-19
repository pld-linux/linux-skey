Summary:	Security one-time passwords
Summary(pl):	Bezpieczne has³a jednokrotnego u¿ytku (one-time)
Name:		linux-skey
Version:	0.2
Release:	3
Epoch:		0
License:	unknown
Vendor:		Olaf Kirch <okir@caldera.de>
Group:		Applications/System
Source0:	ftp://czort.wie.gdzie.de/pub/%{name}-%{version}.tar.gz
# Source0-md5:	c88683f5e23eece9a9b97f35bb359c11
URL:		http://linux.mathematik.tu-darmstadt.de/pub/linux/people/okir
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a Linux port of the S/Key applications.

%description -l pl
Ten pakiet zawiera linuksow± wersjê aplikacji pakietu S/Key.

%package -n pam-pam_skey
Summary:	PAM modules for Linux-S/Key
Summary(pl):	Modu³y PAM dla Linux-S/Key
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	pam
Obsoletes:	pam_skey

%description -n pam-pam_skey
This package contains a Linux port of the S/Key PAM modules.

%description -n pam-pam_skey -l pl
Ten pakiet zawiera linuksow± wersjê modu³ów PAM pakietu S/Key.

%package devel
Summary:	Header files, static library and documentation for linux-skey
Summary(pl):	Pliki nag³ówkowe, biblioteka statyczna i dokumentacja do linux-skey
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files, static library and documentation for linux-skey.

%description devel -l pl
Pliki nag³ówkowe, biblioteka statyczna i dokumentacja do linux-skey.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/%{_lib}/security} \
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir},%{_includedir}}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5}

install /dev/null		$RPM_BUILD_ROOT%{_sysconfdir}/skeykeys
install	/dev/null		$RPM_BUILD_ROOT%{_sysconfdir}/skeyaccess
install skey			$RPM_BUILD_ROOT%{_bindir}/skey
install skeyinit		$RPM_BUILD_ROOT%{_sbindir}/skeyinit
install doc/*.1			$RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.5			$RPM_BUILD_ROOT%{_mandir}/man5
install pam_skey.so		$RPM_BUILD_ROOT/%{_lib}/security
install pam_skey_access.so	$RPM_BUILD_ROOT/%{_lib}/security
install libskey.a		$RPM_BUILD_ROOT%{_libdir}
install skey.h			$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Warning:skeyinit is a suid file"
ls -l %{_sbindir}/skeyinit

%files
%defattr(644,root,root,755)
%doc ChangeLog README samples/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/skeykeys
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/skeyaccess
%attr(755,root,root) %{_bindir}/skey
%attr(4755,root,root) %{_sbindir}/skeyinit
%{_mandir}/man*/*

%files -n pam-pam_skey
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
