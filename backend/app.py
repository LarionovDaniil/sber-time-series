import pickle

from fastapi import FastAPI

app = FastAPI()


with open('arima2.pkl', 'rb') as pkl:
    MODEL = pickle.load(pkl)


@app.get("/healthcheck")
def healthcheck():
    return {"status": "OK"}


@app.get("/predict")
def predict(months):
    # _validate_predict_params(months=months)
    # модель обчучена на пятидневках
    predictions = MODEL.predict(int(months)*7)
    return {"date": str(list(predictions.index)), "predict": list(predictions.values)}
