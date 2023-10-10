from src import server
from src import conn
from src import banner


banner.banner_print()

while True : 
    try : 
        print("[1. Host a party ] \n [2.Join A Party] \n")
        ch = int(input("Enter The Choice !! :"))
        if ch == 1 : 
            server.start_party()
        elif ch == 2 : 
            conn.join_party()
        else :
            print("Enter The Correct Choice !!!")
    except ValueError:
        print("Value Error!! ... ")
    except TypeError:
        print("Type Error !! ...")
    except KeyboardInterrupt : 
        print("Exiting .....!")
        exit()
