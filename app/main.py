import time
from pymongo import MongoClient
from elasticsearch import Elasticsearch, exceptions
from elasticsearch.helpers import scan


# Connect to MongoDB container using name and password of the user
client = MongoClient("mongodb://root:123456@mongodb:27017/logstash?authSource=admin")
db = client["logstash"]
collection = db["db_collection"]


collection.insert_one({
    "name": [
      {
        "first_name": "John",
        "middle_name": "John",
        "last_name": "Doe",
        "client_id": "12345"
    }],
    "address": [
    {
        "postal_code": "ABC123",
        "city": "Cairo",
        "street_adress": "street1"
    }]
})

cursor = collection.find()
for document in cursor:
    print(document)

# # Wait for synchronization
time.sleep(1)

def wait_for_elasticsearch():
    while True:
        try:
            es_client = Elasticsearch("http://elastic:root@elasticsearch:9200")
            if es_client.ping():
                return es_client  # Exit loop if ping successful
        except Exception as e:
            print(f"Waiting for Elasticsearch to start: {e}")
            time.sleep(5)  # Wait for 5 seconds before retrying

es_client = wait_for_elasticsearch()
if not es_client.indices.exists(index="demo_index"):
    try:
        
        es_client.indices.create(index="demo_index")
        start = time.time()
        print("Created index 'demo_index'")
    except exceptions.RequestError as ex:
        if ex.error == 'resource_already_exists_exception':
            pass # Index already exists. Ignore.
        else: # Other exception - raise it
            raise ex
    
search_result = scan(es_client, index='demo_index', query={"query": {"match": {}}})
for hit in search_result:
    print('--------------------------------------------')
    print(hit["_source"])

