# SingleKey Password-Manager

A Password Manager that uses Single key to encrypt and decrypt user's Credentials (username, Password, Email and Comment)

## Features
- Uses a key to Encrypt/Decrypt  Credentials
- Made for CLI
- Uses DB (firebase) to store profiles

## Installation
Clone the repository and install dependencies.

```sh
git clone https://github.com/username/repository.git
cd repository
pip install -r requirements.txt

```
## Setup Firebase 

Download Private key as json from Firebase
- Go to firebase
- Create new project
- Go to Project settings
- Select Service Accounts 
- Then Select Python and Click on Generate new private key

Edit 'cred' variable of main file and assign that file's path


## uses
```sh
- to create a new profile
python SingleKey.py add -u <userID> -k <Key> -p <Password> -c <commant> -e <Email> 
# comment and email is optional


