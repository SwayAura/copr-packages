%global         debug_package %{nil}

%global commit fd73c76c2d289f9eb9ad9b0695fa9e9f151be22f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_rel .git%{shortcommit}

Name:           idlehack
Version:        1.0.0
Release:        1%{?git_rel}%{?dist}
Summary:        Monitor dbus and inhibit swayidle when Firefox or Chromium request it
License:        ISC
URL:            https://github.com/loops/idlehack
Source0:        %{url}/archive/%{commit}/%{name}-master-%{commit}.tar.gz

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
  %{buildroot}%{_exec_prefix}/lib/systemd/user/%{name}.service
# Install license
install -D -m0644 LICENSE.txt \
  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%license %{_licensedir}/%{name}/LICENSE
%{_libexecdir}/idlehack
%{_bindir}/swayidle-inhibit
%{_exec_prefix}/lib/systemd/user/%{name}.service

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
