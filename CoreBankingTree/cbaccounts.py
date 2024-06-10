from cbtransaction import *

class Account:
    minDeposit=100000
    
    #default pin 123456
    def __init__(self, noac, nama, nik):
        self.noac=noac
        self.nama=nama.upper()
        self.nik=nik
        self.pin="123456"        
        self.balance=0
        self.transaction = LinkedListTransaction()

    #tambahkan pemeriksaan amount > 0
    def deposit(self, cabang, amount):    
        self.balance+=amount
        self.transaction.newTransaction(cabang, "12", amount)
        
    #tambahkan pemeriksaan amount > 0
    #tambahkan pemeriksaan setelah penarikan tidak boleh < dari minDeposit
    def withdraw(self, cabang, amount):
        self.balance-=amount
        self.transaction.newTransaction(cabang, "21", amount)

    def show(self):
        print("\n\n>>RINCIAN ACCOUNT\n\n")
        print("No.AC:", self.noac)
        print("Nama:", self.nama)
        print("NIK:", self.nik)
        print("Amount:", f'{self.balance:,}')

    def print(self):
        print(self.noac.ljust(14), self.nama.ljust(50), self.nik.ljust(16))

class AccountNode:
    def __init__(self, account):
        self.account=account
        self.left = None
        self.right = None

class BinarySearchTreeAccount:
    def __init__(self):
        self.root=None
        self.count=0
        
    #non recursive approach
    def newAccount(self,cabang, nik, nama):
        self.count+=1
        noac=cabang + str(self.count).rjust(4,"0")
        account=Account(noac, nama, nik)
        newNode = AccountNode(account)
        
        if not self.root:
            self.root = newNode
        else:
            lastPosition=self.root
            while lastPosition:
                if account.noac < lastPosition.account.noac:
                    if not lastPosition.left:
                        lastPosition.left = newNode
                        break
                    else:
                        lastPosition = lastPosition.left
                else:
                    if not lastPosition.right:
                        lastPosition.right = newNode
                        break
                    else:
                        lastPosition = lastPosition.right                        
        return account

    #recursive approach
    def findTree(self, start, noac):
        if start:
            start.account.print()
            if noac == start.account.noac:
                return start.account
            elif noac < start.account.noac:
                return self.findTree(start.left, noac)
            else:
                return self.findTree(start.right, noac)
        else:
            return None
            
    def find(self, noac):
        return self.findTree(self.root, noac)        
        
    #recursive approach
    def listTree(self, start):
        if start:            
            if start.left:
                self.listTree(start.left)
                
            start.account.print()    
            
            if start.right:
                self.listTree(start.right)
        
    def list(self):
        lastPosition=self.root
        print("\n\n>>DAFTAR ACCOUNT\n\n")
        print("-"*(80+3))
        print("No.AC".ljust(14),"Nama".ljust(50),"NIK".ljust(16))
        print("-"*(80+3))
        self.listTree(self.root)


#unit test
#12=Sumatera Utara, 71=Kota Medan, 11=Medan Johor, 01=Cabang 01, 01=Tabungan
#cabang="1271110101"
#savingAccount=BinarySearchTreeAccount()
#account1=savingAccount.newAccount(cabang, "1271181906730004", "Hendra Soewarno")
#assert account1.nik=="1271181906730004", "Error NIK 1271181906730004"
#account2=savingAccount.newAccount(cabang, "1271181906730005", "Susan")
#account3=savingAccount.newAccount(cabang, "1271181906730006", "Felicia Fortuna")
#account4=savingAccount.newAccount(cabang, "1271181906730007", "Viona Victoria")
#savingAccount.list()
#myAccount = savingAccount.find(account1.noac)
#myAccount.show()
#myAccount.deposit(cabang, 100000)
#assert myAccount.balance==100000, "Error Deposit, new balance 100000 not match"
#myAccount.show()
#myAccount.deposit(cabang, 100000)
#assert myAccount.balance==100000, "Error Deposit, new balance 200000 not match"
#myAccount.show()
#myAccount.withdraw(cabang, 100000)
#assert myAccount.balance==100000, "Error Deposit, new balance 100000 not match"
#myAccount.show()
#myAccount.transaction.list()