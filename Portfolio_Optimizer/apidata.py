'''
Module: Data API Functions
Created On: 2019-07-05              Last Modified: 2019-07-05
**************************************************************************
    **READ ME**

    [Description]
    Module Contains Custom Functions For The Below List of Registerd APIs and
    Returning Specific Financial Data For The Specified Stock Symbol/Company

    [Finance APIs]
    SEC Edgar   Security Exchange Commission - Company Filings & Financial Disclosures
                    -   Consolidated Financial Statements (JSON)
                    -   Performance Ratios
                    -   Insider Trades

    Quandl      Stock Performance Data - Time Series Data
                    -   Open, Low, High, Close, Volume, Ex-Dividend, Splits


'''
import quandl as ql


def timeseries_stock_data(symbol, verbose=False):
    '''
    [params]
        -   symbol:     <str> company stock ticker symbol
        -   verbose:    <bool> displays additional logging detail

    [return]
        -   output:     <DataFrame> containing 5 years of weekly price data
                            -   Open, Low, High, Close, Volume
    '''
    # <Define> DataFrame Column Headers
    col_headers = [
        'Open',
        'High',
        'Low',
        'Close',
        'Volume',
    ]

    # <Set> API Query Parameters
    query_params = {
        'symbol': symbol.upper(),
        'start_date': "2014-01-01",
        "end_date": "2019-01-01",
        "collapse": "monthly",
        "data_type": "pandas",
    }

    try:
        # User Quandl Get to Query API
        stock_returns = ql.get(
            f"WIKI/{query_params['symbol']}",
            start_date=query_params['start_date'],
            end_date=query_params['end_date'],
            colapse=query_params['collapse'],
            returns=query_params['data_type'],
            authtoken=quandl_api_key
        )[col_headers]

        # <Print> Quandl API Summary
        if verbose:
            print(f"\n[Quandl] Query API Summary:\n")
            print("-" * 75, "\n")
            for param, val in query_params.items():
                print(f"- {param}:", val)

            print("\n", ("-" * 75), "\n")
            print("\n[Preview] Response DataFrame\n")
            print("\n", stock_returns.head(10), "\n")
            print("-" * 75, "\n")
            print("\n[View] DataFrame Columns -- Data Uniformity\n")
            print(stock_returns.count(), "\n")
            print("-" * 75, "\n")
            print("\n[View] DataFrame Columns -- Data Types\n")
            print(stock_returns.dtypes, "\n")

        # Return DataFrame Containing API Response Data
        return stock_returns

    except:
        print(f"\n[Error | API Query] Invalid Company Symbol: {query_params['symbol']}")
        return None


def qry_balance_sheet(symbol):
    '''
    [params] symbol: Company Stock Ticker Symbol
    [return] output: SEC API Query String - Consolidated Balance Sheet
    '''
    baseuri = f"https://datafied.api.edgar-online.com/v2/corefinancials/ann"
    symbol = f"primarysymbols={symbol.upper()}"
    periods = "numperiods=5"
    fields = "fields=BalanceSheetConsolidated"
    appkey = f"appkey={sec_api_key}"
    debug = f"debug=true"

    params = [symbol, periods, fields, appkey, debug]
    queryuri = "&".join(params)
    apiquery = f"{baseuri}?{queryuri}"
    print(f"\n<API Query String> {apiquery}\n")

    return apiquery


def qry_income_statement(symbol):
    '''
    [params] symbol: Company Stock Ticker Symbol
    [return] output: SEC API Query String - Consolidated Income Statement
    '''
    baseuri = f"https://datafied.api.edgar-online.com/v2/corefinancials/ann"
    symbol = f"primarysymbols={symbol.upper()}"
    periods = "numperiods=5"
    fields = "fields=IncomeStatementConsolidated"
    appkey = f"appkey={sec_api_key}"
    debug = f"debug=true"

    params = [symbol, periods, fields, appkey, debug]
    queryuri = "&".join(params)
    apiquery = f"{baseuri}?{queryuri}"
    print(f"\n<API Query String> {apiquery}\n")

    return apiquery


def qry_cash_flow_statement(symbol):
    '''
    [params] symbol: Company Stock Ticker Symbol
    [return] output: SEC API Query String - Consolidated Cash Flow Statement
    '''
    baseuri = f"https://datafied.api.edgar-online.com/v2/corefinancials/ann"
    symbol = f"primarysymbols={symbol.upper()}"
    periods = "numperiods=5"
    fields = "fields=CashFlowStatementConsolidated"
    appkey = f"appkey={sec_api_key}"
    debug = f"debug=true"

    params = [symbol, periods, fields, appkey, debug]
    queryuri = "&".join(params)
    apiquery = f"{baseuri}?{queryuri}"
    print(f"\n<API Query String> {apiquery}\n")

    return apiquery
