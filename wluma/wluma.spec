%global         debug_package %{nil}

%global         source_name wluma

Name:           wluma
Version:        4.6.0
Release:        1%{?dist}
Summary:        Automatic brightness adjustment based on screen contents and ALS
License:        ISC
URL:            https://github.com/maximbaz/wluma
Source0:        %{url}/archive/%{version}/%{source_name}-%{version}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: clang
BuildRequires: systemd
BuildRequires: marked
BuildRequires: libv4l-devel
BuildRequires: vulkan-loader-devel
BuildRequires: rust-libudev-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: dbus-devel

Requires: dbus
Requires: vulkan-loader
Requires: systemd-libs
Requires: glibc
Requires: gcc
Requires: v4l-utils
Requires: vulkan

%description
%{summary}

%prep
%autosetup

%build
make build

# Generate docs 
# make docs don't work because of use of marked-man instead of marked
marked -i README.md -o "%{name}.7"
gzip "%{name}.7"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} 

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/wluma
%{_exec_prefix}/lib/udev/rules.d/90-%{name}-backlight.rules
%{_exec_prefix}/lib/systemd/user/%{name}.service
%{_datadir}/doc/%{name}
%{_datadir}/man/man7/%{name}.7.gz
%{_datadir}/%{name}/examples/config.toml

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 1.3.5-1
- Initial COPR/Fedora packaging
