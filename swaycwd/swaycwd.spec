%global         debug_package %{nil}

%global         source_name swaycwd

Name:           swaycwd
Version:        1.1
Release:        1%{?dist}
Summary:        alternative to xcwd for swayvm
License:        MIT
URL:            https://github.com/manjaro-sway/swaycwd
Source0:        %{url}/archive/refs/tags/%{version}-1.tar.gz

Requires: bash
Requires: jq
Requires: procps-ng


%description
%{summary}

%prep
%setup -n %{name}-%{version}-1
%install
install -D -m 755 %{name} "%{buildroot}%{_bindir}/%{name}"

%files
%{_bindir}/swaycwd

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 1.3.5-1
- Initial COPR/Fedora packaging
