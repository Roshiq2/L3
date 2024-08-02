from railwayDatabase import Railway
while True:
    print("1.Book ticket || 2.Cancel ticket ||3.TicketDetails || 0.Exit")
    choice = input("Enter your choice : ")
    if choice in "12340":
        if choice == "1":
            Railway.booking(1)
        elif choice == "2":
            pass
        elif choice =="3":
            Railway.printpassengerDetails(1)
        elif choice == "4":
            Railway.printRacpassenger(1)
        else:
            print("Enter a valid input. ")

