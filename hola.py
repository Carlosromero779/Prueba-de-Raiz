def saludar(mensaje):
    print(mensaje)
    
saludar('Hola como te va ricardo')

def suma(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

print(f'El resultado es el siguiente {suma(1,2)}')

def creditos():
    solicitud_credito = True
    if solicitud_credito:
        print('Credito aprobado')
    else:
        print('Credito denegado')
def resta(valor1, valor2):
    resultado = valor1 - valor2
    return resultado

print(f'El resultado es el siguiente {resta(1,2)}')