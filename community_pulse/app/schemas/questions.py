from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: int
    name: str = Field(..., min_length=1)


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=5)
    category: CategoryBase


class QuestionResponse(BaseModel):
    id: int
    text: str
    category: CategoryBase

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    message: str

    class Config:
        from_attributes = True
