

import json
from cryptography.fernet import Fernet , InvalidToken
import hashlib
import base64
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import re
import main
# Initialize Firebase Admin SDK with your service account credentials
cred = credentials.Certificate("C:\\Users\\shiva\\Downloads\\shiva-dbd2a-firebase-adminsdk-h2lw3-5baf29f46e.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()





def get_profiles(key):

    Profile_cred = {
       
        'UserID':[],
        'Pass':[],
        'Email':[],
        'Comment':[]
    }

    key= main.generate_key(key)
    f=Fernet(key)
    
    docs = db.collection('Pass_Manager_Profiles').list_documents()
    doc= docs.get()
    print (doc)
    # Extract document IDs
    # for doc in docs:

    #     doc_ref = db.collection('Pass_Manager_Profiles').document(doc.id)
    #     doc = doc_ref.get()
    #     try:
    #         Profile = doc.to_dict()
    #         UserID = f.decrypt(Profile['UserID'].encode()).decode()
    #         Pass = f.decrypt(Profile['Password'].encode()).decode()
    #         Email = f.decrypt(Profile['Email'].encode()).decode()
    #         Comment = f.decrypt(Profile['Comment'].encode()).decode()

    #     except InvalidToken:
    #         UserID = 'None'
    #         Pass = 'None'
    #         Email = 'None'
    #         Comment = 'The Provided key is Invalid for this Profile'
        
    #     except Exception as e:
    #         print(f"Occured error : {e}")
        

    #     Profile_cred['UserID'].append(UserID)
    #     Profile_cred['Pass'].append(Pass)   
    #     Profile_cred['Email'].append(Email)
    #     Profile_cred['Comment'].append(Comment)

    df = pd.DataFrame(Profile_cred)
    df.index = range(1, len(df) + 1)  # Set index starting from 1
    print(df.to_string())

get_profiles('')