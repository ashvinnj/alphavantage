"""
     The `alphavantage_api.py` script will validate your apikey generated on alphavantage.co
     The purpose of this script to validate Alphavantage APIKEY.

     provide the APIKEY when running the script to validate as a test before
     exploring the rest of the APIs from alphavantage.co

     to test this script at command prompt:
     python alphavantage_api.py --symbol IBM

"""

import argparse
import bcrypt
import json
import os
import requests
import sys


def get_api_key():
    # Read the hashed API key from the file
    with open("apivantage_apikey.txt", "rb") as f:
        hashed_api_key = f.read()

    # Input the API key to check
    api_key_to_check = str(input("Enter your API Key: ")).encode('utf-8')

    # Use bcrypt to verify the API key
    if bcrypt.checkpw(api_key_to_check, hashed_api_key):
        print("Congratulations! APIKEY is valid")
        return api_key_to_check.decode('utf-8')
    else:
        print("API key is invalid")
        return None


def get_stock_name_by_symbol_search(in_symbol):
    """ function fids Finds Stock's company name after providing APIKEY """

    try:
        retrieved_api_key = get_api_key()
        if not retrieved_api_key:
            raise Exception(" unable to validate APIKEY ")
    except Exception as e:
        print("Error:", str(e))

    params = {
        'function': 'SYMBOL_SEARCH',
        'keywords': in_symbol,
        'apikey': retrieved_api_key
    }

    base_url = 'https://www.alphavantage.co/query'

    try:
        response = requests.get(base_url, params=params)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    json_data = json.loads(response.text)

    stock_company_name = None
    for item in json_data.get("bestMatches", []):
        symbol = item.get("1. symbol")
        exact_match = float(item.get("9. matchScore"))
        if symbol == in_symbol and exact_match == 1.0:
            stock_company_name = item.get("2. name")
            break

    return stock_company_name


def enter_stock_symbol_command_line():
    """ retrieves user's input of stock symbol and ensures command line parameters given"""
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        description='enter stock symbol'
    )

    parser.add_argument('-s', '--symbol', required=True, help='enter stock symbol ')
    args = parser.parse_args()

    return args.symbol


def main():

    symbol = enter_stock_symbol_command_line().upper()

    stock_company_name = get_stock_name_by_symbol_search(symbol)

    if not stock_company_name:
        print(f'stock symbol: {symbol} does not exists ')
        sys.exit(1)

    print(f'Symbol: {symbol} belongs to company: {stock_company_name}')
    print(' ** Test to use alphavantage.co web APIs using your APIKEY is successful **')


if __name__ == '__main__':
    main()
