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
import datetime as dt
import pandas as pd
import numpy as np
import quandl as ql
from config import quandl_api_key


def quandl_stock_data(symbol, verbose=False):
    # <Define> DataFrame Column Headers
    headers = [
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
        "data_type": "pandas",    # [numpy | pandas ] Array vs DataFrame
    }

    try:
        stock_returns = ql.get(
            f"WIKI/{query_params['symbol']}",
            start_date=query_params['start_date'],
            end_date=query_params['end_date'],
            colapse=query_params['collapse'],
            returns=query_params['data_type'],
            authtoken=quandl_api_key
        )[headers]

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

        return stock_returns

    except ql.NotFoundError:
        print(f"\n[Error | API Query] Invalid Company Symbol: {query_params['symbol']}")
        return None

# Portfolio Optimization Function


def optimize_portfolio(assets, simulations=5000):
    num_assets = len(assets)
    portfolio = closing_prices(assets[0])
    print(f'[{0}] Retrieving Stock Data: {assets[0].upper()}')

    for i, asset in enumerate(assets[1:]):
        print(f'[{i + 1}] Retrieving Stock Data: {asset}')
        add_stock = closing_prices(asset)
        portfolio = pd.merge(portfolio, add_stock, on="Date", how="inner")
        del add_stock

    portfolio.set_index("Date", inplace=True)

    print(f'\nOptimizing Portfolio Weights >> Simulations: x {simulations}')
    portfolio_log = []
    portfolio_sim = {}
    for i in range(simulations):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        WTSp = zip(assets, weights)
        RTNp = exp_portfolio_return(portfolio, weights)
        VARp = exp_portfolio_variance(portfolio, weights)

        portfolio_sim = {a: round(wt, 4) for a, wt in WTSp}
        portfolio_sim["Return"] = RTNp
        portfolio_sim["Variance"] = VARp
        portfolio_sim["Sharpe"] = mod_sharpe_ratio(RTNp, VARp)
        portfolio_log.append(portfolio_sim)

    log_df = pd.DataFrame(portfolio_log)
    ranked_df = log_df.sort_values("Sharpe", ascending=False)

    print(f'\nOptimized Portfolio Weights:')
    print(ranked_df.iloc[0])
    return dict(ranked_df.iloc[0])


# Portfolio Performance Back-Testing Function

def backtest_portfolio(pfolio):
    exclude = ["Return", "Sharpe", "Variance"]
    assets = [(a, wt) for a, wt in pfolio.items() if a not in exclude]

    # Initialize Portfolio Back-Test Performance DataFrame
    back_test = closing_prices(assets[0][0]).set_index("Date")
    back_test = np.log(back_test / back_test.shift(1)).iloc[1:]
    back_test = back_test.apply(lambda x: x * assets[0][1])
    print(f'\nTicker: {assets[0][0]} \tPortfolio Weight: {assets[0][1]}')
    print(back_test.head())

    for allocation in assets[1:]:
        stock = allocation[0]
        weight = allocation[1]
        print(f'\nTicker: {stock} \tPortfolio Weight: {weight}')

        closing_data = closing_prices(stock).set_index("Date")
        pct_return = np.log(closing_data / closing_data.shift(1)).iloc[1:]
        pct_return = pct_return.apply(lambda x: x * weight)
        back_test = pd.merge(back_test, pct_return, on="Date", how="inner")
        print(pct_return.head())

    back_test["RTNp"] = back_test.sum(axis=1)
    print("\n[Historic] Portfolio Performance:\n", back_test.head())

    return back_test


# Portfolio Performance Evaluation Function
def evaluate_portfolio(rtns):
    RTNm = pd.read_csv("S&P500.csv")[["Date", "Close"]]
    RTNm["Date"] = pd.to_datetime(RTNm["Date"])
    RTNm = RTNm.rename(columns={"Close": "RTNm"}).set_index("Date")
    RTNm = np.log(RTNm / RTNm.shift(1)).iloc[1:]

    rtns = pd.merge(rtns, RTNm, on="Date", how="inner")
    rtns["Excess"] = rtns["RTNp"] - rtns["RTNm"]
    rtns["Compare"] = rtns["Excess"] > 0
    rtns["Compare"] = rtns["Compare"].apply(lambda x: "Outperform" if x else "Underperform")
    print(rtns.head())

    return rtns[["RTNp", "RTNm", "Excess", "Compare"]]


# Helper Functions - Optimize Portfolio, Backtest Portfolio Performance

def closing_prices(stock):
    price_data = quandl_stock_data(stock) \
        .rename(columns={"Close": stock.upper()})[stock.upper()] \
        .reset_index()
    return price_data


def exp_portfolio_return(portfolio, weights):
    log_returns = np.log(portfolio / portfolio.shift(1)).iloc[1:]
    return round(np.sum(weights * log_returns.mean()) * 250, 4)


def exp_portfolio_variance(portfolio, weights):
    log_returns = np.log(portfolio / portfolio.shift(1)).iloc[1:]
    return round(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))), 4)


def mod_sharpe_ratio(ERp, EVARp):
    mkt_return = .098
    return round((ERp - mkt_return) / EVARp, 4)
