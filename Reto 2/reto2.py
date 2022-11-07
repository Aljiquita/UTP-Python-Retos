
def cliente(informacion):
    if(informacion['edad'] > 18):
        atraccion = 'X-Treme'
        if(informacion.setdefault('primer_ingreso') == True):
            apto = bool(informacion['edad'] > 18 and informacion['primer_ingreso'] == 1)
            total_boleta = 20000 * .95
            
        else:
            apto = bool(informacion['edad'] > 18 and informacion['primer_ingreso'] == 0)
            total_boleta = 20000
            
    elif(informacion['edad'] >= 15 and informacion['edad'] <= 18):
        atraccion = 'Carros chocones'
        if(informacion.setdefault('primer_ingreso') == 1):
            apto = bool((informacion['edad'] >= 15 and informacion['edad'] <= 18) and informacion['primer_ingreso'] == 1)
            total_boleta = 5000 * .93
            
        else:
            apto = bool((informacion['edad'] >= 15 and informacion['edad'] <= 18) and informacion['primer_ingreso'] == 0)
            total_boleta = 5000
            
    elif(informacion['edad'] >= 7 and informacion['edad'] < 15):
        atraccion = 'Sillas voladoras'
        if(informacion.setdefault('primer_ingreso') == 1):
            apto = bool((informacion['edad'] >= 7 and informacion['edad'] < 15) and informacion['primer_ingreso'] == 1)
            total_boleta = 10000 * .95
            
        else:
            apto = bool((informacion['edad'] >= 7 and informacion['edad'] < 15) and informacion['primer_ingreso'] == 0)
            total_boleta = 10000
            
    else:
        atraccion = 'N/A'
        apto = bool(0)
        total_boleta = 'N/A'
        
    informacion = {'nombre': informacion['nombre'],
                    'edad': informacion['edad'],
                    'atraccion': atraccion,
                    'apto': apto,
                    'primer_ingreso': informacion['primer_ingreso'],
                    'total_boleta': total_boleta}
    return (informacion)

            

informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
}
print(cliente(informacion))