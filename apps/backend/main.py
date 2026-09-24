from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Report(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "SafeSignal API running"}

@app.post("/analyze")
async def analyze(report: Report):
    return {
        "category": "fare dispute",
        "tags": ["overcharging", "misconduct"],
        "severity": "medium",
        "summary": "Overcharging and rude conductor behavior reported."
    }