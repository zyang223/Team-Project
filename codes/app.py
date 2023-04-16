from flask import Flask, render_template, request
from decimal import Decimal
from api import *
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate_fair_value', methods=['POST'])
def calculate_fair_value():
    ticker = request.form['ticker']
    apikey = "3178e48c4517a7c30aa49ccbadef2582"
    
    # Load the enterprise value and balance sheet data into dataframes
    ev_data = pd.DataFrame(get_enterprise_value(ticker=ticker, apikey=apikey))
    bs_data = pd.DataFrame(get_balancesheet(ticker=ticker, apikey=apikey))
    
    # Calculate the equity value by subtracting net debt from enterprise value
    ev = ev_data.iloc[0]['enterpriseValue']
    debt = bs_data.iloc[0]['shortTermDebt'] + bs_data.iloc[0]['longTermDebt']
    cash = bs_data.iloc[0]['cashAndCashEquivalents']
    equity_value = ev - debt + cash
    
    # Calculate fair value per share
    ic_data = pd.DataFrame(get_incomestatement(ticker=ticker, apikey=apikey))
    shares_outstanding = ic_data.iloc[0]['weightedAverageShsOut']
    fair_value_per_share = equity_value / shares_outstanding
    
    # Render the results template with the calculated fair value per share
    return render_template('results.html', fair_value_per_share=fair_value_per_share)

if __name__ == '__main__':
    app.run(debug=True)
