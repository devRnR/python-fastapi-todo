from typing import List

from pydantic import BaseModel, ConfigDict


class ToDoSchema(BaseModel):
	id: int
	contents: str
	is_done: bool

	model_config = ConfigDict(from_attributes=True) # pydantic 이 sqlalchemy 의 orm 객체를 해석하기 위해서 필요한 configuration


class ToDoListSchema(BaseModel):
	todos: List[ToDoSchema]