#!/usr/bin/env python
import urllib
import requests
import json
import pprint

# Make the HTTP request.
response = requests.get('http://demo.ckan.org/api/3/action/group_list',
                           data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = response.json()

# Check the contents of the response.
assert response_dict['success'] is True
result = response_dict['result']
pprint.pprint(result)


# import json
# import urllib.request
# url = 'https://data.boston.gov/api/3/action/datastore_search?resource_id=313e56df-6d77-49d2-9c49-ee411f10cf58&limit=5&q=title:jones'
# fileobj = urllib.request.urlopen(url)
# response_dict = json.loads(fileobj.read())
# print(response_dict)