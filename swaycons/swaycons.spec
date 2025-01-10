%global         debug_package %{nil}
%global         cargo_build_opts --release --locked --all-features --target-dir=target
%global         rust_tool_chain stable
Name:           swaycons
Version:        0.3.1
Release:        1%{?dist}
Summary:        Window Icons in Sway with Nerd Fonts
License:        MIT
URL:            https://github.com/allie-wake-up/swaycons.git
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  rust

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%{cargo_build}

%check
RUSTUP_TOOLCHAIN=%{rust_tool_chain} cargo test %{cargo_build_opts}

%install
install -D -m0755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config.toml
%{_bindir}/swaycons
%{_prefix}/lib/systemd/user/%{name}d.service

%changelog
