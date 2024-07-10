

###   creat file for read and write
file1=open('datafile.txt','w+')

###   for write on file
# for i in range(15):
#     file1.write(str(i)+'\n')
#     #file1.write('\n')
b=30

a=['dfjskdf\n',str(b)+'\n','383883','dkfekje']
file1.writelines(a)
file1.flush()
file1.close()
### for read file


# print(type(a))
# print(a[0])

#lst=file1.readlines()
#print(lst)
