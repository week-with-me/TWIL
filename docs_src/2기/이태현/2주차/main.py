from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def test():
    return {"message": "pong"}
