# Description: update organizations of harvested datasets from data.norge.no to their original published organization instead of harvester organization
# Author: Shanshan Jiang, last modified 13.12.2016

import json
import urllib
import urllib2
import pprint

print "update organizations for a dataset"
url='http://127.0.0.1:5000/api/3/action/package_list'
#url='http://78.91.98.234:5000/api/3/action/organization_list'
#content=urllib.urlopen(url).read()

#orgfile = open('orgfile.txt', 'w')



def get_datasets(url):
    content=urllib.urlopen(url).read()
    # Todo: Test that this works before using it in other methods!!
    doc = json.loads(content)
    datasets = doc["result"]
    print datasets
    for dataset in datasets:
        print dataset
        #orgfile.write('org_name:' + str(dataset) + '\n')
        showorgurl='http://127.0.0.1:5000/api/3/action/package_show?id=' + dataset
        dataset_dict = get_package_org(showorgurl)
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        

def get_package_org(url):
    content=urllib.urlopen(url).read()
    doc = json.loads(content)
    dataset_dict = doc["result"]
    print dataset_dict
    print "====================================="
    org_name = dataset_dict.get('organization').get('title')
    print "organization: " + org_name
    extras = dataset_dict.get('extras')
    #print extras
    if extras is not None:
    	for item in extras:
	    if item.get('key') == 'dcat_publisher_name':
           	publisher_name = item.get('value')
           	print "publisher name: " + publisher_name
                check_and_update_org(publisher_name, org_name, dataset_dict)
    

def check_and_update_org(publisher_name, org_name, dataset_dict):
    found = False
    if publisher_name != org_name:
	print publisher_name + " is not the same as  " + org_name
        org_url='http://127.0.0.1:5000/api/3/action/organization_list'
        orglist=urllib.urlopen(org_url).read()
        doc = json.loads(orglist)
        datasets = doc["result"]
        print datasets
        for dataset in datasets:
            print dataset
            showorgurl='http://127.0.0.1:5000/api/3/action/organization_show?id=' + dataset
            orgcontent=urllib.urlopen(showorgurl).read()
            orgdoc = json.loads(orgcontent)
    	    orgdatasets = orgdoc["result"]
            org_title = orgdatasets.get('title')
            print "organization title: " + org_title
            if org_title == publisher_name :
	       print "Find the organization for " + org_title
               org_id = orgdatasets.get('id')
               print "the organization id is : " + org_id
               found = True
               break
    # update organization id
    if found:
       print "owner org id: " + dataset_dict.get('owner_org')
       dataset_dict.update({'owner_org': org_id})
       print "updated org id is --------> " + dataset_dict.get('owner_org')
       update_dataset(dataset_dict)

def update_dataset(dataset_dict):
    data_string = urllib.quote(json.dumps(dataset_dict))
    print "update dataset: " + data_string
    print "**************************************************************"

    # replace with the correct url of CKAN server
    request = urllib2.Request(
    'http://127.0.0.1:5000/api/action/package_update')
    # 'http://78.91.98.234:5000/api/action/organization_update')

    # replace with the correct APIkey
    request.add_header('Authorization', '765e099f-6d07-48a8-82ba-5a79730a976f')  #for local
    #request.add_header('Authorization', '93f9960d-daff-4d67-adb8-e75f24189c44')    #for sintef server

    # Make the HTTP request.
    response = urllib2.urlopen(request, data_string)
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())
    assert response_dict['success'] is True

    # package_create returns the created package as its result.
    updated_package = response_dict['result']
    pprint.pprint(updated_package)
 

get_datasets(url)
#orgfile.close()

