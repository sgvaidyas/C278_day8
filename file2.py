fp = open("file","r")
y=1
for x in fp.readlines():
    print(y,x,end="")
    y+=1
fp.close()
