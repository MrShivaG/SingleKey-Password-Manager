import json
from cryptography.fernet import Fernet , InvalidToken
import hashlib
import base64
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import re
# Initialize Firebase Admin SDK with your service account credentials
cred = credentials.Certificate("C:\\Users\\shiva\\Downloads\\shiva-dbd2a-firebase-adminsdk-h2lw3-5baf29f46e.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()



# Create a new Profile_cred
def NewProfile(key, userID, Pass, Email='none', Comment='none'):
    key= generate_key(key)

    f=Fernet(key)
    try:
        userID= f.encrypt(userID.encode())
        Pass= f.encrypt(Pass.encode())
        Email= f.encrypt(Email.encode())
        Comment= f.encrypt(Comment.encode())
    
        #Creating a new document in DB
        def create_document(collection, doc_id, data):
            doc_ref = db.collection(collection).document(doc_id)
            doc_ref.set(data)
            print(f"Document with ID {doc_id} created.")
    
        #getting only collection's document as list
        docs = db.collection('Pass_Manager_Profiles').list_documents()
        document_ids = [doc.id for doc in docs]
    
        #creating new Profile_cred
        New_Profile = {'UserID':userID.decode(),'Password':Pass.decode(),'Email':Email.decode(),'Comment':Comment.decode()}
    
        create_document("Pass_Manager_Profiles", f"Profile_{len(document_ids)+1}", New_Profile)
    except InvalidToken:
        print("enter valid Key")

    except Exception as e:
        print(f"occured error : {e}")




def delete_Profile(ProfileID):

    docs = db.collection('Pass_Manager_Profiles').list_documents()
    document_ids = [doc.id for doc in docs]

    doc_id = document_ids[ProfileID-1]
    doc_ref = db.collection('Pass_Manager_Profiles').document(doc_id)
    doc_ref.delete()
    print(f"Document with ID {doc_id} deleted.")


def get_profiles(key):

    Profile_cred = {
       
        'UserID':[],
        'Pass':[],
        'Email':[],
        'Comment':[]
    }

    key= generate_key(key)
    f=Fernet(key)
    
    docs = db.collection('Pass_Manager_Profiles').list_documents()

    # Extract document IDs
    for doc in docs:

        doc_ref = db.collection('Pass_Manager_Profiles').document(doc.id)
        doc = doc_ref.get()
        try:
            Profile = doc.to_dict()
            UserID = f.decrypt(Profile['UserID'].encode()).decode()
            Pass = f.decrypt(Profile['Password'].encode()).decode()
            Email = f.decrypt(Profile['Email'].encode()).decode()
            Comment = f.decrypt(Profile['Comment'].encode()).decode()

        except InvalidToken:
            UserID = 'None'
            Pass = 'None'
            Email = 'None'
            Comment = 'The Provided key is Invalid for this Profile'
        
        except Exception as e:
            print(f"Occured error : {e}")
        

        Profile_cred['UserID'].append(UserID)
        Profile_cred['Pass'].append(Pass)   
        Profile_cred['Email'].append(Email)
        Profile_cred['Comment'].append(Comment)

    df = pd.DataFrame(Profile_cred)
    df.index = range(1, len(df) + 1)  # Set index starting from 1
    print(df.to_string())




#getting Document path by Index value
def get_doc_ref(ProfileID):
    docs = db.collection('Pass_Manager_Profiles').list_documents()
    document_ids = [doc.id for doc in docs]
    doc_id = document_ids[ProfileID-1]
    doc_ref = db.collection('Pass_Manager_Profiles').document(doc_id)

    return doc_ref

#  generating a key by raw string
def generate_key(key):
    Key= hashlib.sha256(key.encode()).digest()
    Key = base64.urlsafe_b64encode(Key)
    return Key

#  Validating email structure
def email_validator(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))




def decrypt_creds(key):
    try:
        with open("SingleKey.json",'r') as file:
            data = json.load(file)
        
        for profile in data['Profiles']:
            print(profile)
    except InvalidToken:
        print('Invalid Key')
    except Exception as e:
        print(f'eroor occured {e}')


key = 'mySecretpass'
# key= hashlib.sha256(string.encode()).digest()
# key = base64.urlsafe_b64encode(key)




# docs = db.collection('Pass_Manager_Profiles').list_documents()
# document_ids = [doc.id for doc in docs]
# print(document_ids)



# key = Fernet.generate_key()
# NewProfile("hel",'ddkkk','sds@','rrtfdferfds',key)
# def read_document(collection, doc_id):
#     doc_ref = db.collection(collection).document(doc_id)
#     doc = doc_ref.get()
#     if doc.exists:
#         return doc.to_dict()
#     else:
#         print(f"Document with ID {doc_id} not found.")





# read_document('Pass_Manager_Profiles', 'Profles_1')
#get_profiles(key)
#g = read_for_update(2)
#print(g.to_dict())
