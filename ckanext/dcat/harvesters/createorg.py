# Description: create harvested organizations from orgfile.txt
# Author: Shanshan Jiang, last modified 14.12.2016

import json
import urllib
import urllib2
import pprint


print "create organizations"

org_dict = {
    'name': 'testagain', 
    'title': 'test again',
    'image_url': ''
}


def create_org(dataset_dict):
    data_string = urllib.quote(json.dumps(dataset_dict))

    # replace with the correct url of CKAN server
    request = urllib2.Request(
    'http://127.0.0.1:5000/api/action/organization_create')

    # replace with the correct APIkey
    request.add_header('Authorization', '765e099f-6d07-48a8-82ba-5a79730a976f') 

    # Make the HTTP request.
    response = urllib2.urlopen(request, data_string)
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())
    assert response_dict['success'] is True

    # package_create returns the created package as its result.
    created_package = response_dict['result']
    pprint.pprint(created_package)

# check if organization exists in the catalogue
def check_org_exist(org_name):
        found = False
        for org in org_list:
            print org
            if org == org_name:
               print "Found the organization : " + org_name
               found = True
               break

	return found


# get the list of organizations from the catalogue
org_url='http://127.0.0.1:5000/api/3/action/organization_list'
orglist=urllib.urlopen(org_url).read()
doc = json.loads(orglist)
org_list = doc["result"]
print 'The list of organizations: '
print org_list

with open('orgfile.txt') as f:
     content = f.read().decode('utf8').splitlines()
print content
for line in content:
    print line
    if line.startswith('org_name:'):
       org_name = line[9:]
       print 'org_name: ' + org_name
       org_dict.update({'name': org_name})

    if line.startswith('url:'):
       org_url = line[4:]
       print 'image url: ' + org_url
       org_dict.update({'image_url': org_url})

    if line.startswith('display_name:'):
       display_name = line[13:]
       print 'display_name: ' + display_name
       org_dict.update({'title': display_name})
       print org_dict
       if check_org_exist(org_name):
          print 'The organization ' + org_name + ' already exists!'
       else:
          create_org(org_dict)

f.close()
