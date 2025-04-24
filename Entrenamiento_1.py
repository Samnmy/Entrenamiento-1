def Cond(t_d, m_p, m_e):    #Primero se define una funcion para que cuando el usuario ingrese un valor no valido le vuelva a pedir el valor
    while True:         
        try:
            valor = t_d(input(m_p))
            return valor
        except ValueError:
            print(m_e)
        except TypeError:
            print(m_e)
NP=input("Ingresa el nombre del producto: ")    #Se le pide al usuario que ingrese 
PU=Cond(float,"Ingresa el precio unitaro del producto: ","Error ingrese un precio valido.")   #Se le pide al usuario que ingrese el valor del producto
while PU <= 0:  #En caso de que el producto sea menor a cero se le solicita que vuelva a ingresar el valor hasta que sea correcto
    PU=Cond(float,"Error. Ingresa el precio unitaro del producto: ","Error ingrese un precio valido.")
C=Cond(float,"Ingresa la cantidad de productos: ","Error ingrese una cantidad valida.")     #Se le pide al usuario que ingrese la cantidad de productos
while C <= 0:   #En caso de que la cantidad de productos sea menor a cero se le solicita que vuelva a ingresar el valor hasta que sea correcto
    C=Cond(float,"El valor de la cantidad de productos es incorrecto porfavor ingrese la cantidad correcta: ","Error ingrese una cantidad valida.")
D=Cond(float,"Ingresa el descuento del producto: ","Error ingrese un descuento valido.")    #Se le solicita al usuario que ingrese el descuento
if D < 0 or D > 100:    #En caso de que el descuento sea erroneo hacer:
    while D <= 0 or D > 100:    #Solicita el valor hasta que sea entre 0 a 100
        D=Cond(float,"El valor del descuento esta fuera del rango de 0 a 100: ","Error ingrese un descuento valido.") 
PN=PU*C     #Calculo para el valor del producto sin descuento
PN=round(PN, 2) #Lo formateamos para que solo sea de dos cifras despues del decimal
PD=PN-(PN*(D/100))  #Calculo para el valor del producto con descuento
PD=round(PD, 2) #Lo formateamos para que solo sea de dos cifras despues del decimal
print("El nombre del producto es: "+ NP)    #Muestra el valor del producto
if D == 0.0:    #Condiciona para mostrar algo distinto si tiene o no descuento
    print("El producto no tiene descuento por lo tanto el valor final es de: " + str(PN))   #Muestra el valor total 
else:     #Si no tiene descuento hace:
    print("El precio neto del producto es de: " + str(PN)) #Muestra el valor sin descuento
    print("El precio con descuento es de: " + str(PD))  #Muestra el valor con descuento