
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# from .database import engine

from .routers import post, user, auth, like


# models.Base.metadata.create_all(bind=engine)


app = FastAPI(title='Social Media Api', description='a social media api with all http methods, authentication routing and searching', version="1.0.1", )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(like.router)


@app.get("/")
def root():
    return {"Message": "Hello World"}
