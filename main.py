from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Merhaba Docker,Kubernate,Argo!"}
