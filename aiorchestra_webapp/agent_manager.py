from typing import Dict

class AgentManager:
    def __init__(self):
        self.agents: Dict[str, dict] = {}

    def add_agent(self, agent: dict) -> None:
        """
        Adds a new agent to the manager.

        Args:
            agent (dict): The agent dictionary containing agent details.
        """
        if not isinstance(agent, dict):
            raise ValueError("Agent must be a dictionary.")
        self.agents[agent['id']] = agent

    def remove_agent(self, agent_id: str) -> None:
        """
        Removes an agent from the manager.

        Args:
            agent_id (str): The ID of the agent to remove.
        """
        if agent_id not in self.agents:
            raise ValueError("Agent with the given ID does not exist.")
        del self.agents[agent_id]

    def get_agent(self, agent_id: str) -> dict:
        """
        Retrieves an agent by its ID.

        Args:
            agent_id (str): The ID of the agent to retrieve.

        Returns:
            dict: The agent dictionary.
        """
        if agent_id not in self.agents:
            raise ValueError("Agent with the given ID does not exist.")
        return self.agents[agent_id]
