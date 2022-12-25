from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_database.db', echo=False)

Base = declarative_base()

class Views(Base):
    __tablename__ = 'views'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    view_id = Column(Integer)

    def __init__(self, user_id, view_id):
        self.user_id = user_id
        self.view_id = view_id

    def get(self):
        return self.view_id


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
