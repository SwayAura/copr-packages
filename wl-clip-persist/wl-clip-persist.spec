%global         debug_package %{nil}

%global         source_name wl-clip-persist

Name:           wl-clip-persist
Version:        0.4.3
Release:        1%{?dist}
Summary:        Keep Wayland clipboard even after programs close
License:        MIT
URL:            https://github.com/Linus789/wl-clip-persist
Source0:        %{url}/archive/v%{version}/%{source_name}-%{version}.tar.gz

BuildRequires:	rust
BuildRequires:  cargo

%description
Keep Wayland clipboard even after programs close

%prep
%autosetup

%build
# Build release binary with cargo
cargo build --release --locked

%install
# Install the compiled binary
install -D -m0755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}

# Install license
install -D -m0644 LICENSE \
  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/wl-clip-persist

%changelog
* Sun Jan 05 2025 Maximizer <maximizerr@ik.me> - 0.4.3-1
- Initial COPR/Fedora packaging
