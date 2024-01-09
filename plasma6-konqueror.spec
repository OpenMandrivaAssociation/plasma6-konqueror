%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE file and web browser
Name:		plasma6-konqueror
Version:	24.01.85
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/konqueror-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Su)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6TextToSpeech)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	hunspell
BuildRequires:	myspell-en
Suggests:	keditbookmarks
Suggests:	%{name}-plugins
Requires:	%{name}-webenginepart

%description
KDE file and web browser.

%files -f konqueror.lang
%{_datadir}/qlogging-categories6/konqueror.categories
%{_datadir}/applications/kfmclient.desktop
%{_datadir}/applications/kfmclient_html.desktop
%{_datadir}/applications/kfmclient_war.desktop
%{_datadir}/applications/kfmclient_dir.desktop
%{_datadir}/applications/konqbrowser.desktop
%{_sysconfdir}/xdg/autostart/konqy_preload.desktop
%{_bindir}/kfmclient
%{_bindir}/konqueror
%{_datadir}/config.kcfg/konqueror*
%{_datadir}/kcmcss/template.css
%{_datadir}/kcontrol/*
%{_datadir}/konqueror/about/*
%{_datadir}/konqueror/pics/indicator_*.png
%{_docdir}/HTML/*/konqueror/
%{_docdir}/HTML/*/kcontrol6/
%{_datadir}/icons/*/*/*/konqueror.*
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.?onqueror.*.xml
%{_libdir}/qt6/plugins/konqueror_kcms
%{_sysconfdir}/xdg/useragenttemplatesrc
%{_datadir}/applications/bookmarks.desktop

#------------------------------------------------

%package plugins
Summary:	Konqueror plugins
Group:		Graphical desktop/KDE
Requires:	konqueror
%rename		konq-plugins

%description plugins
This module contains plugins that interact with Konqueror.

%files plugins -f plugins.lang
%{_bindir}/fsview
%{_datadir}/akregator/pics/feed.png
%{_datadir}/konqueror/icons/hicolor/*/actions/google.*
%{_datadir}/konqueror/partsrcfiles/akregatorkonqfeedicon.rc
%{_datadir}/konqueror/partsrcfiles/autorefresh.rc
%{_datadir}/konqueror/partsrcfiles/babelfishplugin.rc
%{_datadir}/konqueror/partsrcfiles/dirfilterplugin.rc
%{_datadir}/konqueror/partsrcfiles/khtmlsettingsplugin.rc
%{_datadir}/konqueror/partsrcfiles/kimgallery.rc
%{_datadir}/konqueror/partsrcfiles/konq_shellcmdplugin.rc
%{_datadir}/konqueror/partsrcfiles/konqueror_kget_browser_integration.rc
%{_datadir}/konqueror/partsrcfiles/searchbarplugin.rc
%{_datadir}/konqueror/partsrcfiles/uachangerplugin.rc
%{_datadir}/konqueror/partsrcfiles/webarchiverplugin.rc
%{_iconsdir}/hicolor/*/actions/babelfish.*
%{_iconsdir}/hicolor/*/actions/imagegallery.*
%{_iconsdir}/hicolor/*/apps/fsview.*
%{_sysconfdir}/xdg/translaterc
%{_qtdir}/plugins/akregatorkonqfeedicon.so
%{_qtdir}/plugins/autorefresh.so
%{_qtdir}/plugins/babelfishplugin.so
%{_qtdir}/plugins/dolphinpart/kpartplugins/kimgallery.so
%{_qtdir}/plugins/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_qtdir}/plugins/dolphinpart/kpartplugins/dirfilterplugin.so
%{_qtdir}/plugins/khtml/kpartplugins/akregatorkonqfeediconkhtml_kpartplugins.so
%{_qtdir}/plugins/khtml/kpartplugins/autorefreshkhtml_kpartplugins.so
%{_qtdir}/plugins/khtml/kpartplugins/babelfishpluginkhtml_kpartplugins.so
%{_qtdir}/plugins/khtml/kpartplugins/khtmlsettingspluginkhtml_kpartplugins.so
%{_qtdir}/plugins/khtml/kpartplugins/konqueror_kget_browser_integrationkhtml_kpartplugins.so
%{_qtdir}/plugins/khtml/kpartplugins/uachangerpluginkhtml_kpartplugins.so
%{_qtdir}/plugins/khtml/kpartplugins/webarchiverpluginkhtml_kpartplugins.so
%{_qtdir}/plugins/khtmlsettingsplugin.so
%{_qtdir}/plugins/khtmlttsplugin.so
%{_qtdir}/plugins/konqueror/kpartplugins/searchbarplugin.so
%{_qtdir}/plugins/konqueror_kget_browser_integration.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/akregatorkonqfeediconkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/autorefreshkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/babelfishpluginkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/khtmlsettingspluginkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/khtmlttspluginkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/konqueror_kget_browser_integrationkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/uachangerpluginkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/kwebkitpart/kpartplugins/webarchiverpluginkwebkitpart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%{_qtdir}/plugins/kf6/parts/fsviewpart.so
%{_qtdir}/plugins/kf6/parts/konq_sidebar.so
%{_datadir}/qlogging-categories6/akregatorplugin.categories
%{_libdir}/qt6/plugins/kf6/kfileitemaction/akregatorplugin.so
%{_datadir}/webenginepart/error.html
%{_sysconfdir}/xdg/konqsidebartngrc
%{_qtdir}/plugins/uachangerplugin.so
%{_datadir}/konqsidebartng
%{_datadir}/qlogging-categories6/fsview.categories
%{_datadir}/applications/org.kde.konqueror.desktop
%{_datadir}/konqueror/webengine_dictionaries
# = webarchive plugin =
%{_bindir}/kcreatewebarchive
%{_libdir}/qt6/plugins/webarchiverplugin.so
%{_libdir}/qt6/plugins/webarchivethumbnail.so
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_datadir}/icons/hicolor/*/actions/webarchiver.*
%{_datadir}/kconf_update/webenginepart.upd
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_bookmarks.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_history.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_konq.so
%{_libdir}/qt6/plugins/konqueror_kcms/kcm_performance.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_appearance.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_behavior.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_filter.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_general.so
%{_libdir}/qt6/plugins/konqueror_kcms/khtml_java_js.so

#----------------------------------------------------------------------------

%package libkonq
Summary:	KDE Frameworks 6 Konq library support files
Group:		Graphical desktop/KDE
%rename		libkonq

%description libkonq
KDE Frameworks 6 Konq library support files.

%files libkonq -f libkonq.lang
%{_datadir}/kf6/kbookmark/directory_bookmarkbar.desktop

#----------------------------------------------------------------------------

%package webenginepart
Summary:	Plasma 6 embeddable HTML component
Group:		Graphical desktop/KDE

%description webenginepart
Plasma 6 embeddable HTML component.

%files webenginepart -f webenginepart.lang
%{_iconsdir}/*/*/*/webengine.*
%{_libdir}/libkwebenginepart.so
%{_libdir}/qt6/plugins/kf6/parts/webenginepart.so
%{_datadir}/kservices6/webenginepart.desktop
%{_kde6_xmlguidir}/webenginepart/webenginepart.rc

#----------------------------------------------------------------------------

%define konquerorprivate_major 6
%define libkonquerorprivate %mklibname konquerorprivate %{konquerorprivate_major}

%package -n %{libkonquerorprivate}
Summary:	Konqueror shared library
Group:		System/Libraries

%description -n %{libkonquerorprivate}
Konqueror shared library.

%files -n %{libkonquerorprivate}
%{_libdir}/libkonquerorprivate.so.%{konquerorprivate_major}*

#----------------------------------------------------------------------------

%define kf6konq_major 6
%define libkf6konq %mklibname KF6Konq %{kf6konq_major}

%package -n %{libkf6konq}
Summary:	KDE Frameworks 6 Konq shared library
Group:		System/Libraries
Requires:	%{name}-libkonq

%description -n %{libkf6konq}
KDE Frameworks 6 Konq shared library.

%files -n %{libkf6konq}
%{_libdir}/libKF6Konq.so.%{kf6konq_major}*
%{_libdir}/libKF6Konq.so.6.97.0
%{_libdir}/libkonqsidebarplugin.so.*
%{_libdir}/libkonquerorprivate.so.*

#----------------------------------------------------------------------------

%define devkf6konq %mklibname KF6Konq -d

%package -n %{devkf6konq}
Summary:	Development files for KDE Frameworks 6 Konq library
Group:		Development/KDE and Qt
Requires:	%{libkf6konq} = %{EVRD}
Provides:	KF6Konq-devel = %{EVRD}

%description -n %{devkf6konq}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf6konq}
%{_includedir}/KF6/konq_events.h
%{_includedir}/KF6/konq_historyentry.h
%{_includedir}/KF6/konq_historyprovider.h
%{_includedir}/KF6/konq_kpart_plugin.h
%{_includedir}/KF6/konq_popupmenu.h
%{_includedir}/KF6/konq_version.h
%{_includedir}/KF6/libkonq_export.h
%{_includedir}/konqsidebarplugin.h
%{_libdir}/cmake/KF6Konq
%{_libdir}/libKF6Konq.so
%{_libdir}/libkonqsidebarplugin.so
%{_includedir}/KF6/asyncselectorinterface.h

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n konqueror-%{version}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang akregator_konqplugin
%find_lang autorefresh
%find_lang babelfish
%find_lang dirfilterplugin
%find_lang fsview
%find_lang imgalleryplugin
%find_lang kcmbookmarks
%find_lang kcmkonqhtml
%find_lang kcmkonq
%find_lang kcmperformance
%find_lang kfmclient
%find_lang kgetplugin
%find_lang khtmlsettingsplugin
%find_lang khtmltts
%find_lang kshellcmdplugin
%find_lang searchbarplugin
%find_lang uachangerplugin
%find_lang webarchiver
cat *.lang >plugins.lang

%find_lang konqueror
%find_lang libkonq
%find_lang webenginepart
