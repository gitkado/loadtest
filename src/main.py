from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginParam(BaseModel):
    username: str
    password: str


@app.get("/hello_world")
async def hello_world():
    return {"Hello World"}


@app.get("/item")
async def view_item(item_id: int):
    return item_id

# 下記を追加
@app.post("/login")
async def login(login_param: LoginParam):
    return {login_param.username: login_param.password}
