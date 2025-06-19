%global         debug_package %{nil}

%global commit fd73c76c2d289f9eb9ad9b0695fa9e9f151be22f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_rel .git%{shortcommit}

Name:           idlehack
Version:        1.0.0
Release:        2%{?git_rel}%{?dist}
Summary:        Monitor dbus and inhibit swayidle when Firefox or Chromium request it
License:        ISC
URL:            https://github.com/loops/idlehack
Source0:        %{url}/archive/%{commit}/%{name}-master-%{commit}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd-libs
BuildRequires: dbus-devel
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: libX11-devel
%description
%{summary}

%prep
%autosetup -n %{name}-%{commit}

%build
make

%install
# Install the compiled binary
install -D -m0755 %{name} \
  %{buildroot}%{_libexecdir}/%{name}
install -D -m0755 swayidle-inhibit \
  %{buildroot}%{_bindir}/swayidle-inhibit
install -D -m0644 %{name}.service \
  %{buildroot}%{_userunitdir}/%{name}.service

%files
%license LICENSE.txt
%{_libexecdir}/idlehack
%{_bindir}/swayidle-inhibit
%{_userunitdir}/%{name}.service

%changelog
* Tue Jun 17 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.0-2.gitfd73c76
- Use better macros and file section

* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
