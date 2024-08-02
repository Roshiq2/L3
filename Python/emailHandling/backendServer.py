from classes import *

users = {}
userGroups = {}


def createUser():
    newUser = User()
    users[newUser.emailId] = newUser
    print("=======Displaying the users=======")
    for i in users:
        user = users[i]
        print(user.userName, end=" | ")
    print()
    print("-----------------------------------")


def createGroup():
    newGroup = UserGroup()
    userGroups[newGroup.groupName] = newGroup


def groupAssignment():
    for i in userGroups:
        userGroup = userGroups[i]
        print(userGroup.groupName, userGroup.emailId)
    groupMailId = input("Enter the group email id : ")
    group = userGroups[groupMailId]
    while True:
        print("1.AddUser | 2.DeleteUser | 3.viewMembers | 0.Exit")
        choice = input("Enter your choice : ")
        if choice in "1230":
            if choice == "1":
                for i in users:
                    user = users[i]
                    print(user.emailId, end=" | ")
                print()
                mailId = input("Enter the emailId to add the user : ")
                group.groupMembers.append(mailId)
                print("User Added")

            elif choice == "2":
                for i in users:
                    user = users[i]
                    print(user.emailId, end=" | ")
                print()
                mailId = input("Enter the emailId to delete the user : ")
                group.groupMembers.remove(mailId)
                print("User Deleted")
            elif choice == "3":
                if len(group.groupMembers) == 0:
                    print("There are no members in this group....")
                else:
                    print("Printing the groupMemebers in this group")
                    for i in group.groupMembers:
                        print(i, end=" | ")
                    print()
            elif choice == "0":
                break


def composeMail():
    sender = input("Enter the from address mailId : ")
    to = input("Enter the to address :")
    subject = input("Subject :")
    print("Enter the content of the mail.")
    content = input()
    if to in userGroups:
        userGroup = userGroups[to]
        for member in userGroup.groupMembers:
            member.inboxList.append([subject,content, sender])
    else:
        user = users[to]
        user.inboxList.append([subject,content, sender])
    user = users[sender]
    user.sentItems.append([subject,content, to])
    print("===Returning to the main page===")
def checkInbox():
    print("---------User Login---------")
    email = input("Enter the user emailId : ")
    user = users[email]
    if len(user.inboxList)==0:
        print("Your inbox is empty")
    else:
        for i in user.inboxList:
            subject, content, sender = i
            print(f'from {sender} : subject {subject} : content {content}')
    print("===Returning to the main page===")

def printsentItems():
    print("---------User Login---------")
    email = input("Enter the user emailId : ")
    user = users[email]
    if len(user.sentItems) == 0:
        print("You have sent 0 messages")
    else:
        for i in user.sentItems:
            subject, content, sender = i
            print(f'subject {subject}: {content}')

def deletemail():
    print("---------User Login---------")
    email = input("Enter the user emailId : ")
    user = users[email]
    for i in user.sentItems:
        subject, content, sender = i
        print(f'subject {subject}: {content}')
    subjectTodelete = input("enter the subject of the mail to delete : ")
    for i in user.sentItems:
        sentsubject, content, to = i
        if subject == subjectTodelete:
            recepiant = users[to]
            for data in recepiant.inboxList:
                inboxsubject, content, sender = data
                if sentsubject == inboxsubject:
                    recepiant.inboxList.remove(data)
                    break

    for i in user.sentItems:
        subject, content, sender = i
        if subject == subjectTodelete:
            user.sentItems.remove(i)
            break
    print(f'subject {subjectTodelete} mail has been delted to the user')