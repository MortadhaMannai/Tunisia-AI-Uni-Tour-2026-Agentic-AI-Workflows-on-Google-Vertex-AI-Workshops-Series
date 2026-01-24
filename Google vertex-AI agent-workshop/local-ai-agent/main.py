from agent import AIAgent

goal = input("Enter a goal for the AI agent: ")

agent = AIAgent(goal)
result = agent.run()

print("\nFinal result:")
print(result)
