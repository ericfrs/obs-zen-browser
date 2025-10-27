Name:           zen-browser
Version:        1.17.3b
Release:        0
Summary:        Minimal browser focused on privacy and calm browsing
License:        MPL-2.0
URL:            https://github.com/zen-browser/desktop
Source0:        %{url}/releases/download/%{version}/zen.linux-x86_64.tar.xz
Source1:        zen-browser.sh
Source2:        zen-browser.desktop
Source3:        policies.json
ExclusiveArch:  x86_64

BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  fdupes
BuildRequires:  mozilla-nss
BuildRequires:  mozilla-nss-certs
BuildRequires:  mozilla-nspr
BuildRequires:  hunspell
BuildRequires:  hyphen
Requires:       mozilla-nss
Requires:       mozilla-nss-certs
Requires:       mozilla-nspr
Requires:       hunspell
Requires:       hyphen

%description
%{summary}.

%prep
%setup -q -n zen

%build

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_libdir}/zen-browser

cp -a * %{buildroot}%{_libdir}/zen-browser/
rm -f %{buildroot}%{_libdir}/zen-browser/removed-files

install -m0755 %{_sourcedir}/zen-browser.sh %{buildroot}/usr/bin/zen-browser

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

for size in 16x16 32x32 48x48 64x64 128x128; do
    install -Dm644 %{buildroot}%{_libdir}/zen-browser/browser/chrome/icons/default/default${size/x*}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/zen-browser.png
done

install -d %{buildroot}%{_libdir}/zen-browser/distribution
install -m644 %{_sourcedir}/policies.json %{buildroot}%{_libdir}/zen-browser/distribution/policies.json

ln -sf /usr/share/hunspell %{buildroot}%{_libdir}/zen-browser/dictionaries
ln -sf /usr/share/hyphen %{buildroot}%{_libdir}/zen-browser/hyphenation
ln -sf /usr/lib64/libnssckbi.so %{buildroot}%{_libdir}/zen-browser/libnssckbi.so 

%fdupes %{buildroot}%{_libdir}/zen-browser

%check

%files
%{_bindir}/zen-browser
%{_libdir}/zen-browser
%{_datadir}/applications/zen-browser.desktop
%{_datadir}/icons/hicolor/*/apps/zen-browser.png

%changelog
* Tue Oct 27 2025 - 1.17.3b
- Initial package