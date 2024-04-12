import railwayDatabase


class Passenger:
    def __init__(self, berths):
        self.name = input("Enter your name : ")
        self.age = input("Enter your age : ")
        self.gender = input("Enter your gender M / F : ").upper()

        if self.gender == "F" and berths["L"]:
                self.berthPreference = "L"
        elif int(self.age) >=63:
            if railwayDatabase.berths["L"] > 0:
                self.berthPreference = "L"
                print("Assiging Lower berth : Senior citizen ")
        else:
            self.berthPreference = input("Enter your berth preference M | L | U : ").upper()
