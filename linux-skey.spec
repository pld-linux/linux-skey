Summary:	Security one-time passwords
Summary(pl):	Bezpieczne has³a jednokrotnego u¿ytku (one-time)
Name:		linux-skey
Version:	0.2
Release:	2
License:	Unknown
Group:		Applications/System
Vendor:		Olaf Kirch <okir@caldera.de>
Source0:	ftp://czort.wie.gdzie.de/pub/%{name}-%{version}.tar.gz
URL:		http://linux.mathematik.tu-darmstadt.de/pub/linux/people/okir
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	pam

%description
This package contains a Linux port of the S/Key applications, and two
PAM modules.

%description -l pl
Linuksowa wersja pakietu S/Key. Zawiera modu³y autoryzuj±ce PAMa.

%package devel
Summary:	Header files, static library and documentation for linux-skey
Summary(pl):	Pliki nag³ówkowe, biblioteka statyczna i dokumentacja do linux-skey
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files, static library and documentation for linux-skey.

%description devel -l pl
Pliki nag³ówkowe, biblioteka statyczna i dokumentacja do linux-skey.

%prep
%setup -q

%build
aclocal
autoconf
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT/lib/security
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5}

install /dev/null		$RPM_BUILD_ROOT%{_sysconfdir}/skeykeys
install	/dev/null		$RPM_BUILD_ROOT%{_sysconfdir}/skeyaccess
install skey			$RPM_BUILD_ROOT%{_bindir}/skey
install skeyinit		$RPM_BUILD_ROOT%{_sbindir}/skeyinit
install doc/*.1			$RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.5			$RPM_BUILD_ROOT%{_mandir}/man5
install pam_skey.so		$RPM_BUILD_ROOT/lib/security
install pam_skey_access.so	$RPM_BUILD_ROOT/lib/security
install libskey.a		$RPM_BUILD_ROOT%{_libdir}
install skey.h			$RPM_BUILD_ROOT%{_includedir}

gzip -9nf ChangeLog README samples/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Warning:skeyinit is a suid file"
ls -l %{_sbindir}/skeyinit

%files
%defattr(644,root,root,755)
%doc samples/* {ChangeLog,README}.gz
%attr(644,root,root)  %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/skeykeys
%attr(600,root,root)  %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/skeyaccess
%attr(755,root,root)  %{_bindir}/skey
%attr(4755,root,root) %{_sbindir}/skeyinit
%attr(644,root,root)  %{_mandir}/man*/*
%attr(755,root,root)  /lib/security/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
%attr(644,root,root) %{_includedir}/*.h
