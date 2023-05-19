from dfa import DFA
from tm import TuringMachine


def run_dfa():
    print("DFA")
    DFA().run()


def run_tm():
    print("Turing Machine")
    TuringMachine().run()


if __name__ == "__main__":
    choice = input("Which machine do you want to run? (dfa/tm): ")
    while choice.lower() != 'dfa' and choice.lower() != 'tm':
        choice = input("Invalid input. Which machine do you want to run? (dfa/tm): ")

    if choice.lower() == 'dfa':
        run_dfa()
    elif choice.lower() == 'tm':
        run_tm()
