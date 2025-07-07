                                                    #  ''' create Phone book '''

user = {}
choice = 0
print("Phone Book")
while choice != 5:    
    choice = int(input("Choose :\n1. Add Contact\n2. View Contact\n3. Update Contact\n4. Delete Contact\n5. Exit\n"))
    if choice == 1:
        phone = []
        name = input("Enter the name: ")
        ch = 1
        while ch != 0:
            number = int(input("enter the phone number: "))
            phone.append(number)
            ch = int(input("DO you want to add more contact ? \n1. Add More\n0. No : "))
        email = input("Enter the mail Id : ")
        dict = {"name":name,"phone":phone,"email":email}
        user.update({name:dict})
    elif choice == 2:
        ch = int(input("Choose:\n1. All Contact\n2. Search Name : "))
        if ch == 2:
            name = input("Enter the name: ")
            exist = user.get(name)
            if exist != None:
                name = user[name]["name"]
                phone = user[name]["phone"]
                email = user[name]["email"]
                print(f"Name: {name}\nnumber: {phone}\nEmail: {email}")
            else:
                print("not Exist")
        elif ch == 1:
            for key,value in user.items():
                print(f"name:{key}\nphone:{value["phone"]}\nemail:{value["email"]}")
                print()
        else:
            print("invalid response")
    elif choice == 3:
        name = input("enter the name: ")
        exist = user.get(name)
        if exist != None:
            ch = int(input("choose:\n1. Update Name\n2.Update Phone\n3. Update email: "))
            if ch == 1:
                name1 = input("Enter the name: ")
                user[name]["name"]=name1
                exist_data = user[name]
                user.update({name1:exist_data})
                rm_user = user.pop(name)
                print("name updated")
            elif ch == 2:
                h = 1
                user[name]["phone"].clear() 
                while h:
                    number = int(input("Enter the number: "))
                    user[name]["phone"].append(number) 
                    h = int(input("add another number ?\n1. Yes\n0. No : "))
                print("phone updated")
            elif ch == 3:
                email = input("Enter the new mail ID : ")
                user[name]["email"]=email
                print("mail id updated")
            else:
                print("invalid")
        else:
            print("not Exist")
    elif choice == 4:
        name = input("Enter the name: ")
        x = user.get(name)
        if x != None:
            res = user.pop(name)
            print(f"{name} removed")   # if print res out = {'name': 'manu', 'phone': [5849562545], 'email': 'sdfs@fge'} removed
        else:
            print("not exist")
    elif choice == 5:
        print("Exiting ...")
    else:
        print("Invalid Input")
    