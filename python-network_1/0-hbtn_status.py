#!/usr/bin/python3
"""A pythonscript that fetches https://intranet.hbtn.io/status using urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
