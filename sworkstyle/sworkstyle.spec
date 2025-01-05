Name:           sworkstyle
Version:        1.3.5
Release:        1%{?dist}
Summary:        Swayest Workstyle - Renames workspaces to the configured icons (for Sway WM)
License:        MIT
Url:            https://github.com/Lyr-7D1h/swayest_workstyle
Source0:         %{url}/archive/%{version}/swayest_workstyle-%{version}.tar.gz
Source1:        additional_files/sworkstyle.man
Source2:        additional_files/default_config.swayaura.toml

BuildRequires:	rust
BuildRequires:  cargo

Requires: fontawesome-fonts

# If you only want to build on x86_64 and aarch64:
ExclusiveArch:  x86_64 aarch64


%description
Swayest Workstyle - This tool will rename workspaces to the icons configured.
Mainly meant for the Sway window manager.

%prep
# Unpack the tarball into swayest_workstyle-1.3.5/
%autosetup -n swayest_workstyle-%{version}

# Copy over the man page from Source1
cp %{SOURCE1} sworkstyle.1

# Copy SwayAura configuration
cp %{SOURCE2} default_config.toml

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

# Install man page
install -D -m0644 %{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/sworkstyle
%{_mandir}/man1/sworkstyle.1*

%changelog
* Sun Jan 05 2025 Maximizerr <maximizerr@ik.me> - 1.3.5-1
- Initial COPR/Fedora packaging
