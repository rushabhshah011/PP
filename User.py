class User:

    def __init__(self,userID, name, email,mobileNumber):
        self.userID = userID
        self.name = name
        self.email = email
        self.mobileNumber = mobileNumber
        self.balance = 0.0
        self.owes = {}

