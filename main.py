import urllib.request
import sys

url = "https://proof.ovh.net/files/10Mb.dat"
file_name = url.split('/')[-1]
print(file_name)
with urllib.request.urlopen(url) as url:
    f = open(file_name, 'wb')
    meta = url.info()
    file_size = round((int(meta.get("Content-Length"))), 2)
    print(file_size)
    print("Downloading: %s Bytes: %s" % (file_name, file_size))
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = url.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = f"{file_size_dl} [{round(((file_size_dl*100.) / file_size), 1)}%]"
        print(status2)
    print(f"\nSaved {file_name}")
    f.close()

""" import urllib2

url = "http://download.thinkbroadband.com/10MB.zip"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close() """