# Original rpm.spec source: https://gitlab.com/Alberto97/rpms

%define buildforkernels akmod
%global debug_package %{nil}

%global commit e0605c9cdff7bf3fe9587434614473ba8b7e5f63
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_rel .git%{shortcommit}
%global source_name ddcci-driver-linux-kmod
%global base_name ddcci-driver-linux

Name:           ddcci-driver-linux-kmod

Version:        0.4.4
Release:        3%{?git_rel}%{?dist}
Summary:        A pair of Linux kernel drivers for DDC/CI monitors

Group:          System Environment/Kernel

License:        GPL2

# This fork allow to build on Kernel > 6.11
# See https://gitlab.com/ddcci-driver-linux/ddcci-driver-linux/-/merge_requests/17
URL:            https://gitlab.com/nullbytepl/ddcci-driver-linux
Source0:        %{url}/-/archive/%{commit}/%{base_name}-%{commit}.tar.gz

# Original URL and Source
#URL:            https://gitlab.com/ddcci-driver-linux/ddcci-driver-linux
#Source0:        %{url}/-/archive/v%{version}/ddcci-driver-linux-v%{version}.tar.gz

Source1:        ddcci-drv.service
Source2:        ddcci-modprobe.sh

BuildRequires:  systemd-rpm-macros
BuildRequires:  %{_bindir}/kmodtool
Requires:       %{name}-common


# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo %{repo} --kmodname %{source_name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
%{summary}.

%package common
Summary: Userland package for ddcci-driver-linux
Group: System Environment/Kernel
Provides: %{source_name}-common = %{version}-%{release}

%description common
Userland package for ddcci-driver-linux

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo %{repo} --kmodname %{source_name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions} ; do
    cp -a ddcci-driver-linux-%{commit} _kmod_build_${kernel_version%%___*}
done

cp -rf %{_topdir}/SOURCES/ddcci-drv.service .
cp -rf %{_topdir}/SOURCES/ddcci-modprobe.sh .

%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M="${PWD}/_kmod_build_${kernel_version%%___*}/ddcci" modules
    make %{?_smp_mflags} -C "${kernel_version##*___}" M="${PWD}/_kmod_build_${kernel_version%%___*}/ddcci-backlight" modules
done


%install
install -D ddcci-drv.service ${RPM_BUILD_ROOT}%{_unitdir}/ddcci-drv.service
install -D -m 755 ddcci-modprobe.sh ${RPM_BUILD_ROOT}%{_exec_prefix}/lib/ddcci-driver/ddcci-modprobe.sh

for kernel_version in %{?kernel_versions}; do
    install -d ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
    install -D -m 0755 _kmod_build_${kernel_version%%___*}/*/*.ko  ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
done
%{?akmod_install}

%files common
%{_unitdir}/ddcci-drv.service
%{_exec_prefix}/lib/ddcci-driver/ddcci-modprobe.sh

%changelog
%autochangelog
