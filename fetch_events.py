from pymisp import PyMISP
from keys import misp_verifycert
import os
import json


def init(url, key):
    return PyMISP(url, key, misp_verifycert, 'json')


def download_last(m, last, out=None):
    result = m.download_last(last)
    if out is None:
        if 'response' in result:
            print(json.dumps(result['response']))
        else:
            print('No results for that time period')
            exit(0)
    else:
        with open(out, 'w') as f:
            f.write(json.dumps(result['response']))


def fetch(misp_url, misp_key):
    if os.path.exists('events.txt'):
        print('Output file already exists, aborting..')
        exit(0)

    misp = init(misp_url, misp_key)

    download_last(misp, '1d', 'events.txt')
