from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# Update the database URL to use users.db
DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False, index=True)
    lastname = Column(String, nullable=False, index=True)
    nin = Column(String, nullable=True)
    phone_no = Column(String, nullable=True)
    next_of_kin = Column(String, nullable=False)
    next_of_kin_phone_no = Column(String, nullable=False)
    district = Column(String, nullable=False)
    subcounty = Column(String, nullable=False)
    parish = Column(String, nullable=False)
    village = Column(String, nullable=False)
    residence = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
