from pydantic import BaseModel
from typing import Optional

class Iris(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

class IrisResponse(BaseModel):
    result : str
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float