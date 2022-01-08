#! /bin/python3 

# with open('test.txt', 'r') as f:

f = open('test.txt', 'r+') #open a file for reading and writing

print(f.name)
print(f.mode)

f.close()




