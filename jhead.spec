Summary:	Command line tools to read and edit EXIF extensions in JPEG files
Name:		jhead
Version:	3.03
Release:	1
License:	Public Domain
Group:		Graphics
Url:		http://www.sentex.net/~mwandel/jhead/
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
Patch0:		jhead-2.97-ldflags.diff
# Without jpegtran the nicest features will not work
Requires:	libjpeg-progs

%description
Most digital cameras produce EXIF files, which are JPEG files with extra tags
that contain information about the image.

In contrary to the tools "exif" and "gexif" (and all other libexif-based tools
as "gphoto2") this tool gives a much easier readable summary of camera settings
(shutter speed in 1/x sec, focal length (also the 35-mm camera equivalent),
focal distance, ...), EXIF header manipulation as stripping off the thumbnail
and other info not needed, stripping off the complete header, applying
arbitrary conversion tools to the JPEG image and conserving the header,
renaming JPEG images with the capture date stored in the header, and even
turning the images upright when the camera has an orientation sensor (as Canon
Digital IXUS 400) ...

The tool is very compact, the executable has only a size of around 35 kb, the
whole package (with documentation) occupies 60 kb.

See %{_docdir}/jhead/usage.html for how to use this program.

%prep
%setup -q
%patch0 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 jhead %{buildroot}%{_bindir}
install -m0644 jhead.1 %{buildroot}%{_mandir}/man1

%files
%doc readme.txt usage.html changes.txt
%{_bindir}/*
%{_mandir}/*/*

