# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:56:04 2019

@author: rahul
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("./synduser.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


doc_ref = db.collection(u'users').document(u"barath G")
doc_ref.set({
    u'first': u'CEO OF GOOGLE',
    u'last': u'CEO OF ORGIN',
    u'born': 1999
})
users_ref = db.collection(u'users')
docs = users_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

ram = u'Alan4'
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': ram,
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})




from pymongo import MongoClient
client = MongoClient("mongodb+srv://endgame:endgame22@asgard-pl70h.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database("syndicate")
reports = db.reports
reports.count_documents({})

new_complaint = {
    "fields":{
      "time_stamp": "2014-12-20T21",
        "name": "hydra maxx",
        "branch": "shield",
        "description":"I went  I freeze your balls xD",
	"domain":"current account",
	"status":"approved"    
},
    "model": "resources.people",
    "token_no": 6
} 
reports.insert_many(".\Users\rahul\Downloads\reports.json")

complaint_updates = {"name":"Thanos"}
reports.update_one({"token_no":4},{"$set":complaint_updates})


import os
os.chdir("C:\\Users\\rahul\\Downloads")
filename = "reports.json"
cmd = "mongoimport --host asgard-shard-00-01-pl70h.mongodb.net:27017 --db syndicate --type json --file " + reports.json+ " --jsonArray --authenticationDatabase admin --ssl --username endgame --password endgame22"
os.system(cmd)


list1 = list(reports.find())




















config ={
   "apiKey": "AIzaSyBv1NhrKqHeYyQMEMTQ_Jook00TcCmk7A8",
    "authDomain": "synduser-aa827.firebaseapp.com",
    "databaseURL": "https://synduser-aa827.firebaseio.com",
    "projectId": "synduser-aa827",
    "storageBucket": "synduser-aa827.appspot.com",
    "messagingSenderId": "663413281362",
    "serviceAccount": "serviceAccountCredentials.json"
}
firebase=pyrebase.initialize_app(config)
db = firebase.database()

#ACCESSING FIRESTORE
storage = firebase.storage()
datadir = 'D:\Projects\Syndicate\Audio'

#DOWNLOADING ALL FILES

#all_files = str(storage.child("Audio/").list_files())
storage.child("Audio/new_audio.3gp").download("final.3gp")