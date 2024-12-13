class State:
    states = ["main-menu", "tracker"]
    state = states[0]

    running = True

    @classmethod
    def change_state(cls, new_state: str):
        for s in cls.states:
            if new_state == s:
                cls.state = new_state

    @classmethod
    def power_state(cls, power_state: bool):
        cls.running = power_state
