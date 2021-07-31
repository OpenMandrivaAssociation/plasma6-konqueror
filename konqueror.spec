%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE file and web browser
Name:		konqueror
Version:	21.07.90
Release:	1
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
%{_kde5_services}/bookmarks.desktop
%{_kde5_services}/filebehavior.desktop
%{_kde5_services}/kcmkonqyperformance.desktop
%{_kde5_services}/kcmperformance.desktop
%{_kde5_services}/khtml_behavior.desktop
%{_kde5_services}/khtml_filter.desktop
%{_kde5_services}/khtml_general.desktop
%{_kde5_services}/khtml_java_js.desktop
%{_kde5_services}/khtml_appearance.desktop
%{_kde5_services}/org.kde.konqueror.desktop
%{_kde5_iconsdir}/*/*/*/konqueror.*
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.?onqueror.*.xml
%{_qt5_plugindir}/kcm_bookmarks.so
%{_qt5_plugindir}/kcm_konq.so
%{_qt5_plugindir}/kcm_konqhtml.so
%{_qt5_plugindir}/kcm_performance.so

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
%{_datadir}/dolphinpart/kpartplugins/dirfilterplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/dirfilterplugin.rc
%{_datadir}/dolphinpart/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/kimgalleryplugin.rc
%{_datadir}/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/kshellcmdplugin.rc
%{_datadir}/khtml/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/khtml/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/khtml/kpartplugins/autorefresh.desktop
%{_datadir}/khtml/kpartplugins/autorefresh.rc
%{_datadir}/khtml/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/khtml/kpartplugins/plugin_babelfish.rc
%{_datadir}/khtml/kpartplugins/plugin_translator.desktop
%{_datadir}/khtml/kpartplugins/khtmltts.desktop
%{_datadir}/khtml/kpartplugins/khtmltts.rc
%{_datadir}/konqueror/icons/hicolor/*/actions/google.*
%{_datadir}/konqueror/kpartplugins/searchbar.desktop
%{_datadir}/konqueror/kpartplugins/searchbar.rc
%{_datadir}/konqueror/opensearch/google.xml
%{_datadir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/kwebkitpart/kpartplugins/autorefresh.desktop
%{_datadir}/kwebkitpart/kpartplugins/autorefresh.rc
%{_datadir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/kwebkitpart/kpartplugins/plugin_babelfish.rc
%{_datadir}/kwebkitpart/kpartplugins/plugin_translator.desktop
%{_datadir}/kwebkitpart/kpartplugins/khtmltts.desktop
%{_datadir}/kwebkitpart/kpartplugins/khtmltts.rc
%{_datadir}/webenginepart/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/webenginepart/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/webenginepart/kpartplugins/autorefresh.desktop
%{_datadir}/webenginepart/kpartplugins/autorefresh.rc
%{_datadir}/webenginepart/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/webenginepart/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/webenginepart/kpartplugins/khtmltts.desktop
%{_datadir}/webenginepart/kpartplugins/khtmltts.rc
%{_datadir}/webenginepart/kpartplugins/plugin_babelfish.rc
%{_datadir}/webenginepart/kpartplugins/plugin_translator.desktop
%{_datadir}/webenginepart/kpartplugins/uachangerplugin.desktop
%{_datadir}/webenginepart/kpartplugins/uachangerplugin.rc
%{_iconsdir}/hicolor/*/actions/babelfish.*
%{_iconsdir}/hicolor/*/actions/imagegallery.*
%{_iconsdir}/hicolor/*/apps/fsview.*
%{_kde5_services}/fsview_part.desktop
%{_kde5_sysconfdir}/xdg/translaterc
%{_qt5_plugindir}/akregatorkonqfeedicon.so
%{_qt5_plugindir}/autorefresh.so
%{_qt5_plugindir}/babelfishplugin.so
%{_qt5_plugindir}/dirfilterplugin.so
%{_qt5_plugindir}/khtmlsettingsplugin.so
%{_qt5_plugindir}/khtmlttsplugin.so
%{_qt5_plugindir}/kimgallery.so
%{_qt5_plugindir}/konq_shellcmdplugin.so
%{_qt5_plugindir}/searchbarplugin.so
%{_qt5_plugindir}/kf5/parts/fsviewpart.so
%{_qt5_plugindir}/kf5/parts/konq_sidebar.so
%{_datadir}/qlogging-categories5/akregatorplugin.categories
%{_libdir}/qt5/plugins/kf5/kfileitemaction/akregatorplugin.so
%{_datadir}/kservices5/akregator_konqplugin.desktop
%{_datadir}/webenginepart/error.html
%{_sysconfdir}/xdg/konqsidebartngrc
%{_qt5_plugindir}/kcm_history.so
%{_qt5_plugindir}/konqsidebar_bookmarks.so
%{_qt5_plugindir}/konqsidebar_history.so
%{_qt5_plugindir}/konqsidebar_places.so
%{_qt5_plugindir}/konqsidebar_tree.so
%{_qt5_plugindir}/uachangerplugin.so
%{_datadir}/khtml/kpartplugins/uachangerplugin.desktop
%{_datadir}/khtml/kpartplugins/uachangerplugin.rc
%{_datadir}/konqsidebartng
%{_datadir}/kservices5/kcmhistory.desktop
%{_datadir}/kservices5/konq_sidebartng.desktop
%{_datadir}/kwebkitpart/kpartplugins/uachangerplugin.desktop
%{_datadir}/kwebkitpart/kpartplugins/uachangerplugin.rc
%{_datadir}/kxmlgui5/fsview/fsview_part.rc
%{_datadir}/qlogging-categories5/fsview.categories
# = webarchive plugin =
%{_bindir}/kcreatewebarchive
%{_libdir}/qt5/plugins/webarchiverplugin.so
%{_libdir}/qt5/plugins/webarchivethumbnail.so
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_datadir}/icons/hicolor/*/actions/webarchiver.*
%{_datadir}/kconf_update/webenginepart.upd
%{_datadir}/khtml/kpartplugins/plugin_webarchiver.*
%{_datadir}/kservices5/webarchivethumbnail.desktop
%{_datadir}/kwebkitpart/kpartplugins/plugin_webarchiver.desktop
%{_datadir}/kwebkitpart/kpartplugins/plugin_webarchiver.rc
%{_datadir}/webenginepart/kpartplugins/plugin_webarchiver.desktop
%{_datadir}/webenginepart/kpartplugins/plugin_webarchiver.rc

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
