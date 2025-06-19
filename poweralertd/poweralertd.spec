%global         debug_package %{nil}

%global         source_name poweralertd

Name:           poweralertd
Version:        0.3.0
Release:        2%{?dist}
Summary:        UPower-powered power alerter
License:        GPL-3.0
URL:            https://git.sr.ht/~kennylevinsen/poweralertd
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:	meson
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  scdoc

Requires: glibc
Requires: pkgconfig(libsystemd)
Requires: systemd-libs
Requires: upower

%description
%{summary}

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
# Install the compiled binary
#install -D -m0755 build/%{name} \
#  %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/poweralertd
%{_userunitdir}/%{name}.service
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Jun 17 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.3.0-2
- Use better macros and file section

* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
