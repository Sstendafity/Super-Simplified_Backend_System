from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import json
from datetime import datetime

app = FastAPI()

os.makedirs('data', exist_ok=True)

@app.get("/")
def root():
    return {"Welcome to Super-Simplified Backend System"}

@app.get("/send-json")
def send_json():
    sample_data = {
        "name" : "Elina Artawirya",
        "email" : "elartawirya@gmail.com",
        "registered" : True,
        "items" : ["pen", "book", "bottle"],
        "total_purchase" : 60000
    }
    return JSONResponse(content=sample_data)

@app.post("/receive-json")
async def receive_json(request: Request):
    data = await request.json()
    
    # Save data
    filename = datetime.now().strftime('received_data_%d%m%Y_%H%M%S.json')
    filepath = os.path.join('data', filename)
    with open(filepath, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return {"status": "success", "file_saved": filename}
    