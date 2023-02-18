import  random
class F:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def __metod(self):
        c = random.randint(1,2)
        if c == 1:
            return self.__a * self.__b
        elif c == 2:
            return  self.__b + self.__a
    def printer(self):
        print(self.__metod())


gg = F(100, 300)
gg.printer()
