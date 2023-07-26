import yfinance as yf
import streamlit as st
import pandas as pd

st.title('Price Stocks Line Charts')
st.subheader('Price stocks of Google')
st.selectbox('Seçiminiz:', ['GOOGL', 'TUPRS', 'THYAO', 'FROTO', 'BIMAS', 'ARCLK', 'EREGL', 'AEFES', 'ENJSA'])
st.multiselect('Which company you want to invest:', ('Tüpraş (TUPRS)' 'Türk Hava Yolları (THYAO)', 'Ford Otosan (FROTO)', 'Bim (BIMAS)', 'Arçelik (ARCLK)', 'Ereğli Demir Çelik (EREGL)', 'Anadolu Efes (AEFES)', 'Enerjisa Enerji (ENJSA)'))
st.button('Simple Button')
st.slider('Kaç yıllık grafik görmek istediğinizi seçiniz:', 0,10, step = 1)
st.write("""
#Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")
tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start = '2010-5-31', end = '2023-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# streamlit run main.py


