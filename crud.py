from models import Agent, ConversationFlow
from schemas import AgentCreate, AgentUpdate, ConversationFlowCreate

def create_agent(db: Session, agent: AgentCreate):
    db_agent = Agent(name=agent.name, description=agent.description)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def get_agent(db: Session, agent_id: int):
    return db.query(Agent).filter(Agent.id == agent_id).first()

def update_agent(db: Session, db_obj: Agent, agent: AgentUpdate):
    for key, value in agent.dict(exclude_unset=True).items():
        setattr(db_obj, key, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_agent(db: Session, id: int):
    db.query(Agent).filter(Agent.id == id).delete(synchronize_session=False)
    db.commit()

def create_conversation_flow(db: Session, conversation_flow: ConversationFlowCreate):
    db_conversation_flow = ConversationFlow(flow_name=conversation_flow.flow_name, agent_ids=conversation_flow.agent_ids, conditions=conversation_flow.conditions, parallel_processes=conversation_flow.parallel_processes)
    db.add(db_conversation_flow)
    db.commit()
    db.refresh(db_conversation_flow)
    return db_conversation_flow

def get_conversation_flow(db: Session, id: int):
    return db.query(ConversationFlow).filter(ConversationFlow.id == id).first()

def update_conversation_flow(db: Session, id: int, conversation_flow: ConversationFlowCreate):
    db_conversation_flow = db.query(ConversationFlow).filter(ConversationFlow.id == id).first()
    for key, value in conversation_flow.dict(exclude_unset=True).items():
        setattr(db_conversation_flow, key, value)
    db.add(db_conversation_flow)
    db.commit()
    db.refresh(db_conversation_flow)
    return db_conversation_flow

def remove_conversation_flow(db: Session, id: int):
    db.query(ConversationFlow).filter(ConversationFlow.id == id).delete(synchronize_session=False)
    db.commit()

