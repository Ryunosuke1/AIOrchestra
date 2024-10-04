from fastapi import FastAPI
import autogen_agentchat as agentchat

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

@app.post("/agents/", response_model=dict)
def create_agent():
    agent = agentchat.Agent()
    return {"agent": agent}

@app.get("/agents/{agent_id}", response_model=dict)
def read_agent(agent_id):
    return {"agent_id": agent_id, "agent": {}}

@app.put("/agents/{agent_id}", response_model=dict)
def update_agent(agent_id):
    return {"agent_id": agent_id, "agent": {}}

@app.delete("/agents/{agent_id}")
def delete_agent(agent_id):
    return {"detail": f"Agent {agent_id} deleted"}
