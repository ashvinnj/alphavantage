"""
The `alphavantage_apikey_validate.py` script will validate your API key (password) to access
     stock APIs provided by alphavantage.co.
Refer to an example of JSON: https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo.

To test this script at the command prompt:
python alphavantage_apikey_validate.py --symbol IBM
"""

import argparse
import json
import os
import requests
import sys


class StockNotFoundException(Exception):
    pass


def get_api_key():
    """Retrieve hashed API key from the file."""
    with open("alphavantage_apikey.txt", "rb") as f:
        hashed_api_key = f.read()

    return hashed_api_key


def get_stock_name_by_symbol_search(in_symbol):
    """Function to get the full stock name based on a symbol using ticker symbol search API."""

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

    print("Total number of items in 'bestMatches' key:", total_items)
    stock_company_name = None
    if total_items > 0:
        for item in json_data.get("bestMatches", []):
            symbol = item.get("1. symbol")
            exact_match = float(item.get("9. matchScore"))
            if symbol == in_symbol and exact_match == 1.0:
                stock_company_name = item.get("2. name")
                break

    return stock_company_name


def enter_stock_symbol_command_line():
    """Retrieves user's input of stock symbol and ensures command line parameters are given."""
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        description='enter stock symbol'
    )

    parser.add_argument('-s', '--symbol', required=True, help='enter stock symbol ')
    args = parser.parse_args()

    return args.symbol


def main():
    """Main function to execute the script."""
    symbol = enter_stock_symbol_command_line().upper()

    stock_company_name = get_stock_name_by_symbol_search(symbol)

    if not stock_company_name:
        raise StockNotFoundException(f'Stock symbol: {symbol} does not exist')

    print(f'Symbol: {symbol} belongs to company: {stock_company_name}')
    print(' ** Test to use alphavantage.co web APIs using your APIKEY is successful **')


if __name__ == '__main__':
    try:
        main()
    except StockNotFoundException as e:
        print(f"Error: {e}")