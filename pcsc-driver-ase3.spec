Summary:	PC/SC Lite driver for the Athena Smartcard Solutions ASEDriveIIIe reader
Summary(pl):	Sterownik PC/SC Lite dla czytnika Athena Smartcard Solutions ASEDriveIIIe
Name:		pcsc-driver-ase3
Version:	1.9.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.athena-scs.com/downloads/ASEDriveIIIe_1_9_1.tar.gz
# Source0-md5:	4cf018d7d3e2ebe261efc0333258737d
URL:		http://www.athena-scs.com/downloads.asp
BuildRequires:	libusb-devel
BuildRequires:	pcsc-lite-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC/SC Lite drivers for the Athena Smartcard Solutions ASEDriveIIIe
reader.

%description -l pl
Sterowniki PC/SC Lite dla czytnika Athena Smartcard Solutions
ASEDriveIIIe.

%package serial
Summary:	PC/SC Lite driver for the Athena Smartcard Solutions ASEDriveIIIe serial reader
Summary(pl):	Sterownik PC/SC Lite dla czytnika szeregowego Athena Smartcard Solutions ASEDriveIIIe
Group:		Libraries
Requires:	pcsc-lite >= 1.2.0

%description serial
PC/SC Lite driver for the Athena Smartcard Solutions ASEDriveIIIe
reader connected to serial port.

%description serial -l pl
Sterownik PC/SC Lite dla czytnika Athena Smartcard Solutions
ASEDriveIIIe pod³±czanego do portu szeregowego.

%package usb
Summary:	PC/SC Lite driver for the Athena Smartcard Solutions ASEDriveIIIe USB reader
Summary(pl):	Sterownik PC/SC Lite dla czytnika USB Athena Smartcard Solutions ASEDriveIIIe
Group:		Libraries
Requires:	pcsc-lite >= 1.2.0

%description usb
PC/SC Lite driver for the Athena Smartcard Solutions ASEDriveIIIe
reader connected to USB port.

%description usb -l pl
Sterownik PC/SC Lite dla czytnika Athena Smartcard Solutions
ASEDriveIIIe pod³±czanego do portu USB.

%prep
%setup -q -c

%build
%{__make} -C ASEDriveIIIeSerial%{version} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -I. `pkg-config --cflags libpcsclite`"

%{__make} -C ASEDriveIIIeUSB%{version} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -D_REENTRANT -Wall -I. `pkg-config --cflags libpcsclite`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers

install ASEDriveIIIeSerial%{version}/libase_drive.so $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers
cp -af ASEDriveIIIeUSB%{version}/ifd-AseIIIeUSB.bundle $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers

%clean
rm -rf $RPM_BUILD_ROOT

%files serial
%defattr(644,root,root,755)
%doc ASEDriveIIIeSerial%{version}/{LICENSE,README,etc/reader.conf}
%attr(755,root,root) %{_libdir}/pcsc/drivers/libase_drive.so

%files usb
%defattr(644,root,root,755)
%doc ASEDriveIIIeUSB%{version}/{LICENSE,README}
%dir %{_libdir}/pcsc/drivers/ifd-AseIIIeUSB.bundle
%dir %{_libdir}/pcsc/drivers/ifd-AseIIIeUSB.bundle/Contents
%attr(755,root,root) %{_libdir}/pcsc/drivers/ifd-AseIIIeUSB.bundle/Contents/Linux
%{_libdir}/pcsc/drivers/ifd-AseIIIeUSB.bundle/Contents/Resources
%{_libdir}/pcsc/drivers/ifd-AseIIIeUSB.bundle/Contents/Info.plist
%{_libdir}/pcsc/drivers/ifd-AseIIIeUSB.bundle/Contents/PkgInfo
