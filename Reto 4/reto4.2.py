# la mision de este codigo era aplica las funciones map() reduce() lambda
# deje el codigo hasta el punto de generar un listado de facturas totales 
# falta el incremento del 25.000 apra las factura menores de 600000
# y falto tambien los resultado por factura con su texto en pantalla
def ordenes(rutinaContable):
    from functools import reduce
    Numero_Facturas = len(rutinaContable)
    y = lambda x , y: x * y
    Facturas = []
    for i in range(0, Numero_Facturas ):
        Numero_Compras_Fac = len(rutinaContable[i])-1
        cantidad = []
        valor = []
        for j in range(0, Numero_Compras_Fac):
            cantidad.append(rutinaContable[i][j+1][1])
            valor.append(rutinaContable[i][j+1][2])
        Valor_producto = list(map(y, cantidad, valor))
        valor_factores = reduce(lambda x, y: x + y, Valor_producto)
        Facturas.append(valor_factores)

    
    print(Facturas)
    respuesta = 0
    print(respuesta)

'''
    respuesta += ('------------------------ Inicio Registro diario ---------------------------------\n')        
    respuesta += ('-------------------------- Fin Registro diario ----------------------------------')
    '''

rutinaContable = [ [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
                   [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
                   [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
                   [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]
ordenes(rutinaContable)
