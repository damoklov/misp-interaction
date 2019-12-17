from pymisp import PyMISP
from keys import misp_verifycert
import tools


def init(url, key):
    return PyMISP(url, key, misp_verifycert, 'json')


def create(misp_url, misp_key):
    misp = init(misp_url, misp_key)
    for _ in range(5):
        tools.create_dummy_event(misp)
