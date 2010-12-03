Summary:	Command line tools to read and edit EXIF extensions in JPEG files
Name:		jhead
Version:	2.90
%if %mdkversion < 201000
%define subrel	1
%endif
Release:	%mkrel 2
License:	Public Domain
Group:		Graphics
URL:		http://www.sentex.net/~mwandel/jhead/
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
Patch1:		jhead-2.87-format_not_a_string_literal_and_no_format_arguments.diff
# Without jpegtran the nicest features will not work
Requires:	libjpeg-progs
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch1 -p0 -b .format_not_a_string_literal_and_no_format_arguments

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 jhead %{buildroot}%{_bindir}
install -m0644 jhead.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt usage.html changes.txt
%{_bindir}/*
%{_mandir}/*/*
