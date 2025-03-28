%define _empty_manifest_terminate_build 0

Name:           waydroid
Version:        1.5.1
Release:        1
Summary:        Uses a container-based approach to boot a full Android system
License:        GPL-3.0-or-later
URL:            https://github.com/waydroid/waydroid
Source0:        https://github.com/waydroid/waydroid/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libgbinder)
BuildRequires:  pkgconfig(libglibutil)
BuildRequires:  spec-helper
Requires: nftables
Requires: dnsmasq
Requires: lxc
Requires: python3dist(gbinder-python)
Requires: python3dist(dbus-python)
Requires: python-gobject3
Requires: python-gi
Requires: python3dist(pyclipper)
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

%post
%_post_service waydroid-container.service

%preun
%_preun_service waydroid-container.service

%files
%{_bindir}/waydroid
# No idea if /usr/lib/ is correct path. Make file force it and it is used also by other distros like fedora, suse or mga. No one change to %{_libdir}
%{_prefix}/lib/systemd/system/waydroid-container.service
%{_prefix}/lib/waydroid/
%{_datadir}/applications/Waydroid.desktop
%{_datadir}/applications/waydroid.market.desktop
%{_datadir}/metainfo/id.waydro.waydroid.metainfo.xml
