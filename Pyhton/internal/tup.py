n1=input("Enter the string")
n2=input("ENter the string")
while True:
    print ("1 -- > join ")
    print ("2 -- > to upper ")
    print ("3 -- > lower ")
    print ("4 -- > len ")
    print ("5 -- > rev ")
    print ("6 -- > substr ")
    print ("7 -- > Converting to upper case and storing to other file ")
  
    choice = int(input("Enter your Choice "))
    if choice == 1:
        print (n1+n2)
        
    elif choice == 2:
       
        print (n1.upper())
    elif choice == 4: