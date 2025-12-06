from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# === === === === SQLITE === === === ===
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# === === === === POSTGRESQL === === === ===
SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:Pouri%401383@localhost/TodoApplicationDB"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# === === === === MYSQL === === === ===
# SQLALCHEMY_DATABASE_URL = (
#     "mysql+pymysql://root:Pouri%401383@localhost:3307/TodoApplicationDB"
# )
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
