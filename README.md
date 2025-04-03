# SingleKey Password-Manager

A Password Manager that uses a **single key** to encrypt and decrypt user's Credentials (username, Password, Email and Comment)

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

## Dependencies & Requirements
- os
- json
- main
- Figlet
- hashlib
- base64
- cryptography
- argparse
- re
- firebase-admin
- pandas


## Usage
- **Create a new profile**

```sh
python SingleKey.py add -u <userID> -k <Key> -p <Password> -c <comment> -e <Email> 
```
- **Delete a profile by index**
```sh
python SingleKey.py del -i <Profile_Index>
```
- **List all profiles**
```sh
python SingleKey.py list -k <Key>
```

- **Update an existing profile**
```sh
python SingleKey.py update -i <Profile_Index> -u <New_UserID> -k <Key>
python SingleKey.py update -i <Profile_Index> -p <New_Password> -k <Key>
python SingleKey.py update -i <Profile_Index> -c <New_Comment> -k <Key>
python SingleKey.py update -i <Profile_Index> -e <New_Email> -k <Key>

```

## How It Works

- Encryption: Every profile is encrypted using the key before storing it in Firebase.
- Decryption: The same key is required to retrieve and decrypt profile information.
- Profile Management: Users can add, delete, update, and list their stored credentials.
- Secure Storage: Firebase stores encrypted credentials, ensuring only authorized users can access them.

## Contributing
Pull requests are welcome! If you have suggestions or improvements, feel free to contribute.