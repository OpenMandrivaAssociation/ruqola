Name:          ruqola
Version:       2.5.0
Release:       1
Summary:       Qt-based client for Rocket Chat
Group:         Internet
License:       BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:           https://invent.kde.org/network/%{name}

Source:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: appstream-util
# Qt
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6NetworkAuth)
BuildRequires: cmake(Qt6MultimediaWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6Test)

# KDE Frameworks
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6TextTranslator)
BuildRequires: cmake(KF6TextAutoCorrectionWidgets)
BuildRequires: cmake(KF6TextEditTextToSpeech)
BuildRequires: cmake(KF6TextEmoticonsWidgets)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6DocTools)
# BuildRequires: cmake(KLLMWidgets)
#BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(PlasmaActivities)

Requires: hicolor-icon-theme
Provides: bundled(cmark-rc)

%description
Ruqola is a Rocket chat client for the KDE desktop.

%package       doc
Summary:       HTML documentation for %{name}
BuildArch:     noarch
%description   doc
%{summary}.

%prep
%autosetup -p1

%build
%cmake -DQT_MAJOR_VERSION=6
%make_build

%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/ruqola
%{_datadir}/applications/org.kde.ruqola.desktop
%{_datadir}/icons/hicolor/*/apps/ruqola.png
%{_datadir}/knotifications6/ruqola.notifyrc
%{_datadir}/messageviewer/openurlwith/ruqola.openurl
%{_datadir}/qlogging-categories6/ruqola.{categories,renamecategories}
%{_libdir}/{librocketchatrestapi-qt,libruqolacore,libruqolawidgets}.so.%{version}
%{_libdir}/{librocketchatrestapi-qt,libruqolacore,libruqolawidgets}.so.0
%{_metainfodir}/org.kde.ruqola.appdata.xml
%{_libdir}/plugins/ruqolaplugins/
%{_libdir}/libcmark-rc-copy.so.*

%files doc
%dir %{_docdir}/HTML/en/ruqola
%{_docdir}/HTML/en/ruqola/index.cache.*
%{_docdir}/HTML/en/ruqola/index.docbook
