from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.week_one import router as week_one_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(week_one_router, prefix="/weekOne")


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050, debug=True)
