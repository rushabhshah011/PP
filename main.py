import User

userDict = {}

def createUser(userID,name,email,mobileNumber): #Assumming that UserID will be given by authAPI

    if userID in userDict:
        print("User already exist!")
        return

    user = User.User(userID,name,email,mobileNumber)
    userDict[userID] = user

def isUserExist(userID):
    if userID in userDict:
        return True
    return False

def addExpense(amount,giver,taker):
    userDict[giver].balance += amount
    currentAmount = 0

    if taker in userDict[giver].owes:
        currentAmount = userDict[giver].owes[taker]
    currentAmount += amount
    userDict[giver].owes[taker] = currentAmount

    currentAmount = 0
    userDict[taker].balance -= amount
    if giver in  userDict[taker].owes:
        currentAmount = userDict[taker].owes[giver]
    currentAmount -= amount
    userDict[taker].owes[giver] = currentAmount

def showBalance():
    for userID in userDict:
        print(userDict[userID].name + " = " + str(userDict[userID].balance))


def showBalanceForUser(userID):
    for userID in userDict[userID].owes:
        print(userDict[userID].name + " = " + str(userDict[userID].balance))


def expenseHandler(expenseType,totalAmount,givers,giversAmount,takers,takersAmount= [],percentages = []):

    if totalAmount != sum(giversAmount):
        print("Invalid Amount Given!")
        return

    if expenseType == "EQUAL":
        totalTakers = len(takers) + len(givers)
        for giver, amount in zip(givers, giversAmount):
            for taker in takers:
                addExpense(amount/totalTakers,giver,taker)
            for otherGiver in givers:
                if giver != otherGiver:
                    addExpense(amount/totalTakers,giver,otherGiver)
    elif expenseType == "EXACT":
        totalTakers = len(takers) + len(givers)
        totalGivers = len(givers)
        calcTotalAmount = sum(takersAmount) + ((totalAmount/totalTakers)*totalGivers)
        if totalAmount == calcTotalAmount:
            for giver, amount in zip(givers, giversAmount):
                for taker, amount in zip(takers,takersAmount):
                    addExpense(amount/totalGivers,giver,taker)
        else:
            print("Invalid Amount Given!")
            return
    elif expenseType == "PERCENT" and len(percentages) > 0 and sum(percentages) == 100:
        totalGivers = len(givers)
        for percentage in percentages:
            takersAmount.append( (totalAmount*percentage) / 100)
        for giver, amount in zip(givers, giversAmount):
            for taker, amount in zip(takers,takersAmount):
                addExpense(amount/totalGivers,giver,taker)
    else:
        print("Invalid Expense Type!")
        return



createUser(1,"Rushabh","rushabhshah011@gmail.com","8128204578")
createUser(2,"Aman","aman011@gmail.com","8128204579")
createUser(3,"Aakash","aman011@gmail.com","8128204579")
createUser(4,"Nidhi","aman011@gmail.com","8128204579")
createUser(5,"Sidhi","aman011@gmail.com","8128204579")

expenseType1 = "EQUAL"
totalAmount1 = 100
givers1 = [1]
giversAmount1 = [100]
takers1 = [2,3]
expenseHandler(expenseType1,totalAmount1,givers1,giversAmount1,takers1)

showBalance()

# expenseType1 = "EXACT"
# totalAmount1 = 150
# givers1 = [1,2]
# giversAmount1 = [100,50]
# takers1 = [3,4,5]
# takersAmount1 = [40,40,10]
# expenseHandler(expenseType1,totalAmount1,givers1,giversAmount1,takers1,takersAmount1)

# showBalance()


# expenseType1 = "PERCENT"
# totalAmount1 = 100
# givers1 = [3]
# giversAmount1 = [100]
# takers1 = [3,4,5]
# takersPercentage1 = [40,40,20]
# expenseHandler(expenseType1,totalAmount1,givers1,giversAmount1,takers1,[],takersPercentage1)

# showBalance()

# addExpense(100,1,2)
# print(userDict[1].__dict__)
# print(userDict[2].__dict__)

# addExpense(10,2,1)
# print(userDict[1].__dict__)
# print(userDict[2].__dict__)

# showBalance()