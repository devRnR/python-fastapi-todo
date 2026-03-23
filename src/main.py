from fastapi import FastAPI

from api import todo

app = FastAPI()
app.include_router(todo.router)


@app.get("/health")
def health_check_handler():
	return {"ping": "pong"}
