%define		_state		stable
%define		orgname		mplayerthumbs
%define		qtver		4.8.1

Summary:	Video thumbnail generator for KDE
Summary(pl.UTF-8):	Generator podglądów video dla KDE
Name:		kde4-%{orgname}
Version:	4.13.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	5a8bb270654ced722df5fc6460717c6b
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdebase >= %{version}
Requires:	mplayer
Obsoletes:	kde4-kdemultimedia-mplayerthumbs < 4.8.99-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPlayerThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...) , now available also for KDE 4.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mplayerthumbsconfig
%attr(755,root,root) %{_libdir}/kde4/videopreview.so
%{_datadir}/apps/videothumbnail
%{_datadir}/config.kcfg/mplayerthumbs.kcfg
%{_datadir}/kde4/services/videopreview.desktop
