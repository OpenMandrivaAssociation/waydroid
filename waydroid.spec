Name:           waydroid
Version:        1.3.1
Release:        1
Summary:        Uses a container-based approach to boot a full Android system
License:        GPL-3.0-or-later
URL:            https://github.com/waydroid/waydroid
Source0:        https://github.com/waydroid/waydroid/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libgbinder)
BuildRequires:  pkgconfig(libglibutil)
Requires:       nftables
Requires:       dnsmasq
Requires:       lxc
Requires:       python3dist(gbinder-python)
Requires:       python-gobject3
Requires:       python3dist(pyclipper)
Requires:       %{_lib}glibutil
Requires:       %{_lib}gbinder

BuildArch:      noarch


%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full Android system
in a container and provide Android applications on any GNU/Linux-based platform.
The Android system inside the container has direct access to any needed hardware.
The Android runtime environment ships with a minimal customized Android system image based on LineageOS.
The image is currently based on Android 10.

%prep
%autosetup -p1


%build

%install
%make_install LIBDIR=%{_libdir}

%post
%_post_service waydroid-container

%preun
%_preun_service waydroid-container

%files
