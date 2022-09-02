import json

a='{"Name":"Nasif", "Education":"CSE"}'
jsload=json.loads(a)
print(jsload["Name"]) #Reading a index data from Json
print(jsload["Education"])

#Json Dump

Details={
    "Name":"Mr K",
    "Age": "30",
    "Adress":"DOHS"
}
dump=json.dumps(Details) #Dumping Json Data
print(dump)
