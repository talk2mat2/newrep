import random
#python program to collect  employee details and save to datab container
main_database =[]

def random5(length=5):
    #function to generate 5 random characters for password
    letters ="abcdefghijklmnopqrstuvwxyz1234567890"
    rand5letters =''.join((random.choice(letters) for i in range(length)))
    return rand5letters
    

def UserData():
    data_store=[]
    first_name=input("your_name?: ")
    last_name=input("yourlast name: ")
    email_name=input("your email: ")
    name= first_name+" "+last_name
    password = first_name[0]+first_name[1]+str(random5())+last_name[-2]+last_name[-1]
    print("your random generated password is "+password)
    data_store.append(name)
    data_store.append(email_name)
    validate_user_password = input("do you like the password and whish to use it (y/n)? ")
    if validate_user_password.lower() =="y":
        data_store.append(password)
    else:
        min_length = 7
        password=""
        while len(password) < min_length:
            password = input("choose a password: ")
            if len(password) < min_length:
                print("value should longer than 7 characters !")
        print("password ok !")
        data_store.append(password)
    
        
    
    main_database.append(data_store)
    print("your data has been saved accordingly")
    
UserData() #this function will always store name that to the main database container when called any nuumber of times
UserData() 

print(main_database) # print the content of the main data container
 