from http import server
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse


class ExampleResponse(BaseModel):
    message: str


@server.get("/example")
def get_example():
    response = ExampleResponse(message="Hello World")

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response.model_dump(),
    )
