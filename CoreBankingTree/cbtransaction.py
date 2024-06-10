import datetime

class Transaction:
    codeList = {"11":"Deposit", "12":"Interest", "13":"Rebate", "14":"Cashback", "21": "Withdraw", "22":"Withholding Tax", "23":"Admin Fee"}
    codeSign = {"11":1, "12":1, "13":1, "14":1, "21":-1, "22":-1, "23":-1}
    
    #pastikan code ada dalam codeList
    def __init__(self, txid, cabang, code, amount):
        self.date = datetime.date.today()
        self.txid = txid
        self.cabang = cabang
        self.code = code
        self.amount = amount*self.codeSign[code]
        self.timestamp = datetime.datetime.now()
        
    def show(self):
        print("Date:", self.date)
        print("Code:", self.code)
        print("Amount:", f'{self.amount:,}')
        print("Timestamp:", self.timestamp)
        
    def print(self):
        print(self.date, self.code.rjust(4), f'{self.amount:,}'.rjust(15), str(self.txid).ljust(15), self.timestamp)
        
class TransactionNode:
    def __init__(self, transaction):
        self.transaction=transaction
        self.next = None
        
class LinkedListTransaction:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
        
    def newTransaction(self, cabang, code, amount):
        self.count+=1
        transaction=Transaction(self.count, cabang, code, amount)
        newNode = TransactionNode(transaction)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return transaction
            
    def list(self):
        lastPosition=self.head
        print("\n\n>>DAFTAR TRANSAKSI\n")
        print("-"*(70+4))
        print("Tanggal".ljust(10),"Code","Amount".rjust(15),"TXID".ljust(15),"Timestamp".ljust(20))
        print("-"*(70+4))
        while lastPosition:
            lastPosition.transaction.print()
            lastPosition=lastPosition.next