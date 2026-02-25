from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

from schema.request import CreateTodoRequest

Base = declarative_base()


class ToDo(Base):
	__tablename__ = "todo"

	id = Column(Integer, primary_key=True, index=True)
	contents = Column(String(256), nullable=False)
	is_done = Column(Boolean, nullable=False)

	def __repr__(self):
		return f"ToDo(id={self.id}, contents={self.contents}, is_done={self.is_done})"

	@classmethod
	def create(cls, request: CreateTodoRequest) -> "ToDo":
		# 클래스 내부에서 자기 자신을 반환하는 메서드를 정의할 때, 해당 클래스가 아직 완전히 정의되지 않았기 때문에 타입 힌트에서 직접 사용할 수 없다.
		# 그렇기 때문에 문자열로 감싸서 사용한다.
		return cls(
				contents=request.contents,
				is_done=request.is_done,
		)

	def done(self) -> "ToDo":
		self.is_done = True
		return self

	def undone(self) -> "ToDo":
		self.is_done = False
		return self
