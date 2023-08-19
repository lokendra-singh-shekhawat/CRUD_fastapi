from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://lokendra:lok121@localhost:3306/db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)