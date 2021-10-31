from fastapi  import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Posts(BaseModel):
    title: str
    content: str

    
@app.get("/ping")
def test():
    return {"message": "pong"}


@app.post("/posts")
def create_posts(post: Posts):
    return post