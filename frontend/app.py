import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re


df = pd.read_csv('grouped_TS.csv', sep=',',
                 index_col=['REPORTDATE'], parse_dates=['REPORTDATE'])

df["VALUE"] /= 1e9

plt.style.use('dark_background')
figure, axes = plt.subplots(1, 1)
axes.plot(df, label="historical data")
axes.set_ylabel('Стабильная часть средств(мдрд руб)')
axes.grid()

def get_predict(months: int) -> float:
    response = requests.get(f"http://backend:8000/predict?months={months}")
    response_json = response.json()
    date = re.findall("\d{4}-\d{2}-\d{2}", response_json["date"])
    date_index = pd.DatetimeIndex(data=date)
    predict = response_json["predict"]

    if response.status_code != 200:
        raise ValueError("Predict failed.")
    return date_index, predict


st.title("SBER Time Series")

months = st.slider(label="Горизонт предсказания(мес.)", min_value=1, max_value=12, value=1)

date, predict = get_predict(months=months)
series = pd.Series(data=predict, index=date)
axes.plot(series, 'g')
axes.set_ylim(0)
st.pyplot(figure)


# if st.button(label="Predict"):
#     try:
#         date, predict = get_predict(months=months)
#         series = pd.Series(data=predict, index=date)
#         axes.plot(series, 'g')
#         st.pyplot(figure)
#
#         # st.success(f"Predict is: {predict}")
#     except ValueError as exception:
#         st.warning("Got exception while trying to get model prediction.")
