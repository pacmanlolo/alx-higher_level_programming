#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request
   to the passed URL with the email as a parameter,
   and finally displays the body of the response."""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) != 2:
        pars = {'q': ""}
    else:
        pars = {'q': sys.argv[1]}
    res = requests.post(url, data=pars)
    try:
        te = res.json()
        if te != {}:
            print('[{}] {}'.format(te['id'], te['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
