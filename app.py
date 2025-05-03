from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.week_one import router as week_one_router
from routes.week_two import router as week_two_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(week_one_router, prefix="/weekOne")
app.include_router(week_two_router, prefix="/weekTwo")


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}
