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

    def add_object(self, name, obj_type, data_json):
        url_path='/v1/objects/'+obj_type+'/'
        headers={'Accept': 'application/json'}
        return requests.put(self.url+':'+self.port+url_path+name, \
                            headers=headers,data=data_json, \
                            auth=(self.login, self.password), \
                            verify=self.verify)
    def get_object(self, name, obj_type):
        url_path='/v1/objects/'+obj_type+'/'
        return requests.get(self.url+':'+self.port+url_path+name, \
                            auth=(self.login, self.password), \
                            verify=self.verify)

    def mod_object(self, name, obj_type, data_json):
        url_path='/v1/objects/'+obj_type+'/'
        headers={'Accept': 'application/json'}
        return requests.post(self.url+':'+self.port+url_path+name, \
                             headers=headers,data=data_json, \
                             auth=(self.login, self.password), \
                             verify=self.verify)

    def del_object(self, name, obj_type, cascade):
        url_path='/v1/objects/'+obj_type+'/'
        headers={'Accept': 'application/json'}
        appends=''
        if cascade:
            appends="?cascade=1"
        return requests.delete(self.url+':'+self.port+url_path+name+appends, \
                            headers=headers,data="{}", \
                            auth=(self.login, self.password), \
                            verify=self.verify) 

    def add_host(self, name, templates=[], **attrs):
        data={}
        if templates:
            data['templates']=templates
        data['attrs']=attrs
        data_json=json.dumps(data)
        return self.add_object(name, 'hosts', data_json)

    def get_host(self, name='', as_object=True):
        resp = self.get_object(name, 'hosts')
        if as_object:
            return json.loads(resp.text)
        else:
            return resp

    def mod_host(self, name, **attrs):
        data={}
        data['attrs']=attrs
        data_json=json.dumps(data)
        return self.mod_object(name, 'hosts', data_json)

    def del_host(self, name, cascade=True):
        return self.del_object(name, 'hosts', cascade)

    def add_service(self, name, templates=[], **attrs):
        data={}
        if templates:
            data['templates']=templates
        data['attrs']=attrs
        data_json=json.dumps(data)
        return self.add_object(name, 'services', data_json)

    def get_service(self, name='', as_object=True):
        resp = self.get_object(name, 'services')
        if as_object:
            return json.loads(resp.text)
        else:
            return resp

    def mod_service(self, name, **attrs):
        data={}
        data['attrs']=attrs
        data_json=json.dumps(data)
        return self.mod_object(name, 'services', data_json)

    def del_service(self, name, cascade=True):
        return self.del_object(name, 'services', cascade)
