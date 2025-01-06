%global         debug_package %{nil}

%global         source_name poweralertd

Name:           poweralertd
Version:        0.3.0
Release:        1%{?dist}
Summary:        UPower-powered power alerter
License:        GPL-3.0
URL:            https://git.sr.ht/~kennylevinsen/poweralertd
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:	meson
BuildRequires:  gcc
BuildRequires:  systemd-libs
BuildRequires:  scdoc

Requires: glibc
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

# Install license
#install -D -m0644 LICENSE \
#  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/poweralertd
%{_exec_prefix}/lib/systemd/user/%{name}.service
%{_datadir}/man/man1/%{name}.1.gz

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
