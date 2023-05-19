from base import CustomHBMachine


class DFA(CustomHBMachine):
    def __init__(self):
        super().__init__()

        self.states = []
        self.alphabet = []
        self.transition_function = {}
        self.start_state = ""
        self.accept_states = []

    def custom_inputs(self):
        super().custom_inputs()

        self.states = input("Enter the states (separated by commas): ").split(',')
        self.alphabet = input("Enter the alphabet (separated by commas): ").split(',')
        self.start_state = input("Enter the start state: ")
        self.accept_states = input("Enter the accept states (separated by commas): ").split(',')

        print("Define the transition function:")
        for state in self.states:
            for letter in self.alphabet:
                next_state = input(f"From state {state} on input {letter}, go to: ")
                self.transition_function[(state, letter)] = next_state

    def predefined_inputs(self):
        super().predefined_inputs()

        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['0', '1']
        self.start_state = 'q0'
        self.accept_states = ['q2']
        self.transition_function = {
            ('q0', '0'): 'q0',
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q0',
            ('q2', '0'): 'q2',
            ('q2', '1'): 'q2'
        }

    def calculate(self, input_string):
        super().calculate(input_string)

        current_state = self.start_state
        print(f"Start state: {current_state}")
        for letter in input_string:
            current_state = self.transition_function.get((current_state, letter))
            if current_state is None:
                print("Invalid input.")
                return

            print(f"On input {letter}, transitioned to {current_state}")

        if current_state in self.accept_states:
            print("Input accepted.")
        else:
            print("Input rejected.")

    def run(self):
        super().run()
