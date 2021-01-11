from fastapi import FastAPI
from app.src.api.routes import router
import uvicorn


app = FastAPI(title="CountriesFilterAPI")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)
