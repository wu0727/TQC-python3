f = open("write.txt",'w')
for i in range(5):
    f.write(input()+'\n')
f.close()