from fastapi import FastAPI
from .routers import task, user

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': "Welcome to TaskManager"}


app.include_router(user.router)
app.include_router(task.router)  # позволяет подключать дополнительные внешние роутеры


# запуск
# в терминале ввод python -m uvicorn Python_Homework.Module17.homework1m17_pydantic.app.main:app