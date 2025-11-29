class payment:
    def __init__(self):
        self.total = 0

    def calculate(self):
        print("Please insert coins.")
        try:
            self.total += int(input("How many dinar?: ")) * 1.000
            self.total += int(input("How many half dinar?: ")) * 0.500
            self.total += int(input("How many 100 fils?: ")) * 0.100
            self.total += int(input("How many 50 fils?: ")) * 0.050
        except ValueError:
            print("Invalid input. Please enter numeric values for coins.")
            return self.calculate()
        
        return self.total