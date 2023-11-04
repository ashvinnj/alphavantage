 
# Alphavantage API Key Encryption and Validation Scripts

This project includes two Python scripts to help you secure and use your Alphavantage API key for accessing stock APIs
provided by Alphavantage.co. The first script, `encrypt_alphavantage_apikey_using_bcrypt.py`, encrypts your API key, 
and the second script, `alphavantage_api_validate.py`, validates the API key.

## Prerequisites

Before using these scripts, make sure you have the following requirements:

1. Python installed on your system.

2. The `bcrypt` module installed. You can install it using pip with the following command:

   ```
   pip install bcrypt
   
### 'encrypt_alphavantage_apikey_using_bcrypt.py'

### overview:
This script encrypts your Alphavantage API key using the bcrypt hashing algorithm, 
which is essential for secure access to Alphavantage.com stock APIs. After encryption, it stores 
the API key securely in a file named alphavantage_apikey.txt

1. Run the script using the following command:
   ```
   python encrypt_alphavantage_apikey_using_bcrypt.py

2. You will be prompted to enter your Alphavantage API key.

The script will encrypt your API key using bcrypt and store the encrypted key 
in the alphavantage_apikey.txt file.

### alphavantage_api_validate.py Script

### Overview

This script validates your Alphavantage API key for accessing stock APIs provided by 
Alphavantage.co. It uses Alphavantage's ticker symbol search API to check 
the validity of the API key.

Examples (click for JSON output)
   ```
   https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo
   ```

### Usage
1. Run the script at the command prompt to validate your API key for a specific stock symbol 
   (replace SYMBOL with the desired stock symbol):
   ```
   python alphavantage_api_validate.py --symbol SYMBOL

2. The script will retrieve the encrypted API key from the alphavantage_apikey.txt file and send a request to 
   Alphavantage's API to check if the provided API key is valid for the given stock symbol.

3. If the API key is valid for the provided stock symbol, 
   the script will display the company name associated with the symbol and a success message.

4. If the API key is not valid or the stock symbol does not exist, 
    an error message will be displayed, and the script will exit with a non-zero status code.