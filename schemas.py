from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class AgentBase(BaseModel):
    name: str = Field(..., description="Name of the agent")
    description: Optional[str] = Field(None, description="Description of the agent")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")

class AgentCreate(AgentBase):
    owner_id: int = Field(..., description="ID of the user creating the agent")
    
    def __init__(self, **data):
        super().__init__(**data)
        print(f"Creating new agent: {self.name}")
    
    def update_description(self, new_description: str):
        self.description = new_description
        self.updated_at = datetime.utcnow()
        print(f"Updated description for agent {self.name}")
    
    def display_agent(self):
        print(f"Agent: {self.name}")
        print(f"Description: {self.description}")
        print(f"Created at: {self.created_at}")
        print(f"Updated at: {self.updated_at}")
        print(f"Owner ID: {self.owner_id}")

class AgentUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Updated name of the agent")
    description: Optional[str] = Field(None, description="Updated description of the agent")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")

    def __init__(self, **data):
        super().__init__(**data)
        print(f"Updating agent")

    def apply_update(self, agent: AgentBase):
        updated = False
        if self.name is not None and self.name != agent.name:
            agent.name = self.name
            updated = True
        if self.description is not None and self.description != agent.description:
            agent.description = self.description
            updated = True
        if updated:
            agent.updated_at = self.updated_at
            print(f"Agent updated: {agent.name}")
        else:
            print("No changes to apply")

    def display_update(self):
        print("Agent Update:")
        if self.name is not None:
            print(f"  New name: {self.name}")
        if self.description is not None:
            print(f"  New description: {self.description}")
        print(f"  Update timestamp: {self.updated_at}")


class ConversationFlowBase(BaseModel):
    title: str = Field(..., description="Title of the conversation flow")
    description: Optional[str] = Field(None, description="Description of the conversation flow")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    steps: List[str] = Field(default_factory=list, description="List of conversation steps")

class ConversationFlowCreate(ConversationFlowBase):
    owner_id: int = Field(..., description="ID of the user creating the conversation flow")
    
    def __init__(self, **data):
        super().__init__(**data)
        print(f"Creating new conversation flow: {self.title}")
    
    def add_step(self, step: str):
        self.steps.append(step)
        self.updated_at = datetime.utcnow()
        print(f"Added step to {self.title}: {step}")
    
    def remove_step(self, index: int):
        if 0 <= index < len(self.steps):
            removed_step = self.steps.pop(index)
            self.updated_at = datetime.utcnow()
            print(f"Removed step from {self.title}: {removed_step}")
        else:
            print(f"Invalid step index: {index}")
    
    def display_flow(self):
        print(f"Conversation Flow: {self.title}")
        print(f"Description: {self.description}")
        print(f"Created at: {self.created_at}")
        print(f"Updated at: {self.updated_at}")
        print("Steps:")
        for i, step in enumerate(self.steps, 1):
            print(f"  {i}. {step}")

