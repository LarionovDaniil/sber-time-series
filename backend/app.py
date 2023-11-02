"""model and fastapi"""
import pickle
from fastapi import FastAPI

app = FastAPI()


with open('arima2.pkl', 'rb') as pkl:
    MODEL = pickle.load(pkl)


@app.get("/healthcheck")
def healthcheck():
    """check if connection is ok"""
    return {"status": "OK"}


@app.get("/predict")
def predict(months: str):
    """get predictions from model

    Parameters:
    months (str): number of months to predict

    Returns:
    dict:date and amount of money

   """
    # модель обучена на пятидневках
    predictions = MODEL.predict(int(months)*7)
    return {"date": str(list(predictions.index)), "predict": list(predictions.values)}
