from fastapi import FastAPI

router = FastAPI()


@router('/hello')
def greetings():
    return 'Hello_World'