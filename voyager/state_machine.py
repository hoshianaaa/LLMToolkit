class StateMachine:
    def __init__(self):
        self.state = "idle"

    def transition(self, new_state):
        print(f"Transitioning from {self.state} to {new_state}")
        self.state = new_state

    def act(self):
        if self.state == "idle":
            print("Standing by.")
        elif self.state == "exploring":
            print("Exploring the environment.")

# 状態遷移の例
state_machine = StateMachine()
state_machine.act()
state_machine.transition("exploring")
state_machine.act()

