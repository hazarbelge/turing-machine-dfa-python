class CustomHBMachine:
    def __init__(self):
        pass

    def custom_inputs(self):
        pass

    def predefined_inputs(self):
        pass

    def calculate(self, input_string):
        pass

    def run(self):
        choice = input("Do you want to use pre-defined inputs? (y/n): ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Invalid input. Do you want to use pre-defined inputs? (y/n): ")

        if choice.lower() == 'y':
            self.predefined_inputs()
        elif choice.lower() == 'n':
            self.custom_inputs()

        while True:
            input_string = input("Enter an input string: ")

            self.calculate(input_string)
            if input("Continue? (y/n) ") == "n":
                break
