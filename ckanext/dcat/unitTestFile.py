import unittest
import converters
from ckanext.harvest.model import HarvestObject, HarvestObjectExtra, HarvestJob
from ckanext.dcat.harvesters.base import DCATHarvester
import json

class TestMethods (unittest.TestCase):
    def test_DataNorgeConverter(self):
        dcat_format={"title":"Kvalitet p\u00e5 nett - resultatliste 2010","description":[{"language":"nb","value":"\u003Cp\u003EResultatliste fra kvalitetsvurderingen av n\u00e6r 700 offentlige nettsteder 2010. Vurderingen er utf\u00f8rt av Direktoratet for forvaltning og IKT. Detaljerte vurderinger for hvert enkelt nettsted finnes i eget datasett. Se http:\/\/kvalitet.difi.no for mer informasjon om vurderingsarbeidet.\u003C\/p\u003E"}],"landingPage":"http:\/\/kvalitet.difi.no","issued":"2015-03-19","modified":"2016-09-23T14:11","language":["NOR"],"publisher":{"name":"Direktoratet for forvaltning og IKT","mbox":"anr@difi.no"},"keyword":["Forvaltning og offentlig sektor"],"distribution":[{"title":"API","description":[{"language":"nb","value":"Kvalitet p\u00e5 nett - Resultatliste 2010"}],"format":"API","downloadURL":"http:\/\/hotell.difi.no\/download\/difi\/kvalitet\/oversikt2010?download","accessURL":"http:\/\/hotell.difi.no\/?dataset=difi\/kvalitet\/oversikt2010","webserviceURL":"http:\/\/hotell.difi.no\/application.wadl","license":"http:\/\/data.norge.no\/nlod\/"}]}
        ckan_format={'tags': [{'name': 'Forvaltning_og_offentlig_sektor'}], 'url': 'http:\\/\\/kvalitet.difi.no', 'notes': '\\u003Cp\\u003EResultatliste fra kvalitetsvurderingen av n\\u00e6r 700 offentlige nettsteder 2010. Vurderingen er utf\\u00f8rt av Direktoratet for forvaltning og IKT. Detaljerte vurderinger for hvert enkelt nettsted finnes i eget datasett. Se http:\\/\\/kvalitet.difi.no for mer informasjon om vurderingsarbeidet.\\u003C\\/p\\u003E', 'title': 'Kvalitet p\\u00e5 nett - resultatliste 2010', 'extras': [{'value': '2015-03-19', 'key': 'dcat_issued'}, {'value': '2016-09-23T14:11', 'key': 'dcat_modified'}, {'value': None, 'key': 'guid'}, {'value': 'Direktoratet for forvaltning og IKT', 'key': 'dcat_publisher_name'}, {'value': 'anr@difi.no', 'key': 'dcat_publisher_email'}, {'value': 'NOR', 'key': 'language'}, {'value': '[]', 'key': 'metadata_provenance'}], 'resources': [{'url': 'http:\\/\\/hotell.difi.no\\/download\\/difi\\/kvalitet\\/oversikt2010?download', 'name': 'API', 'format': 'API'}]}
        self.assertEqual(ckan_format,converters.dcat_to_ckan(dcat_format))

    def test_GeoNorgeConverter(self):
        geonorge_format={"Title":"Kystverket - Nedlasting","Abstract":"Kystverket tilbyr nedlasting av sine geodata. Det skal vaere enkelt aa bruke Kystverkets data i sitt arbeid og Kystverket tilbyr derfor nedlasting av data i tillegg til data som tjenester. Man kan velge datasett, gjoere geografisk utvalg, velge koordiantsystem og laste ned data i ulike formater. Formatene som tilbys er pr. august 2016: ESRI shape, ESRI file geodatabase, SOSI, KML, GML, GeoJSON.","Type":"software","Theme":"Annen","Organization":"Kystverket","OrganizationLogo":"https://register.geonorge.no/data/organizations/874783242_Kystverket_liten.png","ThumbnailUrl":"https://editor.geonorge.no/thumbnails/57749564-7525-433a-aded-349056b1a91a_20160823134118_nedlasting.JPG","DistributionUrl":"Http://nedlasting.kystverket.no","DistributionProtocol":"WWW:LINK-1.0-http--link","ShowDetailsUrl":"https://kartkatalog.geonorge.no/metadata/uuid/57749564-7525-433a-aded-349056b1a91a","OrganizationUrl":"https://kartkatalog.geonorge.no/metadata/kystverket","IsOpenData":False,"IsDokData":False,"AccessConstraint":"otherRestrictions","OtherConstraintsAccess":"no restrictions","DataAccess":"aapne data"}
        ckan_format={'tags': [{'name': 'Annen'}], 'url': 'https://kartkatalog.geonorge.no/metadata/uuid/57749564-7525-433a-aded-349056b1a91a', 'notes': 'Kystverket tilbyr nedlasting av sine geodata. Det skal vaere enkelt aa bruke Kystverkets data i sitt arbeid og Kystverket tilbyr derfor nedlasting av data i tillegg til data som tjenester. Man kan velge datasett, gjoere geografisk utvalg, velge koordiantsystem og laste ned data i ulike formater. Formatene som tilbys er pr. august 2016: ESRI shape, ESRI file geodatabase, SOSI, KML, GML, GeoJSON.', 'title': 'Kystverket - Nedlasting', 'extras': [{'value': 'Kystverket', 'key': 'Organisasjon'}, {'value': 'https://kartkatalog.geonorge.no/metadata/kystverket', 'key': 'Nettside til organisasjon'}, {'value': 'software', 'key': 'Type'}, {'value': '[]', 'key': 'metadata_provenance'}], 'resources': [{'url': 'Http://nedlasting.kystverket.no', 'format': 'software', 'name': 'Kystverket - Nedlasting', 'description': 'Kystverket tilbyr nedlasting av sine geodata. Det skal vaere enkelt aa bruke Kystverkets data i sitt arbeid og Kystverket tilbyr derfor nedlasting av data i tillegg til data som tjenester. Man kan velge datasett, gjoere geografisk utvalg, velge koordiantsystem og laste ned data i ulike formater. Formatene som tilbys er pr. august 2016: ESRI shape, ESRI file geodatabase, SOSI, KML, GML, GeoJSON.'}]}
        self.assertEqual(ckan_format,converters.geonorge_to_CKANpackage(geonorge_format))

    def test_provenance(self):
		id="http://data.norge.no/node/512"
		source_json = {
			"title": "NOBIL - ladestasjoner for elbiler",
			"description": [
				{
					"language": "nb",
					"value": "<p>NOBIL er etablert for formidling av informasjon om ladestasjoner for elbiler. Den har et detaljert innhold om ladestasjonene og formidler sanntidsdata. Alt er fritt tilgjengelig via et API.</p><p>Et ladepunkt er en reservert parkeringsplass med lademulighet for ladbare kjoeretoey. Paa et ladepunkt kan det vaere mer enn en kontakt, men bare plass til et kjoeretoey av gangen. En ladestasjon er et sted for det er ett eller flere ladepunkt.</p>"
				}
			],
			"landingPage": "http://nobil.no",
			"issued": "2013-10-08",
			"modified": "2016-10-07T11:34",
			"language": [
				"NOR"
			],
			"publisher": {
				"name": "Enova SF",
				"mbox": "per.dybvik@enova.no"
			},
			"keyword": [
				"Energi",
				"Miljoe",
				"Transport"
			],
			"distribution": [
				{
					"title": "JSON",
					"description": [
						{
							"language": "nb",
							"value": "Nettside som med informasjon om API-et"
						}
					],
					"format": "JSON",
					"downloadURL": "null",
					"accessURL": "http://nobil.no",
					"webserviceURL": "null",
					"license": "http://creativecommons.org/licenses/by/3.0/no/"
				}
			]
		}
		job= HarvestJob(url="http://data.norge.no/api/dcat/data.json", title="TestHarvest")
		obj = HarvestObject(guid="http://data.norge.no/node/512",content=source_json, source=job)
		initial={"activity_ocurred": "2016-10-21T12:25:09.091774", "harvest_source_title": "TestHarvest", "activity": "initial_harvest", "harvest_sorce_url": "http://data.norge.no/api/dcat/data.json", "excluded_resources": [], "harvested_guid": "http://data.norge.no/node/512"}

		#Testing get_metadata:provenance_for_just_this_harvest
		dcatharvest=DCATHarvester()
		provenance=dcatharvest.get_metadata_provenance_for_just_this_harvest(obj,"initial_harvest",[])

		self.assertEqual(provenance["harvest_source_title"], initial["harvest_source_title"])
		self.assertEqual(provenance["activity"], initial["activity"])
		self.assertEqual(provenance["harvest_sorce_url"], initial["harvest_sorce_url"])
		self.assertEqual(provenance["harvested_guid"], initial["harvested_guid"])
		self.assertEqual(provenance["excluded_resources"],initial["excluded_resources"])

		#Testing append_provenance_data
		val=[initial]
		val_string=json.dumps(val)
		package_dict={
			"extras":[
				{"key":"metadata_provenance","value":val_string}

			]
		}


		update={"activity_ocurred": "2016-10-21T12:25:09.091774", "harvest_source_title": "TestHarvest", "activity": "update", "harvest_sorce_url": "http://data.norge.no/api/dcat/data.json", "excluded_resources": [], "harvested_guid": "http://data.norge.no/node/512"}
		appended=[initial,update]
		package_correct ={
			"extras": [
				{"key": "metadata_provenance", "value": json.dumps(appended)}

			]
		}

		test_package_result=dcatharvest.append_provenance_data(package_dict,obj,"update",[])
		test_provenance=json.loads(test_package_result["extras"][0]["value"])

		correct_provenance=json.loads(package_correct["extras"][0]["value"])

		self.assertEqual(len(correct_provenance),len(test_provenance))


if __name__ == '__main__':
    unittest.main()