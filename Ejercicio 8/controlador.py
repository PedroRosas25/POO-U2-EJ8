from claseconjunto import Conjunto
class Controlador:
    __listadeconjuntos = []
    def __init__(self):
        __listadeconjuntos = []

    def cargar (self):
        lista = Conjunto()
        i = 0
        tamanio = int(input ('Ingrese tamano del conjunto '))
        for i in range(tamanio) :
            elemento = int(input ('Ingrese el elemento numero {} del conjunto '.format(i+1)))
            lista.agregarelemento(elemento)        
        self.__listadeconjuntos.append(lista) 
        print ('Conjunto Creado ')    

    def mostrar (self):
        for i in range (len(self.__listadeconjuntos)):
            print ('Conjunto numero {}: {} '.format(i+1, self.__listadeconjuntos[i]))     
    
    def unir (self): 
        resultado = self.__listadeconjuntos[0] + self.__listadeconjuntos[1]
        print ("Suma de los dos conjuntos ")
        print (": {}".format(resultado))

    def diferencia (self):
        resultado = self.__listadeconjuntos[0] - self.__listadeconjuntos[1]
        print ('Resta del primer conjunto menos el segundo')
        print (': {}'.format(resultado))

    def igualar (self):
        self.__listadeconjuntos[0] == self.__listadeconjuntos[1]