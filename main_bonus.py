from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
import os
import json

app = FastAPI()

os.makedirs('data', exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic model
class UserData(BaseModel):
    name : str
    email : str
    registered : bool
    items : list[str]
    total_purchase : float

@app.get("/", response_class=HTMLResponse)
def get_homepage():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/send-json")
def send_json():
    return {
        "name" : "Elina Artawirya",
        "email" : "elartawirya@gmail.com",
        "registered" : True,
        "items" : ["pen", "book", "bottle"],
        "total_purchase" : 60000
    }

@app.post("/receive-json")
async def receive_json(data: UserData):
    filename = datetime.now().strftime('received_data_%d%m%Y_%H%M%S.json')
    filepath = os.path.join('data', filename)

    with open(filepath, 'w') as f:
        json.dump(data.dict(), f, indent=4)
    return {"status": "success", "file_saved": filename}
    