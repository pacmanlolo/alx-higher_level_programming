#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
   You must use the package requests"""
import requests


if __name__ == '__main__':
    res = requests.get('https://alx-intranet.hbtn.io/status')
    te = res.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(te), te))
