Name:           swaycons
Version:        0.3.1
Release:        1%{?dist}
Summary:        Window Icons in Sway with Nerd Fonts
License:        MIT
URL:            https://github.com/allie-wake-up/swaycons
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cargo
BuildRequires:  cargo-packaging

%description
%{summary}

%prep
%autosetup

%build
%cargo_build

%check
%cargo_test

%install
%cargo_install
install -m0644 %{_builddir}/src/config.toml %{buildroot}%{_sysconfdir}/xdg/%{name}/config.toml

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config.toml
%{_bindir}/swaycons

%changelog
