# FIXME we need to build the images this downloads on
# "waydroid init" from source for this to be properly
# 100% free
Name:           waydroid
Version:        1.5.2
Release:        1
Summary:        Uses a container-based approach to boot a full Android system
License:        GPL-3.0-or-later
URL:            https://github.com/waydroid/waydroid
Source0:        https://github.com/waydroid/waydroid/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  pkgconfig(libgbinder)
BuildRequires:  pkgconfig(libglibutil)
BuildRequires:  spec-helper
Requires: nftables
Requires: dnsmasq
Requires: lxc
Requires: python%{pyver}dist(gbinder-python)
Requires: python%{pyver}dist(dbus-python)
Requires: python-gobject3
Requires: python-gi
Requires: python%{pyver}dist(pyclipper)
Requires: gtk+3.0
Requires: %{_lib}glibutil
Requires: %{_lib}gbinder

Recommends: wl-clipboard


%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full Android system
in a container and provide Android applications on any GNU/Linux-based platform.
The Android system inside the container has direct access to any needed hardware.
The Android runtime environment ships with a minimal customized Android system image based on LineageOS.
The image is currently based on Android 10.

%prep
%autosetup -p1

%build
# Nothing to build, just run make install

%install
%make_install

%files
%{_bindir}/waydroid
# No idea if /usr/lib/ is correct path. Make file force it and it is used also by other distros like fedora, suse or mga. No one change to %{_libdir}
%{_prefix}/lib/systemd/system/waydroid-container.service
%{_prefix}/lib/waydroid/
%{_datadir}/applications/Waydroid.desktop
%{_datadir}/applications/waydroid.market.desktop
%{_datadir}/applications/waydroid.app.install.desktop
%{_datadir}/dbus-1/system-services/id.waydro.Container.service
%{_datadir}/dbus-1/system.d/id.waydro.Container.conf
%{_datadir}/desktop-directories/waydroid.directory
%{_datadir}/icons/hicolor/512x512/apps/waydroid.png
%{_datadir}/polkit-1/actions/id.waydro.Container.policy
%{_datadir}/metainfo/id.waydro.waydroid.metainfo.xml
%{_sysconfdir}/xdg/menus/applications-merged/waydroid.menu
