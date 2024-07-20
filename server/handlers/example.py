from pydantic import BaseModel
from fastapi import status, APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


class ExampleResponse(BaseModel):
    message: str


@router.get("/example")
def get_example():
    response = ExampleResponse(message="Hello World")

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response.model_dump(),
    )
