"""
    encrypt_alphavantage_apikey_using_bcrypt.py script:
        1. prompts for 'apikey' obtained from https://www.alphavantage.co

        2. This script encrypts 'apikey' using 'bcyrpt', an essential step in developing secure access to
           alphavantage.com stock apis:
           refer to https://www.makeuseof.com/encrypt-password-in-python-bcrypt/ for details on 'bcrypt'
           and then it stores encrypted key into a file alphavantage_apikey.txt.

           To install bcrypt module using pip issue command: pip install bcrypt

        3. when using functionality provided by alphavantage.co in your python scripts,
           you will load APIKey stored in from a file: alphavantage_apikey_validate.py

        4. You can use tester program, alphavantage_apikey_validate.py which uses ticker symbol search utility provided
           by alphavantage.com to validate API key

        5. To run this script at command prompt type:
           python encrypt_alphavantage_apikey_using_bcrypt.py
"""

import bcrypt
import os



# Define an apikey as a string
apikey = str(input("Enter alphavantage.co APIKEY: "))

# Encode the apikey into a readable utf-8 byte code
apikey = apikey.encode('utf-8')

# Hash the encoded apikey and generate a salt
hashed_apikey = bcrypt.hashpw(apikey, bcrypt.gensalt())

# Print the hashed apikey on the screen
# print(hashed_apikey)

# store the hashedkey into a flat file
with open('alphavantage_apikey.txt', 'wb') as wfh:
    wfh.write(hashed_apikey)

if os.path.exists('alphavantage_apikey.txt'):
    print('APIKEY encrypted and captured successfully')
