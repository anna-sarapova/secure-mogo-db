import os
from pathlib import Path
from pymongo import MongoClient
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.errors import EncryptionError
from bson import json_util


# Create data for database
data = {"full_name" : ['Kawhi Leonard', 'James Harden', 'Luka Doncic', 'Chris Paul',
 						'Nikola Jokic', 'Stephen Curry', 'Jusuf Nurkic',
 						'Giannis Antetokounmpo', 'Tim Duncan', 'Jrue Holiday',
 						'Kobe Bryant', 'LeBron James', 'Russell Westbrook'],
		"phone_number" : ['(304)482-9056', '(561)845-8405', '(430)991-5950', '(201)383-5477',
						'(779)432-1209', '(252)904-6472', '(270)472-9466',
						'(510)848-6430', '(401)539-9868', '(551)225-1250',
						'(786)258-6269', '(810)595-9505', '(619)206-9941'],
 		"guid" : ['f656cc87-7c76-4a9c-8c8b-7087838e0f2b', 'a12ad1bb-3cf0-4cb8-aec4-5f418aff4551', 'c7a76b18-529f-491a-8a9a-1c4390d0188f', 'b7abac6e-2a38-4177-ad10-ed79aa95516b',
 				'af9b3320-fdba-41a8-9b75-6dde1846c6e9', '964e5eab-dce2-4ec0-a2cb-8d8e5ed895b3', '2319793d-57d6-4f08-a639-bd437b5ff722',
				'674c4966-1985-4228-9b77-0f3a3a3bf58c', 'd98ec1d6-9536-4fc4-9a39-4aa18e59748f', '7ad62f39-7a59-4231-b9e5-ba5688848276',
 				'9e2ed9dd-2268-4f44-bb74-12e8d0aa39fd', '79917fdb-5c68-4df7-84e0-57bbac7b9a46', 'dc0bddc8-e905-4ee7-9a34-4a79b5de6464']}


# Load the master key from 'key_bytes.bin':
key_bin = Path("key_bytes.bin").read_bytes()

# Load the 'person' schema from "json_schema.json":
collection_schema = json_util.loads(Path("json_schema.json").read_text())


# Configure a single, local KMS provider, with the saved key:
kms_providers = {"local": {"key": key_bin}}

# Create a configuration for PyMongo, specifying the local master key,
# the collection used for storing key data, and the json schema specifying
# field encryption:
csfle_opts = AutoEncryptionOpts(
   kms_providers,
   "lab7.__keystore",
   schema_map={"lab7.people": collection_schema},
)

username = 'mongo-user'
password = 'QqldBkX2zzPLoNOL'

# Add a new document to the "people" collection, and then read it back out
# to demonstrate that the ssn field is automatically decrypted by PyMongo:
with MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0.5io68.mongodb.net/Cluster0?retryWrites=true&w=majority", auto_encryption_opts=csfle_opts) as client:
	client.lab7.people.delete_many({})

	for index in range(len(data['full_name'])):
		client.lab7.people.insert_one({
			"full_name": data['full_name'][index],
   			"phone_number": data['phone_number'][index],
			"guid": data['guid'][index]
			})
