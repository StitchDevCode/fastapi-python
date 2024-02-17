from typing import Text, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    create_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


# Define una ruta y una función que manejará las solicitudes a esa ruta
@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/post")
def post_posts(post: Post):
    post.id = str(uuid())  # Generar un nuevo ID
    posts.append(post.dict())
    return posts[-1]

@app.get("/posts/{post_id}")
def get_post():
    return "Funciona"

# Si ejecutamos este script directamente, arrancaremos el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)