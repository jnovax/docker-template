from typing import Union
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{full_path:path}")
def read_other(req: Request, full_path: str):
    return {"path": full_path}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
