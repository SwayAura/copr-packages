%bcond check 1

%global crate swaycons

Name:           swaycons
Version:        0.3.1
Release:        %autorelease
Summary:        Adds nerd font icons to sway window titles

# Upstream license specification: MIT / Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/swaycons
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Swaycons adds nerd font icons to sway window titles.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        MIT OR Apache-2.0

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE-APACHE-2.0
%license LICENSE.dependencies
%doc README.md
%{_bindir}/swaycons

