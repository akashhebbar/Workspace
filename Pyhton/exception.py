while True:
   print ("1 Enter The File Name of Source and Destination File ")
   print ("2 Opening a file in Read and Write Mode")
   print ("3 Writing to a File ")
   print ("4 Reading the content in the File ")
   print ("5 Copying the content to a new file ")
   print ("6 Closing the File ")
   ch = int(input("Enter the Choice "))
   if ch == 1:
       sname=input("Enter the source file name")
       dname=input("Enter the destinstion ilr nsmr")
       print("two file created")
   elif ch==2:
       try:
           a=open(sname,'r')
           b=open(dname,'w')
           print("*"*80)
           print("open done")
       except FileNotFoundError:
           print("file nior found")
       except NameError:
           print("name error")
   elif ch==3:
       try:
           c="Enter the content"
           smame1=input("Enter the source file name desitnation")
           a=open(sname1,'r')
           
           b=open(dname,'w')
           b.write(c)
           print("*"*80)
           print("copy done")
           
       except NameError:
           print("*"*80)
           print("iOOOOOOOOOOOOOOOOOOOOOOOOOOOOeRRRRRRRRRRRRRRRRRRd")
   elif ch==4:
        try:
           
           sname13=input("Enter the new file name ")
           a=open(sname13,'w')
           a.close()
           a=open(sname13,'r')
           a.write("hello")
           
        except IOError as e:
           print("*"*80)
           print("iOOOOO ",e)
       
   

