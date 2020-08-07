users = ["Ram","Shyam","Shiv","Sundar","Suraj","Sushant","Chikki","Khanak","Sonali","Pallavi"]

print(len(users))


while True:
    print("Hi! My name is chitthi and I am the security system robot.")
    name = input("What is your name?: ").strip().capitalize()   
 
    if name in users:
        print("Hello {}!".format(name))
        
        remove = input("Would you like to be removed from the system (yes/no)?: ").lower() 

        if remove == "yes":
            print(users)
            users.remove(name)
            print(users)
        elif remove == "no":
            print("No problem, You can stay here.")

    else:
        print("I think I have not seen you on the list {}".format(name))
        add = input("Would you like to be added to the system (yes/no)?: ").strip().lower()
        if add == "yes":
            users.append(name)
        elif add == "no":
            print("No worries. You will not be on the list.")
            
        

