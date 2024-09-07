class Persona:
    def __init__(self, Prioridad, Nombre):
        self.Prioridad = Prioridad
        self.Nombre = Nombre

class PrioridadFila:
    def __init__(self):
        self.Fila = []

    def __str__(self):
        #Se establece una estructura para mostrar los nombres.
        return ', '.join([i.Nombre for i in self.Fila])
    
    def Insertar(self, Datos):
        self.Fila.append(Datos)
    
    def isEmpty(self):
        return len(self.Fila) == 0
    
    def PopYDelete(self):
        #Este bucle se repite por cada elemento de la lista para ordenarla.
        ValorMaximo = 0

        for i in range(len(self.Fila)):
            if self.Fila[i].Prioridad > self.Fila[ValorMaximo].Prioridad:
                ValorMaximo = i
        item = self.Fila[ValorMaximo]
        del self.Fila[ValorMaximo]
        return item.Nombre
    
def main():
    #El número más alto recibirá mayor prioridad.
    #Esta estructura se puede realizar con listas o con heaps.
    PF = PrioridadFila()
    PF.Insertar(Persona(12, 'Juan'))
    PF.Insertar(Persona(1, 'Domingo'))
    PF.Insertar(Persona(14, 'José'))
    PF.Insertar(Persona(2, 'Nadia'))
    PF.Insertar(Persona(10, 'Penny'))
    PF.Insertar(Persona(3, 'Luke'))
    PF.Insertar(Persona(25, 'John'))
    PF.Insertar(Persona(100, 'Abi'))
    PF.Insertar(Persona(1, 'Marta'))
    PF.Insertar(Persona(30, 'Ruth'))

    print (PF)

    while not PF.isEmpty():
        print(PF.PopYDelete())

if __name__ == '__main__':
    main()