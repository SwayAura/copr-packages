%global         debug_package %{nil}

Name:           autotiling-rs
Version:        0.1.3
Release:        1%{?dist}
Summary:        Automatically alternates container layouts between horizontal and vertical
License:        MIT
URL:            https://github.com/ammgws/autotiling-rs
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	rust
BuildRequires:  cargo

%description
%{summary}

%prep
%autosetup

%build
cargo build --release --locked

%install
# Install the compiled binary
install -D -m0755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}

# Install the compiled binary
#install -D -m0755 build/%{name} \
#  %{buildroot}%{_bindir}/%{name}

# Install license
#install -D -m0644 LICENSE \
#  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/autotiling-rs


%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
