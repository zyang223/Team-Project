from flask import Flask, render_template, request,jsonify
from dcf import *
from decimal import Decimal
from api import *
import pandas as pd
app = Flask(__name__)
    

@app.route('/home/')
def welcome_page():
    return render_template ("welcome.html")

@app.route("/quickdcfcal", methods=["GET", "POST"])
def quickdcfcal():
    if request.method == "POST":
        ticker = request.form["ticker"]
        apikey = request.form["apikey"]
        # Call functions to calculate DCF values
        fcf, fcf_dict, present_value, terminal_value = calculate_enterprise_value(ticker, apikey)
        equity_value = calculate_equity_value(ticker, apikey)
        shares_outstanding, fair_value_per_share, equity_value = calculate_fair_price(ticker, apikey)
        return render_template("dcfresult.html", ticker=ticker, apikey=apikey, fcf=fcf, fcf_dict=fcf_dict, present_value=present_value, terminal_value=terminal_value, equity_value=equity_value, shares_outstanding=shares_outstanding, fair_value_per_share=fair_value_per_share)
    else:
        return render_template("dcfinput.html")
        
@app.route('/dcfresult/', methods=['POST'])
def dcfresult():
    try:
        ticker = request.form['ticker']
        apikey = request.form['apikey']
    except:
        return "Missing form data", 400

    # Calculate enterprise value
    fcf, fcf_dict, present_value, terminal_value = calculate_enterprise_value(ticker, apikey)

    # Calculate equity value
    equity_value = calculate_equity_value(ticker, apikey)

    # Calculate fair value per share
    shares_outstanding, fair_value_per_share, equity_value = calculate_fair_price(ticker, apikey)

    return render_template('dcfresult.html',
                           ticker=ticker,
                           apikey=apikey,
                           fcf=fcf,
                           fcf_dict=fcf_dict,
                           present_value=present_value,
                           terminal_value=terminal_value,
                           equity_value=equity_value,
                           shares_outstanding=shares_outstanding,
                           fair_value_per_share=fair_value_per_share)



if __name__ == '__main__':
    app.run(debug=True)
