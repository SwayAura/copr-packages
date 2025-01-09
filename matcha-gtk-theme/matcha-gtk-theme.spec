%global debug_package %{nil}

%global gitrelease 2024-05-01

Name: matcha-gtk-theme
Version: %(echo %{gitrelease} | tr '-' '.')
Release: 1%{?dist}
Summary: Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell

License: GNU General Public License v3.0
URL: https://github.com/vinceliuice/Matcha-gtk-theme
Source0: %{url}/archive/%{gitrelease}.tar.gz

Requires: gtk-murrine-engine
Requires: gtk2-engines

%description
Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Pantheon, XFCE, Mate, etc.
This theme is based on Arc gtk theme of horst3180. Thanks horst3180 sincerely for his great job!
horst3180 - Arc gtk theme: https://github.com/horst3180/Arc-theme

%prep
%autosetup -n Matcha-gtk-theme-%{gitrelease}

%install
install -m 0755 -d %{buildroot}%{_datadir}
install -m 0755 -d %{buildroot}%{_datadir}/themes
./install.sh -d %{buildroot}%{_datadir}/themes

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/Matcha-sea*
%{_datadir}/themes/Matcha-aliz*
%{_datadir}/themes/Matcha-azul*
%{_datadir}/themes/Matcha-pueril*
%{_datadir}/themes/Matcha-light-sea*
%{_datadir}/themes/Matcha-light-aliz*
%{_datadir}/themes/Matcha-light-azul*
%{_datadir}/themes/Matcha-light-pueril*
%{_datadir}/themes/Matcha-dark-sea*
%{_datadir}/themes/Matcha-dark-aliz*
%{_datadir}/themes/Matcha-dark-azul*
%{_datadir}/themes/Matcha-dark-pueril*

%changelog
%autochangelog

