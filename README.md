# SingleKey Password Manager

A Password Manager that uses a **single key** to encrypt and decrypt user's Credentials (Username, Password, Email and Comment)

## Features
- Uses a key to encrypt and decrypt  credentials
- Designed for fast and easy usage via the terminal
- Uses Firebase Databse to store profiles
- Easy profile Management

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
- Click Generate new private key under the Python section

Edit the 'cred' variable in the main.py file and set the path to your Firebase private key.

## Dependencies & Requirements
- os
- re
- json
- pandas
- base64
- hashlib
- argparse
- cryptography
- firebase-admin


## Usage
- **Create a new profile**
    # Comment and Emails are optional
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

## Glossary

- **Firebase**: A cloud-based database used to store and manage profiles securely.
- **Profile**: A profile contains a user's credentials, including username, password, email, and comments.
- **Profile Index**: A unique number assigned to each stored profile, used for identification when updating or deleting profiles.
- **Key**: A secret passphrase used to encrypt and decrypt stored credentials.


## How It Works

- Encryption: Every profile is encrypted using the key before storing it in Firebase.
- Decryption: The same key is required to retrieve and decrypt profile information.
- Profile Management: Users can add, delete, update, and list their stored credentials.
- Secure Storage: Firebase stores encrypted credentials, ensuring only authorized users can access them.

## Contributing
Pull requests are welcome! If you have suggestions or improvements, feel free to contribute.