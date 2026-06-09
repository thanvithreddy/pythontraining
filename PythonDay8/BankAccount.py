class BankAccount:
    def __inti__(self, name,acc_no,pin):
        self.__name=name
        self.__acc_no=acc_no
        self.__pin=pin
        print("Bank Account created successfully")

    def get_name(self):
        print(self.__name)
    def get_acc_no(self):
        print(self.__acc_no)
    def get_pin(self):
        print(self.__pin)
    def set_name(self,name):
        self.__name=name   
    def set_acc_no(self,acc_no):
        self.__acc_no=acc_no    
    def set_pin(self,pin):
        self.__pin=pin  
b1=BankAccount("Scott",123456,7890)
b1.get_name()