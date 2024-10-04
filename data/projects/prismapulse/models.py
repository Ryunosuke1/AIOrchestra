from sqlalchemy import Column, Integer, String, Boolean, PickleType
from database import Base

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
