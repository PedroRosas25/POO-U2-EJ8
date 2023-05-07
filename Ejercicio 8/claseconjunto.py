class Conjunto:
     __numeros = []
     def __init__(self):
         self.__numeros = []
     def agregarelemento(self,elemento):
          self.__numeros.append(elemento)
     def __eq__ (self, otro):
          b = True
          if (len(self.__numeros )==(len(otro.__numeros))):
               for elemento in self.__numeros:
                    if elemento not in otro.__numeros:
                         b = False
                         break
               for elemento in otro.__numeros:
                    if elemento not in self.__numeros:
                         b = False
                         break     
               if (b == True):
                    print ("Los conjuntos son iguales ")
               else :
                    print ("Los conjuntos son distintos ")               
          else :
               print ("Los conjuntos son distintos ")     

     def __add__ (self, otro):
          listasumada = []
          for elemento in self.__numeros:
               listasumada.append(elemento)
          for elemento in otro.__numeros:
               if elemento not in self.__numeros:
                    listasumada.append(elemento)
          return listasumada          
     def __sub__ (self, otro):
          listarestada = []
          for elemento in self.__numeros:
               if elemento not in otro.__numeros:
                    listarestada.append(elemento)
          return listarestada        
     def __str__(self):
        s='{'
        i=0
        for elem in self.__numeros:
            s+= str(elem)
            if i==len(self.__numeros)-1:
                s+= '}'
            else:
                s+=', '
            i+=1
        return s