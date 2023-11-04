"""
     The `alphavantage_api_validate.py` script will validate your apikey (password) to access
     stock apis provided by alphavantage.co
     refer to example of Json https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo

     to test this script at command prompt:
     python alphavantage_api_validate.py --symbol IBM

"""

import argparse
import json
import os
import requests
import sys


def get_api_key():
    """ retrieve hashed API key from the file """
    with open("alphavantage_apikey.txt", "rb") as f:
        hashed_api_key = f.read()

    return hashed_api_key


def get_stock_name_by_symbol_search(in_symbol):
    """ function to get full stock name based on a symbol using ticker symbol search api """

    retrieved_api_key = None
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
    # Get the total number of items in the "bestMatches" array
    total_items = len(json_data.get("bestMatches", []))

    stock_company_name = None
    print("Total number of items in 'bestMatches' key:", total_items)

    if total_items > 0:
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
