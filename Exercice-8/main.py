from fastapi import FastAPI
from api.routes import router
from models.database import init_db

app = FastAPI(
    title="Jeu de cartes FastAPI",
    description="API pour manipuler un paquet de cartes",
    version="1.0"
)

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
