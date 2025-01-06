%global         debug_package %{nil}

%global         source_name zeit

Name:           zeit
Version:        0.0.8
Release:        1%{?dist}
Summary:        Zeit, erfassen. A command line tool for tracking time spent on activities.
License:        MIT
URL:            https://github.com/mrusme/zeit
Source0:        %{url}/archive/v%{version}/%{source_name}-%{version}.tar.gz

BuildRequires:	go
BuildRequires:	git

%description
%{summary}

%prep
%autosetup

%build
# Build release binary with cargo
VERSION=%{version} make

%install
# Install the compiled binary
install -D -m0755 %{name} \
  %{buildroot}%{_bindir}/%{name}

# Install license
install -D -m0644 LICENSE \
  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/zeit

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
