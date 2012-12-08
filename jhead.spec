Summary:	Command line tools to read and edit EXIF extensions in JPEG files
Name:		jhead
Version:	2.95
Release:	1
License:	Public Domain
Group:		Graphics
URL:		http://www.sentex.net/~mwandel/jhead/
Source0:	http://www.sentex.net/~mwandel/jhead/%{name}-%{version}.tar.gz
Patch0:		jhead-2.93-ldflags.diff
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


%changelog
* Wed Apr 18 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.95-1
+ Revision: 791732
- update to 2.95

* Sat Mar 03 2012 Oden Eriksson <oeriksson@mandriva.com> 2.93-2
+ Revision: 781988
- use %%ldflags

* Sun Dec 04 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.93-1
+ Revision: 737668
- version update 2.93

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.90-3
+ Revision: 665827
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.90-2mdv2011.0
+ Revision: 606085
- rebuild

* Mon May 17 2010 Eugeni Dodonov <eugeni@mandriva.com> 2.90-1mdv2010.1
+ Revision: 544969
- Updated to version 2.90.

* Sat Nov 14 2009 Eugeni Dodonov <eugeni@mandriva.com> 2.88-1mdv2010.1
+ Revision: 465935
- Updated to 2.88.
  Drop P0.

  + Oden Eriksson <oeriksson@mandriva.com>
    - re-bump
    - prepare for main/testing

* Sat Jun 20 2009 Oden Eriksson <oeriksson@mandriva.com> 2.87-1mdv2010.0
+ Revision: 387437
- 2.87
- P0: fix a buffer overflow (debian)
- P1: fix build with -Werror=format-security

* Mon Feb 16 2009 Eugeni Dodonov <eugeni@mandriva.com> 2.86-1mdv2009.1
+ Revision: 341087
- Updated to new upstream 2.86.

* Tue Jan 13 2009 Stéphane Téletchéa <steletch@mandriva.org> 2.84-1mdv2009.1
+ Revision: 329021
- New version 2.84
- Answer to bug #46988, which addresses vulerability issues

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.7-3mdv2009.0
+ Revision: 221711
- rebuild
- fix spacing at top of description

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.7-2mdv2008.1
+ Revision: 150420
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jul 13 2007 Adam Williamson <awilliamson@mandriva.org> 2.7-1mdv2008.0
+ Revision: 51738
- new release 2.7

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Import jhead




* Fri Jul 14 2006 Till Kamppeter <till@mandriva.com> 2.6-1mdv2007.0
- Updated to version 2.6.

* Sat Aug 13 2005 Till Kamppeter <till@mandriva.com> 2.4-1mdk
- Updated to version 2.4.

* Thu Jan 21 2005 Till Kamppeter <till@mandrakesoft.com> 2.3-1mdk
- Updated to version 2.3.

* Thu Jul 15 2004 Till Kamppeter <till@mandrakesoft.com> 2.2-1mdk
- Updated to version 2.2.

* Thu Jan 29 2004 Till Kamppeter <till@mandrakesoft.com> 2.1-1mdk
- Updated to version 2.1.

* Sun Jul 27 2003 Till Kamppeter <till@mandrakesoft.com> 2.0-2mdk
- Require the JPEG utilities ("libjpeg-prgs"), as without "jpegtran" this
  program's most interesting features do not work.
- Install man page.

* Fri Jun 13 2003 Till Kamppeter <till@mandrakesoft.com> 2.0-1mdk
- Updated to version 2.0.

* Thu Jan 16 2003 Till Kamppeter <till@mandrakesoft.com> 1.9-1mdk
- Updated to version 1.9.

* Sun Aug 18 2002 Till Kamppeter <till@mandrakesoft.com> 1.8-1mdk
- Initial release
