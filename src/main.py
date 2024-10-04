import autogen

def main():
    # Initialize the Autogen framework
    agent = autogen.Agent()

    # Define a simple multi-agent conversation
    agents = [agent, autogen.Agent()]
    conversations = [
        {"agent1": "Hello, how can I assist you?", "agent2": "I need help with my project."},
        {"agent1": "Sure, let's get started.", "agent2": "Great! Thanks."}
    ]

    # Simulate the conversation
    for conversation in conversations:
        agent.receive(conversation["agent1"])
        agents[1].receive(conversation["agent2"])

if __name__ == "__main__":
    main()
