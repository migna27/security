from entities.user import User
from getpass import getpass
from entities.card import Card
def registrar_user():
    name= input("nombre: ")
    curp= input("CURP: ")
    

    while True:
        account= input("Cuenta: ")
        if  User.check_account_exists(account):
            print("La cuenta ya existe. Por favor, elija otro nombre de cuenta.")
        else:
            
            password= getpass("Contraseña: ")
            User.insert(name, account, curp, password)
            print("Usuario registrado exitosamente")
            break
    
def view_users():
    users=User.get_users()
    for user in users:
        print(f"ID: {user.id},NAME: {user.name}, CURP: {user.curp},account: {user.account} ")

def login():
    account= input("Cuenta: ")
    password= getpass("Contraseña: ")
    user=User.get_user_by_account(account)
    if user and user.password == password: #conjunción 
        return True
    else:
        return False
    
    #return user and user.password == password # es lo mismo que lo anterior
    
#Si main es la puerta de entrada 
if __name__=="__main__": 
    print("Inicio de sesión ")
    if login():
        print(" Seleccione una opción del menú")
        print(" 1.-Registrar un usuario")
        print(" 2.-Consultar un usuario")
        print (" 3.-Registrar una tarjeta")
        print(" 4.-Consultar una tarjetas")
        option= int(input())
        if option ==1:
            registrar_user()
        elif option==2:
            view_users()
        elif option==3:
            number= input("Número de la tarjeta: ")
            type= input("Tipo de la tarjeta: 1= débito, 2= crédito: ")
            if type == "1":
                type= "Debit"
            elif type == "2":
                type= "Credit"
            else:
                print("Opción inválida")
        
            view_users()
            id_usuario= input("ID del usuario: ")
            Banco= input("Banco: ")
            Card.card_insert(number, type, id_usuario, Banco)
            print("Tarjeta registrada exitosamente")

        elif option==4:
            user_id= input("ID del usuario: ")
            cards= Card.get_cards_by_user_id(user_id)
            for card in cards:
                print(f"ID: {card.id}, Number: {card.number}, Type: {card.type}, Banco: {card.Banco}")


            
        else:
            print("Opción inválida")

    else:
        print("Usuario inválido")
   
        