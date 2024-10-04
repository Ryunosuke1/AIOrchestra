from pydantic import BaseModel, EmailStr
from typing import List, Optional

class AgentBase(BaseModel):
    name: str
    description: Optional[str] = None

class AgentCreate(AgentBase):
    pass

class AgentUpdate(AgentBase):
    name: Optional[str] = None
    description: Optional[str] = None

class ConversationFlowBase(BaseModel):
    flow_name: str
    agent_ids: List[int]
    conditions: Optional[dict] = None
    parallel_processes: Optional[bool] = False

class ConversationFlowCreate(ConversationFlowBase):
    pass
