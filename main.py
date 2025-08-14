from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    type: str
    origin: str
    repeat: bool

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Chai Aur Code"}

@app.get("/teas")
def read_teas():
    return teas

@app.post("/teas")
def post_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def put_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea ID not Found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            return_deleted_item = teas.pop(index)
            return return_deleted_item
    return {"error": "Tea ID not Found"}
