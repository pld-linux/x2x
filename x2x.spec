# $Id: x2x.spec,v 1.1 2004-08-17 06:58:20 aredridel Exp $

# Authority: dag

Summary:	Link two X displays together, simulating a multiheaded display
Name:		x2x
Version:	1.30
Release:	0
License:	BSD
Group:		X11/Applications/Networking
Source0:	http://www.odsd.org/x2x/%{name}-%{version}-beta.tar.gz
# Source0-md5:	af4aa7d73123b94489558029f910fbed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel

%description
x2x joins a pair of X displays together, as if they were a single
multiheaded display. The pointer can be warped between displays, or,
depending on how you start x2x, can slide from one display to the
other when it runs off the edge of the screen. Keyboard focus also
moves between displays in the way you'd expect, and the X selection
propagates around. At least one of the displays involved
(specifically, the one being controlled remotely) must support the
XTEST extension.

%prep
%setup -q -n %{name}-%{version}-beta

%build
xmkmf
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
		$RPM_BUILD_ROOT%{_mandir}/man1
install x2x $RPM_BUILD_ROOT%{_bindir}
install x2x.man $RPM_BUILD_ROOT%{_mandir}/man1/x2x.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
