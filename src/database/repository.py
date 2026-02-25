from typing import List

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database.connection import get_db
from database.orm import ToDo


class ToDoRepository:
	def __init__(self, session: Session = Depends(get_db)):
		self.session = session

	def get_todos(self) -> List[ToDo]:
		return list(self.session.scalars(select(ToDo)))

	def get_todo_by_todo_id(self, todo_id: int) -> ToDo | None:
		return self.session.scalar(select(ToDo).where(ToDo.id == todo_id))

	def create_todo(self, todo: ToDo) -> ToDo:
		self.session.add(instance=todo)  # session 객체에 변경되어야 할 데이터가 쌓이게 된다.
		self.session.commit()  # 실제로 DB 에 데이터를 반영하는 쿼리가 날라가게된다.
		self.session.refresh(
				instance=todo)  # todo 객체를 다시 읽어오게 된다. todo 에 담게 된다.
		return todo

	def update_todo(self, todo: ToDo) -> ToDo:
		self.session.add(instance=todo)
		self.session.commit()
		self.session.refresh(instance=todo)
		return todo

	def delete_todo(self, todo_id: int) -> None:
		self.session.execute(delete(ToDo).where(ToDo.id == todo_id))
		self.session.commit()
