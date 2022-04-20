import pandas as pd
import requests
import streamlit as st

st.title("Bitcoin Prices")

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
currencies = ["CAD","USD","INR"]
currency_low = st.radio("Currency",currencies).lower()
day_selected = st.slider("No. of days", min_value = 1, max_value = 365)
parameters = {"vs_currency":currency_low, "days":str(day_selected), "interval":"daily"}
request = requests.get(url, parameters)

data_back = request.json()
bit_c = pd.DataFrame(data_back["prices"], columns=["date", "prices"])
bit_c["date"] = pd.to_datetime(bit_c["date"], unit="ms")
bit_c.sort_values(by="date", inplace=True)
bit_c = bit_c.set_index("date")
st.line_chart(bit_c)
avg_price = str(round(bit_c["price"].mean(),2))
text = "Average price during this time was "+avg_price+" "+currency_low.upper()
st.write(text)




