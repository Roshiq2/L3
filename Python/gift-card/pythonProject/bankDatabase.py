from collections import defaultdict

customerDetails = {}
giftCardDatabase = {}
transactionHistory = defaultdict(list)
redeemPoint = {}
def updateTransaction(cardnumber, amountUsed):
    transactionHistory[cardnumber].append(f'{amountUsed} has been spent on card Number {cardnumber}')
    # if amountUsed >= 10:
    #     point = amountUsed / 10
    #     redeemPoint[cardnumber] = redeemPoint.get(cardnumber, 0) + point
    #     for cust in customerDetails:
    #         cust.updateRedeemPoints()
def updateTopUpTransaction(cardNumber, amountUsed, topup):
    transactionHistory[cardNumber].append(f'{amountUsed} has been used for topup')
