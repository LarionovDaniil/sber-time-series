"""web page"""
import re
import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("SBER Time Series")
months = st.slider(label="Горизонт предсказания(мес.)", min_value=1, max_value=12, value=1)


def get_predict(months_n: int):
    """get predictions from backend for plot

    Parameters:
    months_n (int): numbers of months to predict

    Returns:
    date and prediction value

   """
    response = requests.get(f"http://backend:8000/predict?months={months_n}", timeout=30)
    response_json = response.json()
    dates = re.findall("\\d{4}-\\d{2}-\\d{2}", response_json["date"])
    date_index = pd.DatetimeIndex(data=dates)
    model_predictions = response_json["predict"]

    if response.status_code != 200:
        raise ValueError("Predict failed.")
    return date_index, model_predictions


def draw_plot():
    """plot drawing"""
    df = pd.read_csv('grouped_TS.csv', sep=',',
                 index_col=['REPORTDATE'], parse_dates=['REPORTDATE'])

    df["VALUE"] /= 1e9

    date, predict = get_predict(months_n=months)
    series = pd.Series(data=predict, index=date)

    plt.style.use('dark_background')
    figure, axes = plt.subplots(1, 1)
    axes.plot(df)
    axes.plot(series, 'g')
    axes.set_ylabel('Стабильная часть средств(мдрд руб)')
    axes.set_ylim(0)
    axes.grid()
    st.pyplot(figure)


draw_plot()
