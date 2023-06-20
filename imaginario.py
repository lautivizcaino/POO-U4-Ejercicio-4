
class Imaginario:
    __entero:int
    __imaginario:int
    def __init__(self,entero,imaginario) -> None:
        self.__entero=entero
        self.__imaginario=imaginario

    def getEntero(self):
        return self.__entero
    
    def getImaginario(self):
        return self.__imaginario

    def __add__(self,otro):
        a=self.__entero
        b=self.__imaginario
        c=otro.getEntero()
        d=otro.getImaginario()
        parteReal=a+c
        parteImaginaria=b+d
        nuevoImaginario=Imaginario(parteReal,parteImaginaria)
        return nuevoImaginario
    
    def __sub__(self,otro):
        a=self.__entero
        b=self.__imaginario
        c=otro.getEntero()
        d=otro.getImaginario()
        parteReal=a-c
        parteImaginaria=b-d
        nuevoImaginario=Imaginario(parteReal,parteImaginaria)
        return nuevoImaginario
    
    def __mul__(self,otro):
        a=self.__entero
        b=self.__imaginario
        c=otro.getEntero()
        d=otro.getImaginario()
        parteReal=a*c-b*d
        parteImaginaria=a*d+b*c
        nuevoImaginario=Imaginario(parteReal,parteImaginaria)
        return nuevoImaginario
    
    def __truediv__(self,otro):
        a=self.__entero
        b=self.__imaginario
        c=otro.getEntero()
        d=otro.getImaginario()
        parteReal=(a*c+b*d)/(c*c+d*d)
        parteImaginaria=(b*c-a*d)/(c*c+d*d)
        nuevoImaginario=Imaginario(parteReal,parteImaginaria)
        return nuevoImaginario

    def __str__(self) -> str:
        if self.__imaginario>=0:
            expresion='%s+%si'%(self.__entero,self.__imaginario)
        elif self.__imaginario<0:
            expresion='%s%si'%(self.__entero,self.__imaginario)
        return expresion