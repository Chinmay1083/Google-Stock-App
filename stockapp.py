import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
 #  Google StockStream

Shows the **cost of valuation** of stocks of Google specified between a **specified range of dates**
"""
)

# adding hashtags to above
tickerSymbol = "GOOGL"
tickerData = yf.Ticker(tickerSymbol)

# need to get historical prices for this ticker app


tickerDf = tickerData.history(period = '1d' , start = '2010-5-31' , end = '2020-5-31')


# Open   High     Low Close    Volume   Dividends  Stock Splits
st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")

st.line_chart(tickerDf.Volume)