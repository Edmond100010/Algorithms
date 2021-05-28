import random
testarr = [[0 for i in range (0,2)] for j in range(0,1003000)]
testarr1 = [0 for i in range(0,1003000)]

def testfileLine():
    f= open("TestFileLine.txt","w+")
    x=0
    for i in testarr:
        i[0] = x + 1
        x = x + 1 
        i[1] = pow(x,2)  + 1
        str1 = str(i[0]) + " " + str(i[1]) + "\n"
        f.write(str1)
    f.close()

def testfile():
    f= open("TestFile.txt","w+")
    x=0
    for i in range(0,len(testarr1)):
        x = x  + 1
        testarr1[i] = pow(x,2)  + 1
    random.shuffle(testarr1)
    for i in testarr1:
        str1 = str(i) + "\n"
        f.write(str1)


testfile()
testfileLine()
