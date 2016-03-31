""" interface to incinga """

import requests
import json

class icinga(object):
    def __init__(self, login, password, url, port, verify=True):
        self.login=login
        self.password=password
        self.url=url
        self.port=str(port)
        self.verify=verify
    def add_host(self, name, templates=[], **attrs):
        url_path='/v1/objects/hosts/'
        data={}
        if templates:
            data['templates']=templates
        data['attrs']=attrs
        headers={'Accept': 'application/json'}
        data_json=json.dumps(data)
        return requests.put(self.url+':'+self.port+url_path+name, \
                            headers=headers,data=data_json, \
                            v auth=(self.login, self.password), \
                            verify=self.verify)
    def del_host(self, name, cascade=True):
        url_path='/v1/objects/hosts/'
        appends=''
        headers={'Accept': 'application/json'}
        if cascade:
            appends="?cascade=1"
        return requests.delete(self.url+':'+self.port+url_path+name+appends, \
                            headers=headers,data="{}", \
                            auth=(self.login, self.password), \
                            verify=self.verify) 
