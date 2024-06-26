from pydantic import BaseModel, Field, HttpUrl


class MemeData(BaseModel):
    id: int = Field(gt=0)
    text: str
    url: HttpUrl
    tags: list
    info: object
