from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres2:newpass@10.0.6.90:5432/new_1', echo=False)

# Create session to connect to DB
Session = sessionmaker(bind=engine)
session = Session()

# Create table
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# Send query for creation table
Base.metadata.create_all(engine)