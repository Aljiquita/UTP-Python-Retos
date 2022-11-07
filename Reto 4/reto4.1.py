# el presente ejercicio es el desarrollo del retor 4 con map() list() y reduce() pero sin generar la respuesta requerida por el bot
 
from functools import reduce


def ordenes(rutinaContable):
    orden_minimo = 600000
    
    # 1.1- OJO el for() lo cámbianos por un .map()  General una lista con los datos de cada el N° orden y los valores de compra
    total = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:]))  ,rutinaContable))
    print (total)
    
    # 1.2- General una lista con los datos de cada el N° orden y los valores de compra
    Total_Ordenes = []
    for i in range(len(rutinaContable)):
        x= len(rutinaContable[i])
        orden = []    
        orden.append(rutinaContable[i][0])
        for j in range(1, x):
            orden.append(rutinaContable[i][j][1] * rutinaContable[i][j][2])
        Total_Ordenes.append(orden)
    print(Total_Ordenes)
    
    
    # 2.1- OJO el for() lo cambiamos por un  .map() uno dentro de otro  Generar una lista con el N° orden y la suma de los valores de los artículos
    orden1 = list(map(lambda x: [x[0]] + [reduce(lambda a,b: round(a+b, 2), x[1:])], total))
    print(orden1)
    
    
    # 2.2- Generar una lista con el N° orden y la suma de los valores de los artículos
    orden = []
    for i in range(len(Total_Ordenes)):
        total = []
        total.append(Total_Ordenes[i][0])
        y = len(Total_Ordenes[i])
        total2 = 0
        for j in range(1, y):
            total2 += Total_Ordenes[i][j]
        total.append(total2) 
        orden.append(total) 
    print(orden)
    
    # 3.1 OJO el for() lo cambiamos por un .map() e integramos el if dentro del .map() Generar un incremento de 25.000 si el valor [1] de cada tupla es menor de 600.000
    orden_final = list(map(lambda x: [x[0] , x[1] + 25000] if x[1] < orden_minimo  else x,  orden1))
    print(orden_final)
    
    # 3.2 OJO el for() lo cambiamos por un .map() e integramos el if dentro del .map() Generar un incremento de 25.000 si el valor [1] de cada tupla es menor de 600.000
    orden_final = list(map(lambda x: x if x[1] >= orden_minimo  else [x[0], x[1] + 25000],  orden1))
    print(orden_final)

    # 3.3 Generar un incremento de 25.000 si el valor [1] de cada tupla es menor de 600.000
    orden_final = []
    for k in range(0,len(orden)):
        total = []
        total.append(orden[k][0])
        if orden[k][1] < orden_minimo:
            total.append(round((orden[k][1] + 25000), 2) )
        else:
            total.append(round((orden[k][1]), 2))
        orden_final.append(total)
    print(orden_final)
    
    
    

    
    
    
    
    
    
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
