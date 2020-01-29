from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class Restaurant(Base):
   __tablename__ = 'restaurants'
   id = Column(Integer, primary_key=True)
   Name = Column(String)
   Location = Column(String)
   Foods = Column(String)
