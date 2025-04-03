# SingleKey Password-Manager

A Password Manager that uses a single key to encrypt and decrypt user's Credentials (username, Password, Email and Comment)

## Features
- Uses a key to Encrypt and Decrypt  Credentials
- Designed for fast and easy usage via the terminal
- Uses firebase Databse to store profiles
- Easy Profile Management

## Installation
Clone the repository and install dependencies.

```sh
git clone https://github.com/username/repository.git
cd repository
pip install -r requirements.txt

```
## Setting up Firebase 

Download Private key as json from Firebase
- Go to firebase
- Create new project
- Go to Project settings
- Select Service Accounts 
- Then Select Python and Click on Generate new private key

Edit 'cred' variable of main file and assign that file's path


## Usage
- **Create a new profile**

```sh
python SingleKey.py add -u <userID> -k <Key> -p <Password> -c <comment> -e <Email> 
```


