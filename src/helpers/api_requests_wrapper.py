# Help us to make POST, PUT, GET, PATCH, DELETE REQUEST

import json
import requests
class Api_Request:

    def get_request(self,url,auth,headers):
        response=requests.get(url=url,auth=auth, headers=headers)
        return response

    def put_request(self,url,auth,headers,payload):
        response = requests.put(url=url,auth=auth, headers=headers, json=payload)
        if payload is True:
            return response.json()
        return response

    def post_request(self,url,auth,headers,payload):
        response = requests.post(url=url,auth=auth, headers=headers, json=payload)
        if payload is True:
            return response
        return response

    def patch_request(self,url,auth,headers,payload):
        response = requests.patch(url=url,auth=auth, headers=headers, json=payload)
        if payload is True:
            return response
        return response

    def delete_request(self,url,auth,headers,payload):
        response = requests.delete(url=url,auth=auth, headers=headers, json=payload)
        if payload is True:
            return response
        return response


