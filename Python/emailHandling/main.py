from backendServer import *

while True:
    print("1.CreateUser | 2.CreateGroup | 3.GroupAssignment | 4.ComposeMail | 5.Inbox | 6.SentMail | ")
    print("7.DeleteMail | 8.Recall | 9.ShareInbox | 0.Exit")
    choice = input("Enter your choice : ")
    if choice in "1234567":
        if choice == "1":
            createUser()
        elif choice == "2":
            createGroup()
        elif choice == "3":
            groupAssignment()
        elif choice == "4":
            composeMail()
        elif choice == "5":
            checkInbox()
        elif choice == "6":
            printsentItems()
        elif choice == "7":
            deletemail()
