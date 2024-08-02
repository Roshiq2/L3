from railwayDatabase import *

while True:
    print("==================================")
    print(f"{RailwayDatabase.waitingList}: waiting list available")
    print("==================================")

    print("1. Book ticket || 2. Cancel Ticket || 3. ViewChart || 0. Exit")
    choice = input("Enter your choice : ")
    if choice in "1230":
        if int(choice) == 1:
            booking()
        elif int(choice) == 2:
            cancel()
        elif int(choice) == 3:
            chart()
        elif int(choice)==0:
            break
        else:
            print("Enter a valid input...")