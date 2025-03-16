import os
import json
import main
from pyfiglet import Figlet
import hashlib
import base64
from cryptography.fernet import Fernet
import argparse
import re



parser = argparse.ArgumentParser(description='Password Manager')
subparser= parser.add_subparsers(dest='Command')

#subparser for new profile
New_Profile = subparser.add_parser('add', help='will be used to create a new profile in DB')
New_Profile.add_argument('-u',required=True, help='assigning UserID')
New_Profile.add_argument('-p',required=True, help='assigning Pass')
New_Profile.add_argument('-e', help='assigning Email')
New_Profile.add_argument('-c', help='assigning Comment')
New_Profile.add_argument('-k', help='will be used to pass key/Password')

#subparser for deleting a profile by it's index value
delet = subparser.add_parser('del',help="will be used to delet the Profile by it's index value")
delet.add_argument('-i',required=True, help='used to assign index value of profile')
#delet.add_argument('-k', required=True, help='will be used to pass key/Password')

#subparser for listing Profiles
list_Profiles = subparser.add_parser('list', help='will be used to list all the profiles')
list_Profiles.add_argument('-k',required=True,help='will be used to pass key/Password')

#subparser for Updating profile
Update = subparser.add_parser('update', help='will be used to create a new profile in DB')
Update.add_argument('-i', type=int,help='will be used to assign Profile index value')
Update.add_argument('-u', help='assigning UserID')
Update.add_argument('-p', help='assigning Pass')
Update.add_argument('-e',help='assigning Email')
Update.add_argument('-c', help='assigning Comment')
Update.add_argument('-k', help='will be used to pass key/Password')



args = parser.parse_args()

if args.Command=='add':

    if args.e:
        if main.email_validator(args.e):
            pass
        else:
            print("Invalid email")
    else:
        args.e = 'none'

    args.c= args.c or 'none'
     
    main.NewProfile(args.k, args.u, args.p, args.e, args.c)

elif args.Command=='del':
    main.delete_Profile(args.i)
    
elif args.Command=='list':
    main.get_profiles(args.k)

elif args.Command=='update':
    doc_ref = main.get_doc_ref(args.i)
    Profile = doc_ref.get().to_dict()
    key= main.generate_key(args.k)
    f=Fernet(key)

    if args.e:       
        if main.email_validator(args.e):
            pass
        else:
            print("Invalid email")

        email = args.e
        Profile['Email'] = f.encrypt(email.encode()).decode()

    arg = {
        'u':'UserID',
        'p':'Password',
        'c':"Comment"
    }

    for args, key in arg.items():
        value = getattr(args, key, None)

        if value:
            Profile[key]=f.encrypt(value.encode()).decode()
            print(f'{key} updated' )
    
        doc_ref.update(Profile)
    
    


else:
    print('provide something')

