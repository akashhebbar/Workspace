dict1={'name':'arun','age':20}
choice = int(input("Enter your Choice "))
if choice == 1:
    dict1['name']='hello'
    print(dict1)
elif choice==2:
    dict2=dict1.copy()
    print(dict2)
elif choice==3:
    print(dict1.items())
elif choice==4:
    dict1.pop('name')
    print(dict1)
elif choice==5:
    dict1.clear()
    print(dict1)
elif choice==6:
    del dict1
   