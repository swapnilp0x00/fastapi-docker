from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'a': 123}


print("Started")