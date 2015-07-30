'''
Jordan Clark
2015 - Blitzen.com
'''

import requests
import re
import json
BASE_URL = 'https://api.constantcontact.com/v2/'

class ConstantContactError(Exception):
  def __init__(self, response):
    self.response = response

  def __str__(self):
    return self.response.get('error', 'No error provided')

class IncorrectApiKey(ConstantContactError):
  pass

class ConstantContact(object):
  
  '''
  ConstantContact
  A python 3 wrapper for v2 constant contact api
  Use attributes as urls
  Following url endpoints: https://developer.constantcontact.com/docs/developer-guides/overview-of-api-endpoints.html
  TODO: Implement OAuth2 server flow.  You can get access tokens right now with the requests_ooauthlib library
  Example:
    from constantcontact import ConstantContact
    cc = ConstantContact('api_key', 'access_token')
    cc.account.info() -> Gets account info /account/info
    cc.contacts() -> Gets the endpoint /contacts
    cc.contacts(params={'email': 'example@example.com}) -> Search a specific contact with email_address query
    data = {'fax': '555-555-5555',
            'first_name': 'Jordan',
            'last_name': 'Clark',
            'prefix_name': 'Mr.',
            'home_phone': '555-555-5555',
            'lists': [
              {'id': '1'}
            ]
            'email_addresses':[
              {'email_address': 'exmaple@example.com'},
              {'email_address': 'example@example2.com'}
            ]}
    cc.contacts(method='POST', data=data) -> Posts a new contact to /contacts
    #You can also use a json string (Which is the way constant contact expects the body)
    #Both will work.
    cc.contacts(method='POST', data=json.dumps(data))
    #In order to sub variables, we'll need to have a lookup dictionary.
    variable = {'contactId': 'abcd1234'}
    #We can then use this dictionary to sub contactId with the actual id.
    cc.contacts.contactId(method='PUT', data=data, variable=variable) -> Puts new information to an existing contact /contacts/{contactId}
    cc.contacts.contactId(method='DELETE', variable=variable) -> Deletes contact /contacts/{contactId}
  '''
  def __init__(self, api_key, access_token):
    self.api_key = api_key
    self.access_token = access_token
    self._attr_path = []
    self._request_method = {
      'POST': requests.post,
      'GET': requests.get,
      'PUT': requests.put,
      'DELETE': requests.delete,
    }

  def __call__(self, *args, **kwargs):
    url = BASE_URL + '/'.join(self._attr_path)
    for variable_name, variable_sub in kwargs.get('variable', {}).items():
      url = re.sub(variable_name, variable_sub, url)
    self._attr_path = []
    return self._request(url,
                        kwargs.get('data', {}),
                        kwargs.get('method', 'GET'),
                        kwargs.get('params', {}))

  def __getattr__(self, attr, *args, **kwargs):
    self._attr_path.append(attr)
    return self

  def _request(self, endpoint, data, method='GET', params = {}):
    headers = {'Authorization': 'Bearer {}'.format(self.access_token),
              'Content-Type': 'application/json'}
    params['api_key'] = self.api_key
    if(type(data) == dict):
      data = json.dumps(data)
    try:
      request = self._request_method[method]
    except KeyError:
      raise ConstantContactError('Unknown verb')
    response = request(endpoint, 
                      data=data,
                      params=params, 
                      headers=headers)
    if response.status_code < 400:
      return response.json()
    else:
      response.raise_for_status()
