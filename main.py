import uvicorn
from fastapi import FastAPI

from app.core.config import Base, engine
from app.routers import answer, question

app = FastAPI()

app.include_router(question.router, prefix="/questions", tags=["questions"])
app.include_router(answer.router, prefix="", tags=["answers"])


@app.on_event("startup")
async def startup():
    """
    Выполняется при запуске приложения.
    Подключает к базе данных.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    """
    Выполняется при остановке приложения.
    Отключает от базы данных.
    """
    await engine.dispose()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8020, reload=True)
