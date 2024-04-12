from backend import *



while True:
    print("1.Booking | 2.Cancel Ticket | 3. Modify seats | 4.Check revenue | 5. Booked tickets")
    print("6.Extend Stations | 0.Exit")
    choice = input("Enter your choice : ")
    if choice in "0123456":
        if choice == "1":
            booking()
        elif choice == "2":
            cancelTicket()
        elif choice == "3":
            modifySeat()
        elif choice == "4":
            checkRevenue()
        elif choice == "5":
            bookedSeats()
        elif choice == "6":
            extendStations()
        elif choice == "0":
            break
