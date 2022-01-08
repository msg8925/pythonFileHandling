#! /bin/python3 

import hashlib

with open('test.txt', 'r+') as f:
   # f_contents = f.readline()
   # print(f_contents)

    listOfPasswds = f.read().split()
    print(listOfPasswds)

    for pwd in listOfPasswds:
        if(pwd == "people"):
            print("success\n")
        else:
            print("failure\n")

    print("\n")

    print(hash("coconut"))
    print(hash("coconut"))
    print(hash("pizza"))



    
    #for password in f:
        #print(password)
        #f_contents = f.readline()
        #print(f_contents)
        

    #f_contents = f.readlines()
    #print(f_contents)

    #f.seek(0, 2) #seek to end of file

    #f.write("frog\n")

    #f.seek(0, 0) #seek to start of file

    #f_contents = f.readlines()
    #:print(f_contents)

#f = open('test.txt', 'r+') #open a file for reading and writing

#print(f.name)
#print(f.mode)

#f.close()




