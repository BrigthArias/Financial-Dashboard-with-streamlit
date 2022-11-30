###############################################################################
# FINANCIAL DASHBOARD #2 - v2.1
###############################################################################

#==============================================================================
# Initiating
#==============================================================================

#Add the neccesary libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import yfinance as yf
import streamlit as st
import numpy as np
import pandas_datareader.data as web
import datetime as dt 
from PIL import Image
#==============================================================================
# Tab 1: Company profile
#==============================================================================

def tab1():
    
    # Add dashboard title and description
    st.title("Brigth Arias: My financial dashboard")
    st.write("Data source: Yahoo Finance. URL: https://finance.yahoo.com/")
    st.header('Tab 1 - Summary of the company')

    @st.cache
    #Get the information company
    def GetCompanyInfo(ticker):
        return yf.Ticker(ticker).info
    if ticker != '':
        # Get the company information in list format
        info = GetCompanyInfo(ticker)
        # Show the company description
        st.write('**1. Business Summary:**')
        st.image(info['logo_url']) 
        st.write(info['longBusinessSummary'])
        
        #Divide in two columns the statistics and major holders
        Col1, Col2 = st.columns(2)   
    
        # Show some statistics
        Col1.write('**2. Key Statistics:**')
        keys = ['previousClose', 'open', 'bid', 'ask','marketCap', 'volume', 'averageVolume', 'marketCap', 'beta', 'pegRatio', 'trailingEps' ]
        company_stats = {}  # Dictionary
        for key in keys:
            company_stats.update({key:info[key]})
        company_stats = pd.DataFrame({'Value':pd.Series(company_stats)})  # Convert to DataFrame
        Col1.dataframe(company_stats)
    
        @st.cache
        #Show the Major Holders
        def GetMajorHolders(ticker):
           return yf.Ticker(ticker).major_holders
       
        if ticker != '':
            major_holders = GetMajorHolders(ticker)
            Col2.write('**3. Major Holders:**')
            Col2.dataframe(major_holders)
            
    #Show the Trade prices
    st.write('**4. Trade prices:**')
    #Separate into 8 columns with its respective buttom    
    x1, x2, x3, x4, x5, x6, x7, x8 = st.columns(8)    
    
    M1 = x1.button("1M")
    M3 = x2.button("3M")
    M6 = x3.button("6M")
    YTD = x4.button("YTD")
    Y1 = x5.button("1Y")
    Y3 = x6.button("3Y")
    Y5 = x7.button("5Y")
    MAX = x8.button("MAX")

    #1M Function for stock price graph 
    @st.cache
    def GetInfo1m(tickers, start_date=end_date - timedelta(days=30), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start=end_date - timedelta(days=30), end=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if M1:
        #Call the function
        if ticker != '':
            stock_price = GetInfo1m([ticker], start_date=end_date - timedelta(days=30), end_date=end_date)   
            
            #Add the plot
            fig1m, ax1m = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                ax1m.plot(stock_df['Close'], label=tick)
            ax1m.legend()
            st.pyplot(fig1m) 

    #3M Function for stock price graph 
    @st.cache
    def GetInfo3m(tickers, start_date=end_date - timedelta(days=90), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start=end_date - timedelta(days=90), end=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if M3:
        #Call the function
        if ticker != '':
            stock_price = GetInfo3m([ticker], start_date=end_date - timedelta(days=90), end_date=end_date)   
            
            #Add the plot
            fig3m, ax3m = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                ax3m.plot(stock_df['Close'], label=tick)
            ax3m.legend()
            st.pyplot(fig3m)  
            
            
    #6M Function for stock price graph 
    @st.cache
    def GetInfo6m(tickers, start_date=end_date - timedelta(days=180), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start=end_date - timedelta(days=180), end=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if M6:
        #Call the function
        if ticker != '':
            stock_price = GetInfo6m([ticker], start_date=end_date - timedelta(days=180), end_date=end_date)   
            
            #Add the plot
            fig6m, ax6m = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                ax6m.plot(stock_df['Close'], label=tick)
            ax6m.legend()
            st.pyplot(fig6m)

    #YTD Function for stock price graph 
    @st.cache
    def GetInfoYTD(tickers, start_date=end_date.replace(month=1, day=1), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start_date=end_date.replace(month=1, day=1), end_date=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if YTD:
        #Call the function
        if ticker != '':
            stock_price = GetInfoYTD([ticker], start_date=end_date.replace(month=1, day=1), end_date=end_date)   
            
            #Add the plot
            figYTD, axYTD = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                axYTD.plot(stock_df['Close'], label=tick)
            axYTD.legend()
            st.pyplot(figYTD)  


    #1Y Function for stock price graph 
    @st.cache
    def GetInfo1Y(tickers, start_date=end_date - timedelta(days=365), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start=end_date - timedelta(days=365), end=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if Y1:
        #Call the function
        if ticker != '':
            stock_price = GetInfo1Y([ticker], start_date=end_date - timedelta(days=365), end_date=end_date)   
            
            #Add the plot
            fig1Y, ax1Y = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                ax1Y.plot(stock_df['Close'], label=tick)
            ax1Y.legend()
            st.pyplot(fig1Y)  


    #Y3 Function for stock price graph 
    @st.cache
    def GetInfo3Y(tickers, start_date=end_date - timedelta(days=1095), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start=end_date - timedelta(days=1095), end=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if Y3:
        #Call the function
        if ticker != '':
            stock_price = GetInfo3Y([ticker], start_date=end_date - timedelta(days=1095), end_date=end_date)   
            
            #Add the plot
            fig3Y, ax3Y = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                ax3Y.plot(stock_df['Close'], label=tick)
            ax3Y.legend()
            st.pyplot(fig3Y)  
            
            
    #Y5 Function for stock price graph 
    @st.cache
    def GetInfo5Y(tickers, start_date=end_date - timedelta(days=1825), end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(start=end_date - timedelta(days=1825), end=end_date)
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if Y5:
        #Call the function
        if ticker != '':
            stock_price = GetInfo5Y([ticker], start_date=end_date - timedelta(days=1825), end_date=end_date)   
            
            #Add the plot
            fig5Y, ax5Y = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                ax5Y.plot(stock_df['Close'], label=tick)
            ax5Y.legend()
            st.pyplot(fig5Y)  
            
            
    #MAX Function for stock price graph 
    @st.cache
    def GetInfoMAX(tickers, end_date=end_date):
        stock_price = pd.DataFrame()
        for tick in tickers:
            stock_df = yf.Ticker(tick).history(period="max")
            stock_df['Ticker'] = tick  # Add the column ticker name
            stock_price = pd.concat([stock_price, stock_df], axis=0)  # Comebine results
        return stock_price.loc[:, ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    if MAX:
        #Call the function
        if ticker != '':
            stock_price = GetInfoMAX([ticker], end_date=end_date)   
            
            #Add the plot
            figMAX, axMAX = plt.subplots(figsize=(15, 5))
            for tick in [ticker]:
                stock_df = stock_price[stock_price['Ticker'] == tick]
                axMAX.plot(stock_df['Close'], label=tick)
            axMAX.legend()
            st.pyplot(figMAX)
    
#==============================================================================
# Tab 2: Chart
#==============================================================================

def tab2():
    
    # Add dashboard title and description
    st.title("Brigth Arias: My financial dashboard")
    st.write("Data source: Yahoo Finance. URL: https://finance.yahoo.com/")
    st.header('Tab 2 - Chart')
    st.image(yf.Ticker(ticker).info['logo_url'])
    st.subheader("Stock Price and Trading Volume")
    
     # Get data for chart tab
    def GetDataChart(ticker, start_date, end_date, interval):
        return yf.Ticker(ticker).history(start = start_date, end = end_date, period = interval)
    
     
     # Separate into columns and add buttons
    Column1, Column2 = st.columns(2)
    Column1_type = Column1.selectbox("📉 Select the graph",("Candle","Line"))
    Column2_type = Column2.selectbox("📏 Select Interval",("Day", "Week","Month","Year"))
     
    x1, x2, x3, x4, x5, x6, x7, x8 = st.columns(8)
    
    M1 = x1.button("1M")
    M3 = x2.button("3M")
    M6 = x3.button("6M")
    YTD = x4.button("YTD")
    Y1 = x5.button("1Y")
    Y3 = x6.button("3Y")
    Y5 = x7.button("5Y")
    MAX = x8.button("MAX")
    
    # Designate to each buttons
    if M1:
        end_day = end_date
        start_day = end_day - timedelta(days=30)
    elif M3:
        end_day = end_date
        start_day = end_day - timedelta(days=90)
    elif M6:
        end_day = end_date
        start_day = end_day - timedelta(days=180)
    elif YTD:
        end_day = end_date
        start_day = end_date.replace(month=1, day=1)
    elif Y1:
        end_day = end_date
        start_day = end_day - timedelta(days=365)
    elif Y3:
        end_day = end_date
        start_day = end_day - timedelta(days=1095)
    elif Y5:
        end_day = end_date
        start_day = end_day - timedelta(days=1825)
    elif MAX:
        end_day = end_date
        start_day = datetime.date(yf.Ticker(ticker).history(period='max').index.min())  
    else:
        end_day = end_date
        start_day = end_day - timedelta(days=365)
     
    
    # Define the select box for each interval Type
    if Column2_type == "Day":
        interval = "1d"
    elif Column2_type == "Week": 
        interval = "1W"
    elif Column2_type == "Month": 
        interval = "1mo"
    else:
        interval = "1Y"
    
    # Calculate stockprice for close, up, and down
    if ticker != '':
        stockprice = GetDataChart(ticker, start_day, end_day, interval)
        up = stockprice[stockprice["Close"]>stockprice["Open"]]
        down = stockprice[stockprice["Close"]<stockprice["Open"]]
        stockprice['moving_avg'] = stockprice['Close'].rolling(window=50).mean()
    
# Part 1: Line Plot
     
     # Create the figure
    figtab2, ax2line = plt.subplots(figsize=(20, 8))
     
     # Second axis
    ax2 = ax2line.twinx()
   
    # Plot close price
    ax2.plot(stockprice["Close"], label="Close", color='black')

    # Plot moving average
    ax2.plot(stockprice.index, stockprice.moving_avg, color="blue", label="Mov Avg 50 day")
  
    # Plot trading volume 
    ax2line.bar(up.index, up.Volume, width = 0.4, color = "red", alpha=0.6, label="Up")
    ax2line.bar(down.index, down.Volume, width = 0.4, color = "green", alpha=0.6, label="Down")
  
    # Adjust the axis
    ax2line.set_ylim(bottom=0,top=stockprice["Volume"].max()*5)
    ax2line.set_xlim(left=stockprice.index.min(),right=stockprice.index.max())
  
    # Create labels
    ax2.set_title("Stock Close and Volume")
    ax2.set_ylabel("Close (USD)")
    ax2line.set_ylabel("Volume (million)")
   
    # Location of legends
    ax2.legend(loc=1)
    ax2line.legend(loc=2)
    
# Part 2: Candle Plot

    # Create the figure
    fig2candles, ax2line = plt.subplots(figsize=(20, 8))
   
    # Second axis
    ax2 = ax2line.twinx()
  
    # Plot close price
    width = 0.6
    width2 = 0.02
   
    # Plot Up data 
    ax2.bar(up.index, up.Close - up.Open, width, bottom = up.Open, color = "red")
    ax2.bar(up.index, up.High - up.Close, width2, bottom= up.Close, color="grey")
    ax2.bar(up.index, up.Open - up.Low, width2, bottom= up.Low, color="grey")
  
    # Plot Down data
    ax2.bar(down.index, down.Close - down.Open, width, bottom = down.Open, color = "green")
    ax2.bar(down.index, down.High - down.Close, width2, bottom= down.Close, color="grey")
    ax2.bar(down.index, down.Open - down.Low, width2, bottom= down.Low, color="grey")

    # Plot moving average
    ax2.plot(stockprice.index, stockprice.moving_avg, color="blue", label="Mov Avg 50 day")
         
    # Plot trading volume 
    ax2line.bar(up.index, up.Volume, width = 0.3, color = "red", alpha=0.6, label="Up")
    ax2line.bar(down.index, down.Volume, width = 0.3, color = "green", alpha=0.6, label="Down")
        
    # Adjust the axis
    ax2line.set_ylim(bottom=0,top=stockprice["Volume"].max()*5)
    ax2line.set_xlim(left=stockprice.index.min(),right=stockprice.index.max())

    # Create labels
    ax2.set_title("Close Price and Trading Volume")
    ax2.set_ylabel("Close Price (USD)")
    ax2line.set_ylabel("Trading Volume (Million)")
    
    # Location of legends
    ax2.legend(loc=1)
    ax2line.legend(loc=2)
        
    # Switch between candle plot and line plot
    if Column1_type == "Candle":
        st.pyplot(fig2candles)
    elif Column1_type == "Line":
        st.pyplot(figtab2)
    else:
        st.pyplot(figtab2)


#==============================================================================
# Tab 3 - Financials
#==============================================================================

def tab3():
    
    # Add dashboard title and description
    st.title("Brigth Arias: My financial dashboard")
    st.write("Data source: Yahoo Finance. URL: https://finance.yahoo.com/")
    st.header('Tab 3 - Financials')
    st.image(yf.Ticker(ticker).info['logo_url'])
        
  # Get the Financial information
    @st.cache
    def GetFinancialData(ticker):
       return yf.Ticker(ticker).financials
   
    if ticker != '':
        # Get the financials information in list format
        financials = GetFinancialData(ticker)

    #Get the Balance Sheet information
    @st.cache
    def GetBalanceData(ticker):
        return yf.Ticker(ticker).balance_sheet
    
    if ticker != '':
        # Get the balance information in list format
        balance = GetBalanceData(ticker)
        
    # Get the cashflow information
    @st.cache
    def GetCashFlowData(ticker):
        return yf.Ticker(ticker).cashflow
    
    if ticker != '':
        # Get the cashflow information in list format
        cashflow = GetCashFlowData(ticker)
     
     
    # Get the financials quarterly information
    @st.cache
    def GetFinancialDataQuarterly(ticker):
        return yf.Ticker(ticker).quarterly_financials
    
    if ticker != '':
        # Get the financials quarterly information in list format
        quarterly_financials = GetFinancialDataQuarterly(ticker)
    
    # Get the Balance Quarterly information
    @st.cache
    def GetBalanceDataQuarterly(ticker):
        return yf.Ticker(ticker).quarterly_balance_sheet
    
    if ticker != '':
        # Get the Balance Quarterly information in list format
        quarterly_balance_sheet = GetBalanceDataQuarterly(ticker)

    # Get the cashflow Quarterly information
    @st.cache
    def GetCashFlowDataQuarterly(ticker):
        return yf.Ticker(ticker).quarterly_cashflow
    
    if ticker != '':
        # Get the cashflow Quarterly information in list format
        quarterly_cashflow = GetCashFlowDataQuarterly(ticker)

    # Define the selection button
    # Create two columns for choosing the options
    col1, col2 = st.columns(2)
    
    with col1:
        # Define the list for table_names
        table_names = ['Income Statements', 'Balance Sheet', 'Cash Flow']
        # Add the option format button
        table = st.radio('Show:', table_names)
    
    with col2:
        # Define the list for table_period
        table_period = ['Annual', 'Quarterly']
        # Add the option format button
        period = st.radio('Chose period 👇:', table_period)
    
    #Conditions for each time and its respective table
    #Condition for Annual and Income Statements
    if period == 'Annual' and table == 'Income Statements':
        # Show title and table 
        st.write('**🟣 Income Statements:**')
        st.write(financials)
    
    #Condition for annual balance sheet
    elif period == 'Annual' and table == 'Balance Sheet':
        # Show title and table 
        st.write('**🔴 Balance Sheet:**')
        st.write(balance)
    
    #Condition for annual cash flow
    elif period == 'Annual' and table == 'Cash Flow':
        # Show title and table 
        st.write('**🟡 Cash Flow:**')
        st.write(cashflow)
    
    #Condition for quarterly Income Statements
    elif period == 'Quarterly' and table == 'Income Statements':
        # Show title and table 
        st.write('**🟣 Income Statements:**')
        st.write(quarterly_financials)
    
    #Condition for quarterly balance sheet
    elif period == 'Quarterly' and table == 'Balance Sheet':
        # Show title and table 
        st.write('**🔴 Balance Sheet:**')
        st.write(quarterly_balance_sheet)
    
    #Condition for quarterly cashflow
    else:
        # Show title and table of the left 
        st.write('**🟡 Cash Flow:**')
        st.write(quarterly_cashflow)    

    
#==============================================================================
# Tab 4
#==============================================================================

def tab4():
    # Add dashboard title and description
    st.title("Brigth Arias: My financial dashboard")
    st.write("Data source: Yahoo Finance. URL: https://finance.yahoo.com/")
    st.header('Tab 4 - Monte Carlo Simulation')
    st.image(yf.Ticker(ticker).info['logo_url'])
    
    # Get two columns
    Column1, Column2 = st.columns(2)
   
    
    # Add list for time horizon
    time_horizon_list = [30, 60, 90]
    # Get the time_horizon as global variable
    global time_horizon
    time_horizon = Column1.selectbox('Select the time horizon (in days):',time_horizon_list)
    
    #Add list for number of simulation
    nbr_simulations = [200, 500, 1000]
    # Get the n_simulation as global variable
    global n_simulation
    n_simulation = Column2.selectbox('Select the number of simulations:',nbr_simulations)


    #Get the Montecarlo function
    class MonteCarlo(object):
        # Define the parameters
        def __init__(self, ticker, data_source, start_date, end_date, time_horizon, n_simulation, seed):
            
            # Initiate class variables
            self.ticker = ticker  # Stock ticker
            self.data_source = data_source  # Source of data, e.g. 'yahoo'
            self.start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')  # Text, YYYY-MM-DD
            self.end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')  # Text, YYYY-MM-DD
            self.time_horizon = time_horizon  # Days
            self.n_simulation = n_simulation  # Number of simulations
            self.seed = seed  # Random seed
            self.simulation_df = pd.DataFrame()  # Table of results
            
            # Extract stock data
            self.stock_price = web.DataReader(ticker, data_source, self.start_date, self.end_date)
            
            # Calculate financial metrics
            # Daily return (of close price)
            self.daily_return = self.stock_price['Close'].pct_change()
            # Volatility (of close price)
            self.daily_volatility = np.std(self.daily_return)
            
        #Get the simulations    
        def run_simulation(self):
            
            # Run the simulation
            np.random.seed(self.seed)
            self.simulation_df = pd.DataFrame()  # Reset
            
            for i in range(self.n_simulation):
    
                # The list to store the next stock price
                next_price = []
    
                # Create the next stock price
                last_price = self.stock_price['Close'][-1]   
                for j in range(self.time_horizon):
                    
                    # Generate the random percentage change around the mean (0) and std (daily_volatility)
                    future_return = np.random.normal(0, self.daily_volatility)
    
                    # Generate the random future price
                    future_price = last_price * (1 + future_return)
    
                    # Save the price and go next
                    next_price.append(future_price)
                    last_price = future_price
    
                # Store the result of the simulation
                next_price_df = pd.Series(next_price).rename('sim' + str(i))
                self.simulation_df = pd.concat([self.simulation_df, next_price_df], axis=1)
                
        #Get the price for simulation
        def plot_simulation_price(self):
            
            # Plot the simulation stock price in the future
            fig, ax = plt.subplots()
            fig.set_size_inches(15, 10, forward=True)
    
            plt.plot(self.simulation_df)
            plt.title('Monte Carlo simulation for ' + self.ticker + \
                      ' stock price in next ' + str(self.time_horizon) + ' days')
            plt.xlabel('Day')
            plt.ylabel('Price')
    
            plt.axhline(y=self.stock_price['Close'][-1], color='red')
            plt.legend(['Current stock price is: ' + str(np.round(self.stock_price['Close'][-1], 2))])
            ax.get_legend().legendHandles[0].set_color('red')
    
            st.pyplot(fig)
        
        #Get the confidence interval
        def value_at_risk(self):
            # Price at 95% confidence interval
            future_price_95ci = np.percentile(self.simulation_df.iloc[-1:, :].values[0, ], 5)
    
            # Value at Risk
            VaR = self.stock_price['Close'][-1] - future_price_95ci
            st.write('VaR at 95% confidence interval is: ' + str(np.round(VaR, 2)) + ' USD')
    
    # Add the date of today
    this_day = datetime.today().date().strftime('%Y-%m-%d')
    
    # Define the information for parameters of Montecarlo simulation
    mc_sim = MonteCarlo(ticker, data_source='yahoo',
                    start_date='2020-01-01', end_date= this_day,
                    time_horizon=time_horizon, n_simulation=n_simulation, seed=123)
    
    # Run simulation
    mc_sim.run_simulation()
    
    # Plot the results
    mc_sim.plot_simulation_price()
    
    # Value at risk
    mc_sim.value_at_risk()
    
#==============================================================================
# Tab 5
#==============================================================================

def tab5():
    # Add dashboard title and description
    st.title("Brigth Arias: My financial dashboard")
    st.write("Data source: Yahoo Finance. URL: https://finance.yahoo.com/")
    st.header('Tab 5 - News')

    # Get three columns to center the logo
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')
    with col2:
        st.image(yf.Ticker(ticker).info['logo_url'])
    with col3:
        st.write(' ')
    
    # Get the list to the number of news
    keys = [1,2,3,4,5]
    
    # Create a dictionary for title news
    title = {}
    # Create a dictionary for publisher news
    publisher = {}
    # Create a dictionary for link news
    link = {}
    
    # Create a for loop to get the elements for each dictionary
    for key in keys:
        
        # Get elements for title dictionary
        title.update({key:yf.Ticker(ticker).news[key]['title']})
        
        # Get elements for publisher dictionary
        publisher.update({key:yf.Ticker(ticker).news[key]['publisher']})
        
        # Get elements for link dictionary
        link.update({key:yf.Ticker(ticker).news[key]['link']})
        
    # Conver all the dictionaries into one data frame    
    news = pd.DataFrame({'Title':pd.Series(title), 'Publisher':pd.Series(publisher), 'Link':pd.Series(link)})
    
    # Show the data frame
    st.write(news)
  
#==============================================================================
# Main body
#==============================================================================

def run():
        
    # Add the ticker selection on the sidebar
    # Get the list of stock tickers from S&P500
    ticker_list = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol']
    
    # Add image in the top of sidebar
    image = Image.open('./img/Yahoo!_Finance_logo_2021.png')
    st.sidebar.image(image)
    
    
    # Add selection box
    global ticker
    ticker = st.sidebar.selectbox("Select a ticker", ticker_list)
    

    # Add select begin-end date as global
    global start_date, end_date
    
    # Get two columns for start_date and end_date
    col1, col2 = st.sidebar.columns(2)
    
    # Get the start_date (for one month as default in app)
    start_date = col1.date_input("Start date", datetime.today().date() - timedelta(days=30))
    # Get the end_date (today as default in app)
    end_date = col2.date_input("End date", datetime.today().date())
    
    
    # Add a radio box
    select_tab = st.sidebar.radio("Select tab", ['Company profile', 'Chart','Finance', 'Monte Carlo Simulation','News'])
    

    
    # Show the selected tab
    if select_tab == 'Company profile':
        # Run tab 1
        tab1()
    if select_tab == 'Chart':
        # Run tab 2
        tab2()
    if select_tab == 'Finance':
        # Run tab 3
        tab3()
    
    if select_tab == 'Monte Carlo Simulation':
        # Run tab 4
        tab4()
                
    elif select_tab == 'News': 
        # Run tab 5
        tab5()

    
if __name__ == "__main__":
    run()
    

###############################################################################
# END
###############################################################################

###############################################################################
# REFERENCES
###############################################################################

#https://docs.streamlit.io/library/api-reference/widgets/st.radio
#https://github.com/fondaa/bigdata/blob/2ac02eaabafb0b75a4e704449a2192b8b915c6ff/StreamlitApp_YahooFinance_Webscraping.py
#https://www.youtube.com/watch?v=sAVEbpBMXuc
#http://theautomatic.net/yahoo_fin-documentation/#get_company_info 
#https://analyzingalpha.com/yfinance-python
#https://medium.com/codex/extracting-financial-news-seamlessly-using-python-4dcc732d9ff1
#https://github.com/hackingthemarkets/streamlit-dashboards/blob/main/dashboard.py
#https://stackoverflow.com/questions/70932538/how-to-center-the-title-and-an-image-in-streamlit 

