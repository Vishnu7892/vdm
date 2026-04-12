from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MachineData(BaseModel):
    temperature: float
    vibration: float

@app.post("/predict")
def predict(data: MachineData):
    if data.temperature > 90:
        return {
            "issue": "Overheating",
            "risk": 85
        }
    return {
        "issue": "Normal",
        "risk": 10
    } 