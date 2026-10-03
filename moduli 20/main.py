from fastapi import FastAPI

app = FastAPI()

@app.get("/")
#per me lan emrin e api,aka endpointin#
def root():
    return{"message":"Hello World!"}

@app.get("/greet")

def read_root(name:str):
    return{"message":f"Hello,{name}!"}

