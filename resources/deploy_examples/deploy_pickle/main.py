import pandas as pd
import pickle5 as pickle
from fastapi import FastAPI
from schemas import Iris, IrisResponse
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"detail":"please make a post request to /predict"}


@app.post('/predict/', response_model=IrisResponse)
def predict(request: Iris):
    data = dict(request)
    sepal_length = request.sepal_length
    sepal_width = request.sepal_width
    petal_length = request.petal_length
    petal_width = request.petal_width
    # for python 3.6
    with open("model/new_model.pickle", "rb") as fh:
        model = pickle.load(fh)

    # for python 3.8
    # model = pd.read_pickle("model/new_model.pickle")
    
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    classification = result[0]
    data['result'] = classification
    return data
    # return data


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)