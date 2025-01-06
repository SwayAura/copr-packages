%global         debug_package %{nil}

Name:           swayr
Version:        0.4.2
Release:        1%{?dist}
Summary:        Window-switcher & more for sway
License:        GPL-3.0
URL:            https://git.sr.ht/~tsdh/swayr
Source0:        %{url}/archive/%{source_name}-%{version}.tar.gz

BuildRequires:	rust
BuildRequires:  cargo

%description
%{summary}

%prep
%autosetup

%build
RUSTUP_TOOLCHAIN=stable cargo build --release --locked --all-features --target-dir=target

%check
RUSTUP_TOOLCHAIN=stable cargo test --release --locked --target-dir=target
%install
# Install the compiled binary
install -D -m0755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}
install -D -m0755 target/release/%{name}d \
  %{buildroot}%{_bindir}/%{name}d

%files
%{_bindir}/swayr
%{_bindir}/swayrd

%changelog
%autochangelog
