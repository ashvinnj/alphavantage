# Alphavantage API Key Encryption Script

This Python script is designed to encrypt and store your Alphavantage API key securely using the bcrypt library. It also includes a second script for interacting with the Alphavantage API using the encrypted API key.

## Getting Started

Before you begin, you will need to obtain an API key from Alphavantage. You can register and claim your API key at the Alphavantage website: [Alphavantage API Key](https://www.alphavantage.co/#about)

### Prerequisites

To run the encryption script, you will need to have the bcrypt library installed. You can install it using pip:


```shell
pip install bcrypt
```
### Usage - Encryption Script

1. Run the encrypt_alphavantage_apikey_using_bcrypt.py script.
2. Enter your Alphavantage API key when prompted.
3. The script will hash and encrypt the API key and store it in a file named apivantage_apikey.txt.
4. This file will be used by the second script for API interactions.

### Usage - API Interaction Script
* The alphavantage_api.py script is designed to interact with the Alphavantage API using the encrypted API key.

* To use this script:
```
alphavantage_api.py [-h] -s SYMBOL
```

### Acknowledgments

* [Professor David Blaikie](https://www.sps.nyu.edu/professional-pathways/faculty/d/961-david-blaikie.html) 
for suggesting the use of the bcrypt encryption module.

* [Alphavantage](https://www.alphavantage.co) for providing financial market data through their APIs.
