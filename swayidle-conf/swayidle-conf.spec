%global         debug_package %{nil}

%global commit e3d9b8b390dc12224bdca23a0eb78265c824a360
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_rel .git%{shortcommit}
%global source_name sway-services

Name:           swayidle-conf
Version:        1.0
Release:        1%{?dist}
Summary:        Generate swayidle configuration from YAML
License:        MIT
URL:            https://github.com/xdbob/sway-services
Source:			%{url}/archive/%{commit}/%{name}-master-%{commit}.tar.gz
Source1:        swayidle.service

Requires: python

%description
%{summary}

%prep
%setup -n %{source_name}-%{commit}

%install
install -Dm0755 bin/%{name} "%{buildroot}%{_bindir}/%{name}"
install -Dm0644 %{SOURCE1} \
  %{buildroot}%{_exec_prefix}/lib/systemd/user/swayidle.service

%files
%_bindir/swayidle-conf
%_userunitdir/swayidle.service

%changelog
%autochangelog