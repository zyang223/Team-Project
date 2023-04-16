from decimal import Decimal
from api import *
import pandas as pd


ticker = 'ADSK'
apikey = "3178e48c4517a7c30aa49ccbadef2582"
def calculate_enterprise_value(ticker: str, apikey: str) -> Decimal:
    """Assuming perpetual growth rate, gorwth rate and Wacc could be adjusted mannualy"""
    # Load the FCF data into a Pandas dataframe
    fcf_data = pd.DataFrame(get_cashflow(ticker=ticker, apikey=apikey))

    # Calculate FCF for the most recent year
    fcf = fcf_data.iloc[0]['operatingCashFlow'] + fcf_data.iloc[0]['capitalExpenditure']

    # Assume FCF will grow at a constant rate over the next five years
    fcf_growth_rate = 0.12 
    fcf_estimates = [fcf * (1 + fcf_growth_rate)**n for n in range(1, 6)]
    fcf_dict = {f"n{n+1}": fcf for n, fcf in enumerate(fcf_estimates)}
    
    # Discount the future cash flows back to their present value WACC
    discount_rate = 0.10
    present_value = sum([cf / (1 + discount_rate)**n for n, cf in enumerate(fcf_estimates, start=1)])   
    # Calculate the terminal value using the Gordon growth model

    terminal_growth_rate = 0.03
    terminal_cash_flow = fcf_estimates[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    terminal_value = terminal_cash_flow / (1 + discount_rate)**5 # for five years
    return fcf,fcf_dict,present_value,terminal_value
        






# Load the enterprise value and balance sheet data into dataframes
def calculate_equity_value(ticker: str, apikey: str) -> Decimal:
    ev_data = pd.DataFrame(get_enterprise_value(ticker=ticker, apikey=apikey))
    bs_data = pd.DataFrame(get_balancesheet(ticker=ticker, apikey=apikey))
    

    # Calculate the equity value by subtracting net debt from enterprise value
    ev = ev_data.iloc[0]['enterpriseValue']
    print(f"Enterprise Value ={ev:,}\n")
   
    debt = bs_data.iloc[0]['shortTermDebt'] + bs_data.iloc[0]['longTermDebt']
    print(f"Debt= {debt:,}")
    
    cash = bs_data.iloc[0]['cashAndCashEquivalents']
    print(f"Cash={cash:,}")
    equity_value = ev -debt +cash
    print(f"equityvalue: {equity_value:,.2f} = {ev:,.2f} - {debt:,.2f} + {cash:,.2f}\n")
    return equity_value


# # Calculate the fair value per share
def calculate_fair_price(ticker: str, apikey: str) -> Decimal:
    ic_data = pd.DataFrame(get_incomestatement(ticker=ticker, apikey=apikey))
    equity_value=calculate_equity_value(ticker,apikey)
    shares_outstanding = ic_data.iloc[0]['weightedAverageShsOut']
    fair_value_per_share = equity_value / shares_outstanding
    return shares_outstanding,fair_value_per_share,equity_value


def main():
    ticker = 'ADSK'
    apikey = "3178e48c4517a7c30aa49ccbadef2582"
    fcf,fcf_dict,present_value,terminal_value=calculate_enterprise_value (ticker=ticker, apikey=apikey)
    
    print(f"FCF for the most recent year={fcf:,}\n")
    print(f"FCF projection={fcf_dict}\n")
    print(f"Present Value={present_value:,}\n")
    print(f"Present Value of terminal_value={terminal_value:,}\n")

    #equity value
    print(f"equity_value={calculate_equity_value(ticker=ticker, apikey=apikey):,.2f}\n")
    
    

     # Calculate fair value per share
    shares_outstanding, fair_value_per_share,equity_value = calculate_fair_price(ticker=ticker, apikey=apikey)
    print(f"shares_outstanding={shares_outstanding:,}")
    print(f"fair_value_per_share: {fair_value_per_share:.2f} = {equity_value:,.2f} / {shares_outstanding:,.2f}")
    print(f"fair_value_per_share = {fair_value_per_share:.2f}")



if __name__ == '__main__':
    main()