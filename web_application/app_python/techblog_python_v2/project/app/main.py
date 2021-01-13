from fastapi import FastAPI
import uvicorn
from api.routes.api import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
