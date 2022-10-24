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

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
#dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("mlzoomcamp_homework_classifier", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(vector) -> np.ndarray:
    prediction = model_runner.predict.run(vector)
    print(prediction)
    return prediction


# def classify(vector):
#     #application_data = user_profile.dict()
#     #vector = dv.transform(application_data)
#     prediction = model_runner.predict.run(vector)
#     print(prediction)

#     result = prediction[0]

    # if result > 0.5:
    #     return {"status" : "DECLINED"}
    # elif result > 0.23:
    #     return {"status" : "MAYBE"}
    # else:
    #     return {"status" : "APPROVED"}
