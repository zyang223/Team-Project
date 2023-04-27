  # Team-Project
  
  **DCF WEB App Produced by Zide Yang**

  <span style="color:red">**Important update, my API's authorization for the download the finacial data in the quickexcel template seemed get banned, please try to use yours api from finicial model www.financialmodelingprep.com to sign up a new api Thank you!**</span> But you could still try Ticker ADSK to test the function.

  " Hi all, this is a final project created by Zide Yang. The objective of this DCF instruction website is to  help college students  reducing their suffer from  doing Discounting Cash Flow model. I know it is very hard while you haven't deal it before and it is quite annoying for you to do the whole model and finding information from different websites that takes several hours. Therefore, I am creating this website and tutorial to help you to release your stress and go through the whole process with you.

  This DCF (Discounted Cash Flow) web app is designed to provide a quick and simple way to estimate the fair value per share of a publicly traded company based on the DCF method. The app is based on Python and uses the Flask web framework to provide a user interface.


<br>

  **The app takes the following inputs:**

  Ticker Symbol: The stock ticker symbol of the company.
  API Key: The API key for accessing financial data from financial APIs.
  Perpetual Growth Rate: The estimated growth rate for cash flows beyond the forecast period.
  WACC: Weighted Average Cost of Capital, the required rate of return used to discount future cash flows.
  The app provides the following outputs:

  + FCF for the most recent year.
  + FCF projection over the next five years.
  + Present value of future cash flows.
  + Present value of terminal value.
  + Enterprise value.
  + Equity value.
  + Fair value per share.

<br>

  The app uses the following financial APIs to retrieve financial data:

  + Alpha Vantage
  + Financial Modeling Prep

<br>
<br>

  The dcf.py includes several function and calculation in ther 

  **Enterprise Value (EV) calculation:** This function calculates the Enterprise Value of a company based on the Free Cash Flow (FCF) projections, WACC, and terminal growth rate assumptions. It uses the financial data API to fetch FCF and balance sheet data of the company and uses the FCF projections to calculate the present value of future cash flows using the Discounted Cash Flow (DCF) method. The terminal value of the company is also calculated using the Gordon Growth Model. The sum of the present value of future cash flows and terminal value is the Enterprise Value.

  **Equity Value calculation:** This function calculates the Equity Value of a company based on the Enterprise Value, net debt, and cash and cash equivalents. It uses the financial data API to fetch Enterprise Value, balance sheet data of the company, and calculates the Equity Value by subtracting the net debt from the Enterprise Value and adding the cash and cash equivalents.

  **Fair Value per share calculation:** This function calculates the Fair Value per share of a company based on the Equity Value and the number of shares outstanding. It uses the financial data API to fetch the income statement data of the company and calculates the fair value per share by dividing the Equity Value by the weighted average shares outstanding.

  The result of this DCF Web app has been shown by using a **flask app**
  <br>

  **You could run the app.py enter http://127.0.0.1:5000/home in your browser to use the app.**

  <br>
  <br>
  The website have 5 main pages and each of them contains different information:


  + **welcome.html:** This page serves as the landing page or welcome page of the web app. It gives users a brief introduction of the app and directs them to the main functionality of the app.

  + **dcfinput.html:** This page allows users to input a stock ticker and their API key, which is required to fetch financial data from the Alpha Vantage API. Once the user inputs this data and submits the form, the app calculates the discounted cash flow (DCF) values and presents them to the user in the dcfresult.html page.

  + **dcfresult.html:** This page presents the DCF values calculated by the app in a tabular format. It includes various DCF values such as free cash flow (FCF), present value, terminal value, equity value, shares outstanding, and fair value per share. Additionally, the user can download an Excel file containing the calculation details by clicking on the "Download Excel" button.

  + **whatisdcf.html:** This page explains what discounted cash flow (DCF) analysis is and why it is important in stock valuation.

  + **tutorial.html:**This page provides a tutorial on how to use the app. It guides the user through the process of entering a stock ticker and API key, calculating the DCF values, and downloading the Excel file.
  
  <br>

Feel free to use the webapp and the entire model, I need to special than to **financialmodelingprep.com** for utilizingtheir free-endpoint APIto gather company financials and help and assistance from **Hugh Alessiand** instruction from the website: https://financialmodelingprep.com/developer/docs/.
<br>

  Also, I need to special than to **Professor Li** to help to while I facing difficulties during the project. For further I will still continue on improving this website. If you have a similar interest or meet any problem please contact me **zyang2@babson.edu**