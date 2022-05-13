import dload
import sys

#print(sys.argv[1:])
file_list = ["https://ftp.mozilla.org/pub/firefox/releases/0.8/contrib/firefox-0.8-i386-pc-solaris2.8.tar.gz",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/contrib/firefox-0.8-i386-unknown-netbsdelf1.6.tar.bz2",
			 "https://ftp.mozilla.org/pub/firefox/releases/1.0.6/linux-i686/da-DK/firefox-1.0.6.tar.gz",
			 "https://ftp.mozilla.org/pub/firefox/releases/1.0.6/linux-i686/da-DK/firefox-1.0.6.installer.tar.gz",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/contrib/firefox-0.8-i686-pc-linux-gnu-ctl-svg.tar.gz",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/contrib/firefox-0.8-sparc-sun-solaris2.8-gtk2.tar.gz",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/contrib/firefox-os2-0.8.zip",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/FirefoxSetup-0.8.exe",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/Firefox-0.8.zip",
			 "https://ftp.mozilla.org/pub/firefox/releases/0.8/firefox-source-0.8.tar.bz2",
			 "https://ftp.mozilla.org/pub/firefox/releases/1.0.6/win32/cs-CZ/Firefox%20Setup%201.0.6.exe"]

print(dload.save_multi(file_list, "test/", max_threads=10).bit_length())