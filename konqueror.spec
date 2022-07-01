%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE file and web browser
Name:		konqueror
Version:	22.04.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Su)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(hunspell)
Suggests:	keditbookmarks
Suggests:	%{name}-plugins
Requires:	%{name}-webenginepart

%description
KDE file and web browser.

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/konqueror.categories
%{_kde5_applicationsdir}/kfmclient.desktop
%{_kde5_applicationsdir}/kfmclient_html.desktop
%{_kde5_applicationsdir}/kfmclient_war.desktop
%{_kde5_applicationsdir}/kfmclient_dir.desktop
%{_kde5_applicationsdir}/konqbrowser.desktop
%{_kde5_autostart}/konqy_preload.desktop
%{_bindir}/kfmclient
%{_bindir}/konqueror
%{_datadir}/config.kcfg/konqueror*
%{_datadir}/kcmcss/template.css
%{_datadir}/kcontrol/*
%{_datadir}/konqueror/about/*
%{_datadir}/konqueror/pics/indicator_*.png
%{_docdir}/HTML/*/konqueror/
%{_docdir}/HTML/*/kcontrol5/
%{_libdir}/libkdeinit5_kfmclient.so
%{_libdir}/libkdeinit5_konqueror.so
%{_kde5_services}/org.kde.konqueror.desktop
%{_kde5_iconsdir}/*/*/*/konqueror.*
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.?onqueror.*.xml

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
%{_datadir}/konqueror/partsrcfiles/khtmlttsplugin.rc
%{_datadir}/konqueror/partsrcfiles/kimgallery.rc
%{_datadir}/konqueror/partsrcfiles/konq_shellcmdplugin.rc
%{_datadir}/konqueror/partsrcfiles/konqueror_kget_browser_integration.rc
%{_datadir}/konqueror/partsrcfiles/searchbarplugin.rc
%{_datadir}/konqueror/partsrcfiles/uachangerplugin.rc
%{_datadir}/konqueror/partsrcfiles/webarchiverplugin.rc
%{_iconsdir}/hicolor/*/actions/babelfish.*
%{_iconsdir}/hicolor/*/actions/imagegallery.*
%{_iconsdir}/hicolor/*/apps/fsview.*
%{_kde5_services}/fsview_part.desktop
%{_kde5_sysconfdir}/xdg/translaterc
%{_qt5_plugindir}/akregatorkonqfeedicon.so
%{_qt5_plugindir}/autorefresh.so
%{_qt5_plugindir}/babelfishplugin.so
%{_qt5_plugindir}/dolphinpart/kpartplugins/kimgallery.so
%{_qt5_plugindir}/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_qt5_plugindir}/dirfilterplugin.so
%{_qt5_plugindir}/khtml/kpartplugins/akregatorkonqfeediconkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/autorefreshkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/babelfishpluginkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/dirfilterpluginkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/khtmlsettingspluginkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/khtmlttspluginkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/konqueror_kget_browser_integrationkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/uachangerpluginkhtml_kpartplugins.so
%{_qt5_plugindir}/khtml/kpartplugins/webarchiverpluginkhtml_kpartplugins.so
%{_qt5_plugindir}/khtmlsettingsplugin.so
%{_qt5_plugindir}/khtmlttsplugin.so
%{_qt5_plugindir}/konqueror/kpartplugins/searchbarplugin.so
%{_qt5_plugindir}/konqueror_kget_browser_integration.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/akregatorkonqfeediconkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/autorefreshkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/babelfishpluginkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/dirfilterpluginkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/khtmlsettingspluginkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/khtmlttspluginkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/konqueror_kget_browser_integrationkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/uachangerpluginkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/kwebkitpart/kpartplugins/webarchiverpluginkwebkitpart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/dirfilterpluginwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/khtmlttspluginwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%{_qt5_plugindir}/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%{_qt5_plugindir}/kf5/parts/fsviewpart.so
%{_qt5_plugindir}/kf5/parts/konq_sidebar.so
%{_datadir}/qlogging-categories5/akregatorplugin.categories
%{_libdir}/qt5/plugins/kf5/kfileitemaction/akregatorplugin.so
%{_datadir}/webenginepart/error.html
%{_sysconfdir}/xdg/konqsidebartngrc
%{_qt5_plugindir}/konqsidebar_bookmarks.so
%{_qt5_plugindir}/konqsidebar_history.so
%{_qt5_plugindir}/konqsidebar_places.so
%{_qt5_plugindir}/konqsidebar_tree.so
%{_qt5_plugindir}/uachangerplugin.so
%{_datadir}/konqsidebartng
%{_datadir}/kservices5/konq_sidebartng.desktop
%{_datadir}/kxmlgui5/fsview/fsview_part.rc
%{_datadir}/qlogging-categories5/fsview.categories
# = webarchive plugin =
%{_bindir}/kcreatewebarchive
%{_libdir}/qt5/plugins/webarchiverplugin.so
%{_libdir}/qt5/plugins/webarchivethumbnail.so
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_datadir}/icons/hicolor/*/actions/webarchiver.*
%{_datadir}/kconf_update/webenginepart.upd
%{_datadir}/kservices5/webarchivethumbnail.desktop
%{_libdir}/qt5/plugins/konqueror_kcms/kcm_bookmarks.so
%{_libdir}/qt5/plugins/konqueror_kcms/kcm_history.so
%{_libdir}/qt5/plugins/konqueror_kcms/kcm_konq.so
%{_libdir}/qt5/plugins/konqueror_kcms/kcm_performance.so
%{_libdir}/qt5/plugins/konqueror_kcms/khtml_appearance.so
%{_libdir}/qt5/plugins/konqueror_kcms/khtml_behavior.so
%{_libdir}/qt5/plugins/konqueror_kcms/khtml_filter.so
%{_libdir}/qt5/plugins/konqueror_kcms/khtml_general.so
%{_libdir}/qt5/plugins/konqueror_kcms/khtml_java_js.so

#----------------------------------------------------------------------------

%package libkonq
Summary:	KDE Frameworks 5 Konq library support files
Group:		Graphical desktop/KDE
%rename		libkonq

%description libkonq
KDE Frameworks 5 Konq library support files.

%files libkonq -f libkonq.lang
%{_datadir}/kf5/kbookmark/directory_bookmarkbar.desktop

#----------------------------------------------------------------------------

%package webenginepart
Summary:	Plasma 5 embeddable HTML component
Group:		Graphical desktop/KDE

%description webenginepart
Plasma 5 embeddable HTML component.

%files webenginepart -f webenginepart.lang
%{_iconsdir}/*/*/*/webengine.*
%{_libdir}/libkwebenginepart.so
%{_libdir}/qt5/plugins/kf5/parts/webenginepart.so
%{_kde5_services}/webenginepart.desktop
%{_kde5_xmlguidir}/webenginepart/webenginepart.rc

#----------------------------------------------------------------------------

%define konquerorprivate_major 5
%define libkonquerorprivate %mklibname konquerorprivate %{konquerorprivate_major}

%package -n %{libkonquerorprivate}
Summary:	Konqueror shared library
Group:		System/Libraries

%description -n %{libkonquerorprivate}
Konqueror shared library.

%files -n %{libkonquerorprivate}
%{_libdir}/libkonquerorprivate.so.%{konquerorprivate_major}*

#----------------------------------------------------------------------------

%define kf5konq_major 6
%define libkf5konq %mklibname KF5Konq %{kf5konq_major}

%package -n %{libkf5konq}
Summary:	KDE Frameworks 5 Konq shared library
Group:		System/Libraries
Requires:	%{name}-libkonq

%description -n %{libkf5konq}
KDE Frameworks 5 Konq shared library.

%files -n %{libkf5konq}
%{_libdir}/libKF5Konq.so.%{kf5konq_major}*
%{_libdir}/libKF5Konq.so.5.97.0
%{_libdir}/libkonqsidebarplugin.so.*
%{_libdir}/libkonquerorprivate.so.*

#----------------------------------------------------------------------------

%define devkf5konq %mklibname KF5Konq -d

%package -n %{devkf5konq}
Summary:	Development files for KDE Frameworks 5 Konq library
Group:		Development/KDE and Qt
Requires:	%{libkf5konq} = %{EVRD}
Provides:	KF5Konq-devel = %{EVRD}

%description -n %{devkf5konq}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkf5konq}
%{_includedir}/KF5/konq_events.h
%{_includedir}/KF5/konq_historyentry.h
%{_includedir}/KF5/konq_historyprovider.h
%{_includedir}/KF5/konq_kpart_plugin.h
%{_includedir}/KF5/konq_popupmenu.h
%{_includedir}/KF5/konq_version.h
%{_includedir}/KF5/libkonq_export.h
%{_includedir}/konqsidebarplugin.h
%{_libdir}/cmake/KF5Konq
%{_libdir}/libKF5Konq.so
%{_libdir}/libkonqsidebarplugin.so

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

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
