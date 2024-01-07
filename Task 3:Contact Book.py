contact ={}


def display_contact():
    print("name\t\t contact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice=int(input("1.Add new contact \n 2.Search contact \n 3. Display contact \n 4.update contact \n  5.delete contact \n 6.exit\n enter your choice : "))
    if choice ==1:
        name=input("enter contact name:")
        phone=input("enter phone number:")
        email=input("enter email :")
        address=input("enter address :")
        contact[name]=phone
        
    elif choice ==2:
        search_name=  input("enter contact name:")
        if search_name in contact:
            print(search_name," 's contact number is",contact[search_name])
        else:
            print("name is not found in contact list")
    elif choice ==3:
        if not contact:
            print("Empty contact book")    
        else:
            display_contact()      
    elif choice==4:
        update_contact=input("enter a contact to be updated :")  
        if update_contact in contact:  
            phone=input("enter phone number:")
            contact[update_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("name is not found in contact list")
    elif choice==5:
        del_contact=  input("enter a contact to be deleted :")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact y/n?")
            if confirm =='y' or confirm=='Y':
                contact.pop(del_contact)
            display_contact()    
        else:
            print("name is not found in contact list")
    else:
        break        



 
