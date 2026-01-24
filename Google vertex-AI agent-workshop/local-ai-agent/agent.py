from llm import call_llm

class AIAgent:
    def __init__(self, goal):
        """
        Initialize agent with a goal
        """
        self.goal = goal
        self.plan = []
        self.memory = []
        self.final_answer = None
    def create_plan(self):
        """
        Ask the LLM to break the goal into steps
        """
        prompt = f"""
You are an AI planner.

Break this goal into simple steps.
Only list the steps, no explanations.

Goal:
{self.goal}
"""
        response = call_llm(prompt)
        # Split response into list of steps
        self.plan = [
            step.strip("- ").strip()
            for step in response.split("\n")
            if step.strip()
        ]
    def execute_step(self, step):
        """
        Execute one step using the LLM
        """
        prompt = f"""
You are an AI agent working on this goal:
{self.goal}

Current step:
{step}

Do the work for this step. Be short and concrete.
"""
        result = call_llm(prompt)
        self.memory.append(result)
        return result
    def is_finished(self):
        """
        Ask LLM if the goal is complete
        """
        prompt = f"""
Given the following work:

{self.memory}

Is the original goal fully completed? Answer yes or no.
"""
        answer = call_llm(prompt)
        return "yes" in answer.lower()
    def run(self):
        """
        Full agent loop: plan → act → stop
        """
        print("\nCreating plan...")
        self.create_plan()

        for step in self.plan:
            print(f"\nExecuting: {step}")
            self.execute_step(step)

            if self.is_finished():
                break

        self.final_answer = "\n".join(self.memory)
        return self.final_answer
