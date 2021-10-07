%define gitdate 20211006 

Name:           tok
Version:        0.0.1
Release:        0.%{gitdate}.0
License:        GPL-3.0-or-later
Summary:        Telegram client built using Kirigami
Url:            https://invent.kde.org/cblack/tok
Source0:        https://invent.kde.org/network/tok/-/archive/dev/tok-dev.tar.bz2

BuildRequires:  qbs
BuildRequires:  cmake(ECM)
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets) 
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(KF5Kirigami2) 
BuildRequires:  cmake(KF5I18n) 
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5SyntaxHighlighting)
#BuildRequires:  cmake(Td)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  cmake(rlottie)

Requires:       kirigami2

%description
WIP, Pidor

%prep
%autosetup -n %{name}-dev

%build
# who is that smart to droping good cmake build system and switch to almost not used qbs?
qbs

%install
qbs install --install-root %{buildroot}

%files
