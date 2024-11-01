class IterativePrompter:
    def __init__(self):
        self.prompts = []

    def add_prompt(self, prompt):
        self.prompts.append(prompt)
        print(f"Prompt added: {prompt}")

    def refine_prompt(self, feedback):
        new_prompt = f"{self.prompts[-1]} with feedback: {feedback}"
        self.prompts.append(new_prompt)
        print(f"Refined prompt: {new_prompt}")

prompter = IterativePrompter()
prompter.add_prompt("Gather resources")
prompter.refine_prompt("Failed to find resources nearby")

