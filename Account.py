class Account:
    __name = ""
    __password = ""
    __money = 0

    def __init__(self, name, password, money):
        self.__name = name
        self.__password = password
        self.__money = money

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getMoney(self):
        return self.__money

    def setMoney(self, money):
        self.__money = money