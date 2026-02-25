from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:qwer1234@127.0.0.1:3306/todos"

engine = create_engine(DATABASE_URL, echo=True) # echo = True | spring 의 show_sql 과 같음
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
	session  = SessionFactory()
	try:
		yield session
	finally:
		session.close()

'''
from sqlalchemy import create_engine

DB_USER = "root"
DB_PASS = "your_password"
DB_HOST = "db"  # Docker에서는 서비스 이름
DB_NAME = "test_db"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
engine = create_engine(DATABASE_URL)
'''