import bentoml
import numpy as np
from bentoml.io import JSON
from bentoml.io import NumpyNdarray


from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")
#dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("mlzoomcamp_homework_classifier", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify(vector) -> np.ndarray:
    prediction = model_runner.predict.async_run(vector)
    print(prediction)
    return await prediction