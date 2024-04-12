from collections import defaultdict

from customer import Customer

bookingId = 100
sugePrice = 0
stations = ["chennai", "katpadi", "salem", "erode", "coimbatore"]
seatsAvailable = defaultdict(dict)
customerDetails = {}
revenue = 0
for i in range(len(stations)):
    seatsAvailable[i] = {}
    seatsAvailable[i]["normal"] = 0
    seatsAvailable[i]["premium"] = 0
def addSeatsInTrain(norm, pre):
    for i in range(len(stations)):
        seatsAvailable[i]["normal"] += norm
        seatsAvailable[i]["premium"] += pre
addSeatsInTrain(2, 2)  ## ALLOCATION FOR SINGLE COACH
def booking():
    for i in range(len(stations)):
        print(i, stations[i], end=" | ")
    print()
    fro = int(input("Enter the number of the station -- (FROM) : "))
    for i in range(int(fro) + 1, len(stations)):
        print(i, stations[i], end=" | ")
    print()
    to = int(input("To -- Enter the number of the station -- (TO) : "))
    coach = int(input("Enter 1.PREMIUM | 2.NORMAL : "))
    if coach == 1:
        seat = "premium"
    else:
        seat = "normal"
    for station in range(fro, to + 1):
        if seatsAvailable[station][seat] <= 0:
            print("TICKET COULD NOT BE PROCESSED")
            return
    for station in range(fro, to + 1):
        seatsAvailable[station][seat] -= 1
    global sugePrice, bookingId, revenue
    if seat == "premium":
        print(f"THE PRICE OF YOUR TICKET IS : {20 * (to - fro) + sugePrice}")
        revenue += (20 * (to - fro) + sugePrice)
        sugePrice += 5
    else:
        print(f"THE PRICE OF YOUR TICKET IS : {10 * (to - fro)}")
        revenue += 10 * (to - fro)
    print("SEAT BOOKED SUCCESSFULLY")
    cust = Customer(bookingId, fro, to, seat)
    customerDetails[bookingId] = cust
    bookingId += 1
def cancelTicket():
    global revenue
    print(f"{list(customerDetails.keys())} are the customer booking Id's available. ")
    bID = int(input("ENTER YOUR BOOKING-ID : "))
    customer = customerDetails[bID]
    fro, dest, seat = customer.fro, customer.to, customer.seat
    print(fro, dest, seat)
    print(seatsAvailable)
    for i in range(fro, dest + 1):
        if seat == "normal":
            seatsAvailable[i]["normal"] += 1
        else:
            seatsAvailable[i]["premium"] += 1
    if customer.seat == "premium":
        print(f"{(dest - fro) * 20} HAS BEEN REFUNDED SUCCESSFULLY")
        revenue -= (dest - fro) * 20
    else:
        print(f"{(dest - fro) * 10} HAS BEEN REFUNDED SUCCESSFULLY")
        revenue -= (dest - fro) * 10
    customerDetails.pop(bID)
    print(seatsAvailable)
def modifySeat():
    print("YOU ARE NOW SUPPOSED TO ADD COACH ")
    print("1.PREMIUM COACH | 2.NORMAL COACH")
    choice = input("Enter your choice : ")
    if choice == "1":
        addSeatsInTrain(0, 5)
    elif choice == "2":
        addSeatsInTrain(10, 0)
def checkRevenue():
    print(f'{revenue} has been totally obtained from this train so far...!!!')
def bookedSeats():
    for id in customerDetails:
        customer = customerDetails[id]
        print(f"{customer.seat} ticket has been booked from {customer.fro} --> to {customer.to}")
def extendStations():
    i = len(stations)
    name = input("Enter the staion name : ")
    stations.append(name)
    seatsAvailable[i] = {}
    seatsAvailable[i]["normal"] = 10
    seatsAvailable[i]["premium"] = 5