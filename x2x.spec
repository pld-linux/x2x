Summary:	Link two X displays together, simulating a multiheaded display
Summary(pl):	��czy ze sob� dwa wy�wietlacze X, udaj�c wieloekranowy wy�wietlacz
Name:		x2x
Version:	1.30
Release:	1
License:	BSD
Group:		X11/Applications/Networking
Source0:	http://www.odsd.org/x2x/%{name}-%{version}-beta.tar.gz
# Source0-md5:	af4aa7d73123b94489558029f910fbed
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x2x joins a pair of X displays together, as if they were a single
multiheaded display. The pointer can be warped between displays, or,
depending on how you start x2x, can slide from one display to the
other when it runs off the edge of the screen. Keyboard focus also
moves between displays in the way you'd expect, and the X selection
propagates around. At least one of the displays involved
(specifically, the one being controlled remotely) must support the
XTEST extension.

%description -l pl
x2x ��czy ze sob� par� wy�wietlaczy X, tak jakby by�y pojedynczym
wieloekranowym wy�wietlaczem. Wska�nik mo�e si� przesuwa� pomi�dzy
wy�wietlaczami, lub w zale�no�ci gdzie uruchomiono x2x, mo�e
przeskoczy� z jednego wy�wietlacza na drugi, gdy dojdzie do brzegu
ekranu. Wska�nik klawiatury mo�e si� tak�e prze��cza� mi�dzy
wy�wietlaczami w przewidywalny spos�b. Co najmniej jeden z
wy�wietlaczy (konkretniej, zdalnie kierowany) musi obs�ugiwa�
rozszerzenie XTEST.

%prep
%setup -q -n %{name}-%{version}-beta

%build
xmkmf
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D x2x $RPM_BUILD_ROOT%{_bindir}/x2x
install -D x2x.man $RPM_BUILD_ROOT%{_mandir}/man1/x2x.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
