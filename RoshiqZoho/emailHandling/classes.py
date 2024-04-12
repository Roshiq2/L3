class User:
    def __init__(self):
        self.userName = input("Enter your name : ")
        self.emailId = input("Enter your email-id : ")
        self.password = input("Enter your password : ")
        self.inboxList = []
        self.sentItems = []

class UserGroup:
    def __init__(self):
        self.groupName = input("Enter your group name : ")
        self.emailId = input("Enter your group mail-ID : ")
        self.password = input("Enter your group password : ")
        self.groupMembers = []
