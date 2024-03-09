print ("|WELCOME TO CALCIIII APP|\n")
print ("|PLEASE CALCULATE ME :)|\n")
no = 1
while(no):
    
    print("1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT\n")
    choice  = int(input("Enter the choise BETWEEN 1 to 5 "))
    if(choice > 5):
        print("Invalid Choice !!!!\n Please come up with valid choice :)")
        print("----------------------------------------------------------------")
        continue
        
    if(choice == 5):
        no = 0
        break
    print("\n\n || Enter the numbers ||")
    op1=int(input())
    op2 = int(input())
  
        
        
    if(choice == 1):
        print(op1+op2)
        print("----------------------------------------------------------------")
    elif (choice == 2):
        print(op1-op2)
        print("----------------------------------------------------------------")
    elif (choice == 3):
        print(op1*op2)
        print("----------------------------------------------------------------")
    elif (choice == 4):
        if(op2 == 0):
            print("---DIVISION ERROR---")
            print("----------------------------------------------------------------")
        else:
            print(op1/op2)
            print("----------------------------------------------------------------")
  
   
        
   