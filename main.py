import urllib.request
import sys

try:
    url = sys.argv[1]
except:
    print("Need to give url")
    exit()

file_name = url.split('/')[-1]
print(file_name)
with urllib.request.urlopen(url) as url:
    f = open(file_name, 'wb')
    meta = url.info()
    file_size = round((int(meta.get("Content-Length"))), 2)
    print(f"Downloading : {file_name} Size : {round(file_size*9.53674e-7, 1)}MiB")
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = url.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        file_size_status = round(file_size_dl*9.53674e-7, 1)
        status = f"{file_size_status} [{round(((file_size_dl*100.) / file_size), 1)}%]"
        print(" "*60, end="\r")
        print(status, end="\r")
    print(f"\nSaved {file_name}")
    f.close()