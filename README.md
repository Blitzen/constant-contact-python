# constant-contact-python

An api sdk for v2 of constant contact api, using python 3.1+

## Installation:

    pip install constant-contact-python

## Examples:
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
    cc.contacts.contactId(method='PUT', data=data, variable=variable) -> Puts new information to an existing contact /contacts/abcd1234
    cc.contacts.contactId(method='DELETE', variable=variable) -> Deletes contact /contacts/abcd1234
