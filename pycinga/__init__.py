""" interface to incinga """

import requests
import json

class icinga(object):
    def __init__(self, login, password, url, port, verify=True):
        self.login=login
        self.password=password
        self.url=url
        self.port=port
        self.verify=verify
    def add_host(self, name, templates=[], **attrs):
        url_path='/v1/objects/hosts/'
        data={}
        if templates:
            data['templates']=templates
        data['attrs']=attrs
        data_json=json.dumps(data)
        return requests.put(self.url+':'+self.port+url_path+name, \
                            data=data_json, auth=(self.login, self.password),\
                            verify=self.verify)
