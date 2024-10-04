from sqlalchemy import create_engine, Column, Integer, String, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Agent(Base):
    __tablename__ = "agents"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)

class ConversationFlow(Base):
    __tablename__ = "conversation_flows"

    id = Column(Integer, primary_key=True, index=True)
    flow_name = Column(String, index=True, nullable=False)
    agent_ids = Column(PickleType)
    conditions = Column(PickleType)
    parallel_processes = Column(Boolean)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

