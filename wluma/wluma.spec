%global         debug_package %{nil}

%global         source_name wluma

Name:           wluma
Version:        4.9.0
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
RUSTUP_TOOLCHAIN=stable cargo build --release --locked --all-features --target-dir=target
# Generate docs 
# make docs doesn't work because of use of marked-man instead of marked
marked -i README.md -o "%{name}.7"
gzip "%{name}.7"

%install
install -D -m0755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}
install -Dm644 90-%{name}-backlight.rules \
  %{buildroot}%{_exec_prefix}/lib/udev/rules.d/90-%{name}-backlight.rules 
install -Dm644 %{name}.service \
  %{buildroot}%{_exec_prefix}/lib/systemd/user/%{name}.service
install -Dm644 LICENSE \
  %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dm644 README.md \
  %{buildroot}%{_datadir}/doc/%{name}
install -Dm644 %{name}.7.gz \
  %{buildroot}%{_datadir}/man/man7/%{name}.7.gz
install -Dm644 config.toml \
  %{buildroot}%{_datadir}/%{name}/examples/config.toml

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
