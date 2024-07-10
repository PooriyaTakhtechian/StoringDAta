

file1=open('datafile.txt','r+')

#print(file1.read(2))
# print(file1.readline())
# print(file1.readline())
'''
for i in range(10):
    a=file1.readline()
    print(a)
'''
b=[]
print(type(b))
a=file1.read()
a=list(a)

for i in range(len(a)):
    if(a[i]!='\n'):
        b.append(int(a[i]))
        
print(b)