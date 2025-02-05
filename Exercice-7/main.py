from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Card Game API", description="API pour manipuler un paquet de cartes", version="1.0")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
