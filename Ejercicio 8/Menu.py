from claseconjunto import Conjunto
from controlador import Controlador
class Menuclass:
    __opcion=0
    def __init__(self):
        self.__opcion=0
    def opciones(self, c):
        while self.__opcion != 6:
            print ('\nOpcion 1: Crear un conjunto ')
            print ("Opcion 2: Union de dos conjuntos ")
            print ("Opcion 3: Diferencia de conjuntos ")
            print ("Opcion 4: Igualar conjuntos ")
            print ("Opcion 5: Mostrar conjuntos ")
            print ("Opcion 6: SALIR \n")
            self.__opcion=int(input("Seleccione una opcion "))
            if self.__opcion == 1:
                c.cargar()
            elif self.__opcion==2:
                c.unir()
            elif self.__opcion==3:
                c.diferencia()
            elif self.__opcion==4:
                c.igualar()
            elif self.__opcion == 5:
                c.mostrar()
        else: print ("SALIENDO DEL SISTEMA")        
                


                   
                   