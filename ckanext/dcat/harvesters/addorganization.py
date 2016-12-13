# Description: get harvested organizations from data.norge.no and save to orgfile.txt
# Author: Shanshan Jiang, last modified 13.12.2016

import json
import urllib
print "test"
url='http://78.91.98.234:5000/api/3/action/organization_list'
content=urllib.urlopen(url).read()

orgfile = open('orgfile.txt', 'w')

def _get_organizations(content):
    # Todo: Test that this works before using it in other methods!!
    doc = json.loads(content)
    datasets = doc["result"]
    print datasets
    for dataset in datasets:
        print dataset
        orgfile.write('org_name:' + str(dataset) + '\n')
        showorgurl='http://78.91.98.234:5000/api/3/action/organization_show?id=' + dataset
        _get_org_details(showorgurl)
        print '**************'

def _get_org_details(url):
    content=urllib.urlopen(url).read()
    doc = json.loads(content)
    datasets = doc["result"]
    image_url = datasets.get('image_url')
    print image_url
    orgfile.write('url:' + str(image_url) + '\n')
    #orgfile.write('display_name:' + datasets.get('display_name').get('value') + '\n')
    orgfile.write('display_name:' + datasets.get('display_name').encode('utf8') + '\n')
    

_get_organizations(content)
orgfile.close()
