
def ordenes(rutinaContable):
    from functools import reduce
    sumaPorPedido = 0
    cantidadFacturas = len(rutinaContable)
    tamañoLista = 0
    contador1 = 0
    respuesta= str()
    x = lambda x , y: x + y
    y = lambda x , y: x * y
    respuesta += ('------------------------ Inicio Registro diario ---------------------------------\n')
    for i in range(0, cantidadFacturas):
        LisFac = list()
        for j in range(1, len(rutinaContable[i])):
            limite = 0
            if i == i:
                factura = rutinaContable[i][0]
                z = y(rutinaContable[i][j][2], rutinaContable[i][j][1])
                LisFac.append(z)
                limite += limite
        totalFac = reduce(lambda x, y: x + y, LisFac)
        
        if totalFac < 600000:
            t= x(totalFac, 25000)
            respuesta += (f'La factura {factura} tiene un total en pesos de {t:,.2f}\n')
        else:
            respuesta += (f'La factura {factura} tiene un total en pesos de {totalFac:,.2f}\n') 
        
    respuesta += ('-------------------------- Fin Registro diario ----------------------------------')
    print(respuesta)


rutinaContable = [ [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
                   [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
                   [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
                   [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]
ordenes(rutinaContable)

