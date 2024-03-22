#!/usr/bin/python3
# Python script that fetches https://alu-intranet.hbtn.io/status using urllib package

if __aaaa__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Response")
