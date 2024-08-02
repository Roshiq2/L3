from passenger import Passenger

berths = {"L": 1, "U": 1, "M": 1}
availableTickets = 3
passengerDetails = {}
rac = 1
racPassengerList = []
wl = 1
wlPassengerList = []
id = 1


class Railway:
    def booking(self):
        global availableTickets, id, racPassengerList, rac, wl, wlPassengerList
        person = Passenger(berths)
        # Checking if the passenger is a child and direcitly adding in the passenger details
        if int(person.age) <= 5:
            passengerDetails[id] = person
            person.berthPreference = "Child"
            id += 1
        # checking if the desired berth is available and allocating the seat
        elif berths[person.berthPreference]:
            berths[person.berthPreference] -= 1
            availableTickets -= 1
            passengerDetails[id] = person
            id += 1
        # checking if any berth seats is available and alocating it
        elif availableTickets:
            for berth in berths:
                if berths[berth]:
                    berths[berth] -= 1
                    print(f"{person.berthPreference} is not available || {berth} is alloted.")
                    break
            availableTickets -= 1
            passengerDetails[id] = person
            id += 1
        elif rac:
            print("Currently there are no tickets available")
            racPassengerList.append(person)
            rac -= 1
            print("Rac ticket booked")

        elif wl:
            print("currenty there are no confirm or Rac tickets available")
            wlPassengerList.append(person)
            wl -= 1
            print("Booked a waiting list")
        else:
            print("There are no tickets available.")

    def printpassengerDetails(self):
        global passengerDetails, berths
        if not passengerDetails:
            print("Currently there are no bookings done.")
        else:
            print("Printing passenger details")
            for bookingId in passengerDetails:
                passenger = passengerDetails[bookingId]
                print(f"{passenger.name}|Age:{passenger.age}|Berth:{passenger.berthPreference}")

        for berth in berths:
            if berths[berth] > 0:
                print(f'{berth} Berth : {berths[berth]} seats available')

    def printWlPassenger(self):
        for passenger in wlPassengerList:
            print(f"{passenger.name}|Age:{passenger.age}|Berth:{passenger.berthPreference}")

    def cancelTicket(self):
        pass
