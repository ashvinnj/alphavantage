"""
    encrypt_alphavantage_apikey_using_bcrypt.py script takes'apikey'* generated on https://www.alphavantage.co
    Refer to https://www.alphavantage.co/#about
    Alpha Vantage provides realtime and historical financial market data through a set of powerful
    and developer-friendly data APIs and spreadsheets.

    *apikey notes:
    API Key:  Alphavantage requires you to register and use
    an API Key to validate your request.  Please visit the website to claim
    your API Key at the alphavantage website.
    (You can give any email address; the 16-digit key will appear in the web page (
    i.e., you don't have to confirm your email to receive the key)).

    This script will:
    - encrypt the APIKey and store into a file: apivantage_apikey.txt
      the encryption module suggested by Professor David Blaikie
      (https://www.sps.nyu.edu/professional-pathways/faculty/d/961-david-blaikie.html)
       on how to encrypt a password in python using bcyrpt refer to url:
       https://www.makeuseof.com/encrypt-password-in-python-bcrypt/

    - when using functionality provided by alphavantage.co in your python scripts,
      you will load APIKey stored in from a file: apivantage_apikey.txt

    - To install bcrypt using pip: pip install bcrypt
      (note: in pycharm, click on Terminal and type the command: pip install bcrypt)
    - You'll need to run this script once only to generate encrypted APIKey and store it in
      apivantage_apikey.txt
    - Then use the file apivantage_apikey.txt in your scripts to query financial market data using
      modules provided by alphavantage.co
"""


import bcrypt
import os


# Define a apikey as a string
apikey = str(input("Enter alphavantage.co APIKEY: "))

# Encode the apikey into a readable utf-8 byte code
apikey = apikey.encode('utf-8')

# Hash the encoded apikey and generate a salt
hashed_apikey = bcrypt.hashpw(apikey, bcrypt.gensalt())

# Print the hashed apikey on the screen
# print(hashed_apikey)

# store the hashedkey into a flat file
with open ('apivantage_apikey.txt', 'wb') as wfh:
    wfh.write(hashed_apikey)

if os.path.exists('apivantage_apikey.txt'):
    print('APIKEY encrypted and captured sucessfully')
   
    