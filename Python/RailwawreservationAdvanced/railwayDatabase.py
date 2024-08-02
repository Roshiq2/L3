from collections import defaultdict
from passenger import Passenger
#is possible --> to check the seat availability from source to destination return a boolan value
class RailwayDatabase:
    pnr = 1
    stations = ['A', 'B', 'C', 'D', 'E']
    seatCount = {'A': 8, 'B': 8, 'C': 8, 'D': 8, 'E': 8}
    waitingList = 2
    journeyDetails = defaultdict(list)
    waitingListDetials = defaultdict(list)
def isPossible(source, destination):
    for i in range(ord(source), ord(destination) + 1):
        if RailwayDatabase.seatCount[chr(i)] <= 0:
            return False
    return True
def updateSeats(source, destination):
    for i in range(ord(source), ord(destination)+1):
        RailwayDatabase.seatCount[chr(i)] -= 1
def booking():
    pnr = RailwayDatabase.pnr
    source = input("Enter the source : ").upper()
    destination = input("Enter the destination : ").upper()
    seatsRequired = int(input("Enter the number of seats : "))
    while seatsRequired:
        if RailwayDatabase.waitingList<=0:
            print("there are no tickets available")
            print("=====================")
            break
        customer = Passenger(source, destination, pnr)
        if isPossible(source,destination):
            RailwayDatabase.journeyDetails[pnr].append(customer)
            print(f"PNR {pnr} : {source}==>{destination} has been booked")
            seatsRequired -= 1
            updateSeats(source, destination)
        elif RailwayDatabase.waitingList > 0:
            RailwayDatabase.waitingListDetials[pnr].append(customer)
            print(print(f"{pnr} : {source}==>{destination} has been booked in waiting list"))
            RailwayDatabase.waitingList -= 1
            seatsRequired -= 1

    RailwayDatabase.pnr += 1
    print(list(RailwayDatabase.journeyDetails.items()))
    print(list(RailwayDatabase.waitingListDetials.items()))
    return
def allocateForWaitingList():
    validID = defaultdict(list)
    for pnr, passengerList in RailwayDatabase.waitingListDetials.items():
        for i in range(len(passengerList)):
            customer = passengerList[i]
            if isPossible(customer.source,customer.destination):
                validID[pnr].append(i)
                RailwayDatabase.journeyDetails[pnr].append(customer)
                print(f"PNR {pnr} : {customer.source}==>{customer.destination} has been booked from waiting list.")
                RailwayDatabase.waitingList += 1
                updateSeats(customer.source, customer.destination)
    for pnr, val in validID.items():
        for i in val:
            RailwayDatabase.waitingListDetials[pnr].pop(i)
        if len(RailwayDatabase.waitingListDetials[pnr]) == 0:
            RailwayDatabase.waitingListDetials.pop(pnr)
def updateCancelledSeats(source, destination, seatType):
    if seatType == "waitingList":
        RailwayDatabase.waitingList += 1
        return
    else:
        for i in range(ord(source), ord(destination)+1):
            RailwayDatabase.seatCount[chr(i)] += 1
        print(f"1 seat has been added for the route {source}==>{destination}")
        allocateForWaitingList()
def cancel():
    print(list(RailwayDatabase.journeyDetails.keys()))
    ticketID = int(input("Enter your PNR number : "))
    seatsToCancel = int(input("Enter the number of seats to cancel : "))
    if ticketID in RailwayDatabase.journeyDetails:
        customer = RailwayDatabase.journeyDetails[ticketID].pop(0)
        while seatsToCancel:
            updateCancelledSeats(customer.source, customer.destination, "confirmedTicket")
            seatsToCancel -= 1
    elif ticketID in RailwayDatabase.waitingListDetials:
        customer = RailwayDatabase.waitingListDetials[ticketID].pop(0)
        while seatsToCancel:
            updateCancelledSeats(customer.source, customer.destination, "waitingList")
            seatsToCancel -= 1
    else:
        print("Enter a valid PNR details....")

def chart():
    seatList = {'A':[], 'B':[], 'C':[], 'D':[], 'E':[]}
    for pnr, passengerList in RailwayDatabase.journeyDetails.items():
        for i in range(len(passengerList)):
            customer = passengerList[i]
            source, destination = customer.source, customer.destination
            for seat in seatList:
                if ord(seat) >= ord(source) and ord(destination) <= ord(seat):
                    seatList[seat].append("*")
                else:
                    seatList[seat].append("_")
        for val in seatList:
            print(val, seatList[val])




