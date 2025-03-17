Name:		cliphist
Version:	0.6.1
Release:	1
Source0:	https://github.com/sentriz/cliphist/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	vendor_cliphist-v0.6.1.tar.xz
Summary:	clipboard history “manager” for wayland
URL:		https://github.com/cliphist/cliphist
License:	GPL-3.0
Group:	    Wayland
BuildRequires:	go
BuildRequires:	wl-clipboard
Requires:	wl-clipboard
Requires:	xdg-utils

%description
clipboard history “manager” for wayland

write clipboard changes to a history file
recall history with dmenu / rofi / wofi (or whatever other picker you like)
both text and images are supported
clipboard is preserved byte-for-byte
leading / trailing whitespace / no whitespace or newlines are preserved
won’t break fancy editor selections like vim wordwise, linewise, block mode
no concept of a picker, only pipes

%prep
%autosetup -p1 -a1 

%build 
go build -o %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license	LICENSE
%doc		readme.md CHANGELOG.md
