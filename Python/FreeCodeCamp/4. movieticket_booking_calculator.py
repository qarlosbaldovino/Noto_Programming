#Condicionales
age = 21
seat_type = 'Gold'
show_time = 'Evening'
is_member = True
is_weekend = False

#Valores
base_price = 15
discount = 0
extra_charges = 0
service_charges = 0
final_price = (base_price + extra_charges + service_charges) - discount

#SI ES MAYOR
#SI ES A LA TARDENOCHE
#SI ES MIEMBRO


if age >= 18:
    print("Podes comprar entradas")
    if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member): #Si tenes 21 o tenes menos de 21 (Sos miembro o No es TARDE NOCHE)

        #Tipos de asiento
        if seat_type == 'Premium':
            service_charges = 5
        elif seat_type == 'Gold':
            service_charges = 3
        else:
            service_charges = 1
        print(f"Asiento {seat_type}: +{service_charges}") 

        #Es fin de semana o Tarde-Noche
        if is_weekend or show_time == 'Evening':
            extra_charges = 2
            print(f"Es Finde o Tarde-noche: +{extra_charges}") 

    #Descuentos
    if age >= 21 and is_member:
            discount = 3
            print(f"Tenes un descuento: -{discount}")
else:
    print("No podes comprar entradas")

final_price = (base_price + extra_charges + service_charges) - discount
print("Final price:",final_price)