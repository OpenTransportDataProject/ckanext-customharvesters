# ckanext-customharvesters

This extension is a modification of the already existing extension that can be found here [https://github.com/ckan/ckanext-dcat](https://github.com/ckan/ckanext-dcat). The extension provides functionality for logging data about harvest activity done on each dataset, and functionality that checks if the dataset already exists based on its resources. It alse extends the original extension by adding two custom harvesters which are adapted for harvesting data from [http://data.norge.no](http://data.norge.no)and [http://geonorge.no](http://geonorge.no).


## Contents

- [Installation](#installation)
- [How to harvest data](#how-to-harvest-data)



## Installation

1.  Install ckanext-harvest ([https://github.com/ckan/ckanext-harvest#installation](https://github.com/ckan/ckanext-harvest#installation)) 

2.  Install the extension on your virtualenv:

        (pyenv) $ pip install -e git+https://github.com/OpenTransportDataProject/ckanext-customharvesters.git#egg=ckanext-customharvesters

3.  Install the extension requirements:

        (pyenv) $ cd /usr/lib/ckan/default/src/
        (pyenv) $ pip install -r ckanext-customharvesters/requirements.txt

4.  Enable the required plugins in your ini file:

        ckan.plugins = dcat dcat_rdf_harvester dcat_json_interface geonorgeHarvester datanorgeHarvester

5.  Restart apache:

        sudo service apache2 restart

## How to harvest data

1.  Navigate to the harvester interface by going to http://yourCKANIP/harvest

2.  Press the ”Add Harvest Source” button and fill in the necessary information about your harvest source.  
    -If you want to add a general tag to all datasets(for example ”OTD”), add the following line in the configurationfield:
        
        "default_tags": [{"name": "OTD"}]
      
    -Example URL for data.norge.no: [http://data.norge.no/api/dcat/data.json](http://data.norge.no/api/dcat/data.json)
    
    -Example URL for geonorge.no: [https://kartkatalog.geonorge.no/api/search?text=kystverket&limit=10000000](https://kartkatalog.geonorge.no/api/search?text=kystverket&limit=10000000)
    
    
    Remember to hit save when you are done

3.  Choose the harvest source you created from the list found at http://yourCKANIP/harvest

4.  Press the ”Admin”-button.  (you must be logged in as a sysadmin user)

5.  Press  the  ”Reharvest”-button,  you have  now  created  a new  harvest  job.

6.  Login to your CKAN server through SSH.(How to do this depends on your own setup)

7.  Activate your CKAN virtual environment(How to do this may vary, depending on your CKAN installation):

        /usr/lib/ckan/default/bin/activate

  
8.  Run the gather_consumer-command:

        (pyenv) $ paster --plugin=ckanext-harvest harvester gather_consumer --config=/etc/ckan/default/production.ini

9.  On another terminal, run the fetch_consumer-command:

        (pyenv) $ paster --plugin=ckanext-harvest harvester fetch_consumer --config=/etc/ckan/default/production.ini

10. Finally, on a third console, run the run-command to start any pending harvesting jobs:

        (pyenv) $ paster --plugin=ckanext-harvest harvester run --config=/etc/ckan/default/production.ini
