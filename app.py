from flask import Flask, render_template, request,jsonify,send_file, send_from_directory
from dcf import *
from decimal import Decimal
from api import *
import pandas as pd
app = Flask(__name__)
    

@app.route('/home/')
def welcome_page():
    return render_template ("welcome.html")

@app.route("/quickdcfcal/", methods=["GET", "POST"])
def quickdcfcal():
    if request.method == "POST":
        ticker = request.form.get("ticker")
        apikey = request.form.get("apikey")
        # Call functions to calculate DCF values
        fcf, fcf_table, present_value, terminal_value = calculate_enterprise_value(ticker, apikey)
        equity_value = calculate_equity_value(ticker, apikey)
        shares_outstanding, fair_value_per_share, equity_value = calculate_fair_price(ticker, apikey)
        # Create the excel file for downloading
        download_xlsx(ticker, apikey) # generate an excel file
        return render_template("dcfresult.html",
                        ticker=ticker,
                        apikey=apikey,
                        fcf=format(fcf, ","),
                        fcf_table=fcf_table,   
                        present_value=format(present_value, ","),
                        terminal_value=format(terminal_value, ","),
                        equity_value=format(equity_value, ","),
                        shares_outstanding=format(shares_outstanding, ","),
                        fair_value_per_share=format(fair_value_per_share, ","))

    else:
        return render_template("dcfinput.html")
    
app.config['EXCEL_FOLDER']='Excel'

@app.route('/download/excel/<string:ticker>.xlsx')
def download_excel(ticker):
    filename = f"{ticker}.xlsx"
    # return send_file(filename, as_attachment=True)
    print(app.root_path)
    full_path = os.path.join(app.root_path, app.config['EXCEL_FOLDER'])
    print(full_path)
    return send_from_directory(full_path, filename)


@app.route('/whatisdcf/')
def whatisdcf():
    return render_template("whatisdcf.html")

@app.route('/exceltemplate/')
def exceltemplate():
    return render_template("exceltemplate.html")

@app.route('/tutorial/')
def tutorial():
    return render_template("tutorial.html")


# @app.route('/dcfresult/', methods=['POST'])
# def dcfresult():
#     try:
#         ticker = request.form['ticker']
#         apikey = request.form['apikey']
#     except:
#         return "Missing form data", 400

#     # Calculate enterprise value
#     fcf, fcf_dict, present_value, terminal_value = calculate_enterprise_value(ticker, apikey)

#     # Calculate equity value
#     equity_value = calculate_equity_value(ticker, apikey)

#     # Calculate fair value per share
#     shares_outstanding, fair_value_per_share, equity_value = calculate_fair_price(ticker, apikey)

#     return render_template('dcfresult.html',
#                            ticker=ticker,
#                            apikey=apikey,
#                            fcf=fcf,
#                            fcf_dict=fcf_dict,
#                            present_value=present_value,
#                            terminal_value=terminal_value,
#                            equity_value=equity_value,
#                            shares_outstanding=shares_outstanding,
#                            fair_value_per_share=fair_value_per_share)



if __name__ == '__main__':
    app.run(debug=True)
