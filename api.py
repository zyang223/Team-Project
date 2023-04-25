"""Special Thans to 
Utilizing financialmodelingprep.com for their free-endpoint API
to gather company financials and help and assistance from Hugh Alessi
and instruction from the website: https://financialmodelingprep.com/developer/docs/. """


from urllib.request import urlopen
import json, pprint
import pandas as pd
import os


def get_api_url(requested_data, ticker, apikey):
    """create a url generator to get the url that the company you are looking for"""
    url = "https://financialmodelingprep.com/api/v3/{requested_data}/{ticker}?apikey={apikey}".format(
        requested_data=requested_data, ticker=ticker, apikey=apikey
    )
    print(url)
    return url


def get_data(url):
    """take the latest five year data in json format"""
    response = urlopen(url)
    data = response.read().decode("utf-8")
    json_data = json.loads(data)
    return json_data[:5]


### After getting the data we are going to get the company's finicial Income statement, balance sheet, FCF, stock_price


def get_incomestatement(ticker, apikey):
    """create url return with the latest five year income-statemenet result"""
    url = get_api_url("income-statement", ticker=ticker, apikey=apikey)
    return get_data(url)


def get_balancesheet(ticker, apikey):
    url = get_api_url("balance-sheet-statement", ticker=ticker, apikey=apikey)
    return get_data(url)


def get_cashflow(ticker, apikey):
    url = get_api_url("cash-flow-statement", ticker=ticker, apikey=apikey)
    return get_data(url)


def get_enterprise_value(ticker, apikey):
    url = get_api_url("enterprise-values", ticker=ticker, apikey=apikey)
    return get_data(url)


def get_stockpricetoday(ticker, apikey):
    url = get_api_url("quote-short", ticker=ticker, apikey=apikey)
    return get_data(url)


def download_xlsx(ticker, apikey):
    # print(os.getcwd())
    if os.path.exists(f'Excel/{ticker}.xlsx'):
        print('exist!')
        return

    # Get financial data from API
    income_statement = get_incomestatement(ticker, apikey)
    balance_sheet = get_balancesheet(ticker, apikey)
    cash_flow = get_cashflow(ticker, apikey)
    enterprise_value = get_enterprise_value(ticker, apikey)
    stock_price_today = get_stockpricetoday(ticker, apikey)

    # Convert data to dataframes
    df_income_statement = pd.DataFrame(income_statement)
    df_balance_sheet = pd.DataFrame(balance_sheet)
    df_cash_flow = pd.DataFrame(cash_flow)
    df_enterprise_value = pd.DataFrame(enterprise_value)
    df_stock_price_today = pd.DataFrame(stock_price_today)

    # Save dataframes to Excel
    if not os.path.exists('/Excel'):
        os.makedirs('/Excel')
    
    with pd.ExcelWriter(f"/Excel/{ticker}.xlsx") as writer:
        df_income_statement.to_excel(writer, sheet_name="Income Statement")
        df_balance_sheet.to_excel(writer, sheet_name="Balance Sheet")
        df_cash_flow.to_excel(writer, sheet_name="Cash Flow")
        df_enterprise_value.to_excel(writer, sheet_name="Enterprise Value")
        df_stock_price_today.to_excel(writer, sheet_name="Stock Price Today")



if __name__ == "__main__":
    """quick test, to use run data.py directly"""

    ticker = "ADSK"
    apikey = "3178e48c4517a7c30aa49ccbadef2582"

    # print(f"INCOME STATEMENT SECTION\n")
    # pprint.pprint(get_incomestatement(ticker=ticker, apikey=apikey))

    # print(f"BALANCESHEET SECTION\n")
    # pprint.pprint(get_balancesheet(ticker=ticker, apikey=apikey))

    # print(f"FREE CASH FLOW SECTION\n")
    # pprint.pprint(get_cashflow(ticker=ticker, apikey=apikey))

    # print(f"Enterprise Value  SECTION\n")
    # pprint.pprint(get_enterprise_value(ticker=ticker, apikey=apikey))

    # print(f"Stock-Realtime Price \n")
    # pprint.pprint(get_stockpricetoday(ticker=ticker, apikey=apikey))

    # Get data
    download_xlsx(ticker=ticker, apikey='apikey')



