class Bank:
    def __init__(self,cname,cid,accbalance):
        self.cname = cname
        self.cid = cid
        self.accbalance = accbalance

    def display(self):
        print("Customer name is: ",self.cname)
        print("Customer id is: ",self.cid)
        print("Current balance is: ",self.accbalance)

    def deposit(self,amount):
        self.accbalance+= amount
    
    def withdraw(self,amount):
        self.accbalance-= amount

C1 = Bank("Bleh",1234,25000)
C1.display()
C1.deposit(25000)
C1.withdraw(10000)
C1.display()