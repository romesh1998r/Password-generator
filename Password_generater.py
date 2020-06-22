import random


Characters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890|\!"£$%&/()=?^[]{}@#,._+*-/'


#how many passwords user want
xy=int(input("Enter the number of passwords:"))
#length of password
fg=int(input("Enter the length of passwords:"))

yu=print("Password :")


for i in range(xy):

    Password=''

    for c in range(fg):

        Password=Password+random.choice(Characters)

    print(Password)
        
    

    
