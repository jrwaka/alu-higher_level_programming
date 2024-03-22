#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status using urllib package"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://0.0.0.0:5050/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

