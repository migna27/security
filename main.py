from entities.user import User
from getpass import getpass

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
        option= int(input())
        if option ==1:
            registrar_user()
        elif option==2:
            view_users()
    else:
        print("Usuario inválido")
   
        