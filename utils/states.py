class State:
    states = ["main-menu", "tracker"]
    state = states[0]

    @classmethod
    def change_state(cls, new_state: str):
        for s in cls.states:
            if new_state == s:
                cls.state = new_state
