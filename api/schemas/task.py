from typing import Optional

from pydantic import BaseModel,Field

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Pow(BaseModel):
    input: int
    ans: int



class Deadline(TaskBase):
    pass