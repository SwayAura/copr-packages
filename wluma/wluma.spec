%global         debug_package %{nil}

%global         source_name wluma

Name:           wluma
Version:        4.9.0
Release:        2%{?dist}
Summary:        Automatic brightness adjustment based on screen contents and ALS
License:        ISC
URL:            https://github.com/maximbaz/wluma
Source0:        %{url}/archive/%{version}/%{source_name}-%{version}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: clang
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
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
RUSTUP_TOOLCHAIN=stable cargo build --release --locked --all-features --target-dir=target
# Generate docs 
# make docs doesn't work because of use of marked-man instead of marked
marked -i README.md -o "%{name}.7"
gzip "%{name}.7"

%install
install -D -m0755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}
install -Dm644 90-%{name}-backlight.rules \
  %{buildroot}%{_udevrulesdir}/90-%{name}-backlight.rules
install -Dm644 %{name}.service \
  %{buildroot}%{_userunitdir}/%{name}.service
install -Dm644 %{name}.7.gz \
  %{buildroot}%{_mandir}/man7/%{name}.7.gz
install -Dm644 config.toml \
  %{buildroot}%{_datadir}/%{name}/examples/config.toml

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_udevrulesdir}/90-%{name}-backlight.rules
%{_userunitdir}/%{name}.service
%{_mandir}/man7/%{name}.7.gz
%doc %{_datadir}/%{name}/examples/config.toml

%changelog
* Tue Jun 17 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.9.0-2
- Use better macros and file section

* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 1.3.5-1
- Initial COPR/Fedora packaging
