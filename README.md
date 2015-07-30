# constant-contact-python

An api sdk for v2 of constant contact api, using python 3.1+

## Installation:

    pip install constant-contact-python

## Examples:
    from constantcontact import ConstantContact

    #Create the class instance with an api_key and access_token
    cc = ConstantContact('api_key', 'access_token')

    #Gets account info /account/info
    cc.account.info()

    #Gets the endpoint /contacts
    cc.contacts()

    #Search a specific contact with email_address query
    cc.contacts(params={'email': 'example@example.com}) 

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

    #Posts a new contact to /contacts
    cc.contacts(method='POST', data=data) 

    #You can also use a json string (Which is the way constant contact expects the body)
    cc.contacts(method='POST', data=json.dumps(data))

    #In order to sub variables, we'll need to have a lookup dictionary.
    variable = {'contactId': 'abcd1234'}

    #We can then use this dictionary to sub contactId with the actual id.
    #Puts new information to an existing contact /contacts/abcd1234
    cc.contacts.contactId(method='PUT', data=data, variable=variable) 

    #Deletes contact /contacts/abcd1234
    cc.contacts.contactId(method='DELETE', variable=variable) 
