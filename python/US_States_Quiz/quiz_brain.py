import pandas


class QuizBrain:
    def __init__(self):
        self.states = pandas.read_csv("50_states.csv")
        self.score = 0
        self.answered_states = []
        self.unanswered_states = self.states['state'].tolist()

    def check_state(self, state):
        coordinates = []
        if state in self.states.values:
            if state in self.answered_states:
                return False
            self.answered_states.append(state)
            state_row = self.states[self.states["state"] == state]
            coordinates.append(int(state_row.x))
            coordinates.append(int(state_row.y))
            return coordinates
        return False

    def game_end(self):
        for state in self.answered_states:
            self.unanswered_states.remove(state)
        data_frame = pandas.DataFrame(self.unanswered_states)
        data_frame.to_csv('missed_states.csv', mode="w")
