data = {
    123456  : { 'pin ' : 1234, 'balance': 5000, 'history': [] },
    234567 : { 'pin ': 1234, 'balance' : 5678, 'history': [] },
    5678888 : { 'pin': 2345, 'balance':4567,'history': [] }
}

def menu():
    print('[C]heck balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew transaction')
    print('[E]xit')
def login():
    global acc_num
    acc_num = int(input("enter the account"))
    pin = int(input("enter the pin"))
    if acc_num in data and data [acc_num]['pin'] == pin:
        print("login successful")
    else:
        print("Invalid login")
        return False
def checkbalance():
    print("Current Balance :",data[acc_num]['balance'])

def deposit():
    amount = int(input("enter the amount :"))
    data[acc_num]['balance'] += amount
    print(f"{amount} is successfully deposited")
    data[acc_num]['history'].append(f'{amount} is deposited +++++++')
def withdraw( ):
    amount = int(input("enter the amount"))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance'] -= amount
        print(f'{amount} is successfully withdraw')
        data [acc_num]['history'].append(f'{amount} is withdraw--------')
    else:
        print("Insufficient balance")
def viewtransactions():
    if data[acc_num]['history']:
        print("-------------Transactional History-------------")
        for i in data[acc_num]['history']:
            print(i)
    else:
        print("No transaction History")
        
    

    
