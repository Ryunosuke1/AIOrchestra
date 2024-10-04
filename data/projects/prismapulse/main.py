from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
from database import get_db
from schemas import AgentCreate, AgentUpdate, ConversationFlowCreate
from crud import agent_crud, conversation_flow_crud

app = FastAPI()

# CORS middleware setup
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://prismapulse.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Dependency
def get_current_agent(db: Session = Depends(get_db), agent_id: int = None):
    if not agent_id:
        raise HTTPException(status_code=400, detail="Agent ID is required")
    
    db_agent = agent_crud.get_agent(db, agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@app.post("/agents/", response_model=models.Agent)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    return agent_crud.create_agent(db=db, agent=agent)

@app.get("/agents/{agent_id}", response_model=models.Agent)
def read_agent(agent_id: int, current_agent: models.Agent = Depends(get_current_agent), db: Session = Depends(get_db)):
    return current_agent

@app.put("/agents/{agent_id}", response_model=models.Agent)
def update_agent(agent_id: int, agent: AgentUpdate, current_agent: models.Agent = Depends(get_current_agent), db: Session = Depends(get_db)):
    return agent_crud.update_agent(db=db, db_obj=current_agent, agent=agent)

@app.delete("/agents/{agent_id}")
def delete_agent(agent_id: int, current_agent: models.Agent = Depends(get_current_agent), db: Session = Depends(get_db)):
    agent_crud.remove_agent(db=db, id=agent_id)
    return {"detail": "Agent deleted successfully"}

# Conversation Flow API
@app.post("/conversation-flows/", response_model=models.ConversationFlow)
def create_conversation_flow(conversation_flow: ConversationFlowCreate, db: Session = Depends(get_db)):
    return conversation_flow_crud.create_conversation_flow(db=db, conversation_flow=conversation_flow)

@app.get("/conversation-flows/{conversation_flow_id}", response_model=models.ConversationFlow)
def read_conversation_flow(conversation_flow_id: int, current_agent: models.Agent = Depends(get_current_agent), db: Session = Depends(get_db)):
    return conversation_flow_crud.get_conversation_flow(db=db, id=conversation_flow_id)

@app.put("/conversation-flows/{conversation_flow_id}", response_model=models.ConversationFlow)
def update_conversation_flow(conversation_flow_id: int, conversation_flow: ConversationFlowCreate, current_agent: models.Agent = Depends(get_current_agent), db: Session = Depends(get_db)):
    return conversation_flow_crud.update_conversation_flow(db=db, id=conversation_flow_id, conversation_flow=conversation_flow)

@app.delete("/conversation-flows/{conversation_flow_id}")
def delete_conversation_flow(conversation_flow_id: int, current_agent: models.Agent = Depends(get_current_agent), db: Session = Depends(get_db)):
    conversation_flow_crud.remove_conversation_flow(db=db, id=conversation_flow_id)
    return {"detail": "Conversation Flow deleted successfully"}
