usuario = input("Usuario: ")
capital = int(input("Monto: "))
tiempo = int(input("Tiempo: " ))


def CDT(usuario,capital,tiempo):
    if(tiempo > 2):
        porcentajeInteres = 0.03
        valorInteres = (capital * porcentajeInteres * tiempo)/12
        valorTotal = valorInteres + capital
    
    else:
        porcentajePerder = 0.02
        valorPerder = capital * porcentajePerder
        valorTotal = capital - valorPerder
    
    return (f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valorTotal}')

print(CDT(usuario,capital,tiempo))