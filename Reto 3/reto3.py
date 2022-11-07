def AutoPartes(ventas: list):

    cantVent = len(ventas)
    
    IdProducto = list()
    dProducto = list()
    pnProducto = list()
    cvProducto = list()
    sProducto = list()
    nComprador = list()
    cComprador = list()
    fVenta = list()
    
    for i in range(0, cantVent):
        IdProducto.append(ventas[i][0])
        dProducto.append(ventas[i][1])
        pnProducto.append(ventas[i][2])
        cvProducto.append(ventas[i][3])
        sProducto.append(ventas[i][4])
        nComprador.append(ventas[i][5])
        cComprador.append(ventas[i][6])
        fVenta.append(ventas[i][7])
    
    ventas = {'IdProducto': IdProducto,
              'dProducto': dProducto,
              'pnProducto': pnProducto,
              'cvProducto': cvProducto,
              'sProducto': sProducto,
              'nComprador': nComprador,
              'cComprador': cComprador,
              'fVenta': fVenta}    

    return ventas




def consultaRegistro(ventas, idProducto):
    idProExiste = 0
    j = len(ventas['IdProducto'])
    existe = idProducto  in ventas['IdProducto']
    if existe == False:
        respuesta = 'No hay registro de venta de ese producto'
    else:
        respuesta= str()
        for i in range(0, j):            #print(idProducto)
            if idProducto == ventas['IdProducto'][i]:
                idproducto = ventas['IdProducto'][i]
                dproducto = ventas['dProducto'][i]
                pnproducto = ventas['pnProducto'][i]
                cvproducto = ventas['cvProducto'][i]
                sproducto = ventas['sProducto'][i]
                ncomprador = ventas['nComprador'][i]
                ccomprador = ventas['cComprador'][i]
                fventa = ventas['fVenta'][i]
                
                respuesta += f'Producto consultado : {idproducto}  Descripción  {dproducto}  #Parte  {pnproducto}  Cantidad vendida  {cvproducto}  Stock  {sproducto}  Comprador {ncomprador}  Documento  {ccomprador}  Fecha Venta  {fventa}\n' 
    print(respuesta)
    
    
    
consultaRegistro(AutoPartes([
    (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (2001,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)
print()