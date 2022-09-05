Name:           waydroid
Version:        1.2.1
Release:        1
Summary:        Uses a container-based approach to boot a full Android system
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/waydroid/waydroid
Source0:        https://github.com/waydroid/waydroid/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz


Requires:       lxc
Requires:       python3-gbinder
Requires:       python3-gobjec
Requires:       python3-pyclipper
#commenting out to prevent explicit-lib-dependency error
#Requires:       libgbinder1
#Requires:       libglibutil1
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
%make_instal

%pre
%service_add_pre %{name}-container.service

%post
%service_add_post %{name}-container.service

%preun
%service_del_preun %{name}-container.service

%postun
%service_del_postun %{name}-container.service

%files
