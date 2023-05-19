from base import CustomHBMachine


class TuringMachine(CustomHBMachine):
    def __init__(self):
        super().__init__()

        self.states = []
        self.alphabet = []
        self.blank_symbol = None
        self.input_symbols = []
        self.initial_state = ""
        self.accept_state = ""
        self.reject_state = ""
        self.transition_function = {}

    def custom_inputs(self):
        super().custom_inputs()

        self.states = input("Enter the states (separated by commas): ").split(',')
        self.alphabet = input("Enter the alphabet (separated by commas): ").split(',')
        self.blank_symbol = input("Enter the blank symbol: ")
        self.input_symbols = input("Enter the input symbols (separated by commas): ").split(',')
        self.initial_state = input("Enter the initial state: ")
        self.accept_state = input("Enter the accept state: ")
        self.reject_state = input("Enter the reject state: ")
        print("Define the transition function:")
        for state in self.states:
            for symbol in self.alphabet:
                next_state = input(f"From state {state} on symbol {symbol}, next state: ")
                write_symbol = input(f"Symbol to write: ")
                move_direction = input(f"Move direction (L/R): ")
                self.transition_function[(state, symbol)] = (next_state, write_symbol, move_direction)

    def predefined_inputs(self):
        super().predefined_inputs()

        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['0', '1', 'b']
        self.blank_symbol = 'b'
        self.input_symbols = ['0', '1']
        self.initial_state = 'q0'
        self.accept_state = 'q2'
        self.reject_state = 'q1'
        self.transition_function = {
            ('q0', '0'): ('q2', '1', 'R'),
            ('q0', '1'): ('q0', '0', 'R'),
            ('q0', 'b'): ('q1', 'b', 'R'),
            ('q1', '0'): ('q1', '0', 'L'),
            ('q1', '1'): ('q2', '1', 'L'),
            ('q1', 'b'): ('q1', 'b', 'L'),
            ('q2', '0'): ('q2', '0', 'R'),
            ('q2', '1'): ('q2', '1', 'R'),
            ('q2', 'b'): ('q1', 'b', 'R')
        }

    def calculate(self, input_string):
        super().calculate(input_string)

        tape = list(input_string)
        head_position = 0
        current_state = self.initial_state
        while current_state != self.accept_state and current_state != self.reject_state:
            if head_position < 0 or head_position >= len(tape):
                tape.append(self.blank_symbol)
            current_symbol = tape[head_position]
            action = self.transition_function.get((current_state, current_symbol))

            if action is None:
                print("Invalid transition.")
                return

            next_state, write_symbol, move_direction = action
            tape[head_position] = write_symbol

            if move_direction == 'R':
                head_position += 1
            elif move_direction == 'L':
                head_position -= 1
            else:
                print("Invalid direction.")
                return

            current_state = next_state
            print(f"On symbol {current_symbol}, write {write_symbol}, move {move_direction}, next state {next_state}")

        if current_state == self.accept_state:
            print("Input accepted.")
        else:
            print("Input rejected.")

    def run(self):
        super().run()
