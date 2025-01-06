%global         debug_package %{nil}

Name:           cliphist
Version:        0.6.1
Release:        1%{?dist}
Summary:        wayland clipboard manager
License:        GPL3
URL:            https://github.com/sentriz/cliphist
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: go

Requires: glibc
Requires: wl-clipboard
Requires: xdg-utils

%description
%{summary}

%gopkg

%prep
%autosetup

%build
go build -ldflags "-linkmode external -extldflags '$LDFLAGS'" -o %{name}

%install
install -Dm0755 -t %{buildroot}%{_bindir}/ %{name}
install -Dm0644 LICENSE \
  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/*

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
