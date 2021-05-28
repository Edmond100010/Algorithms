x = "DEADBEEF"
y = "EABEEF"


def lcs(str1,str2):
    str1 = "0" + str1
    str2 = "0" + str2
    c = [[0 for i in range (0,len(str2))]for j in range(0,len(str1))] #i = str1,j = str2
    b = [[0 for i in range (0,len(str2))]for j in range(0,len(str1))]
    for i in range(1,len(str1)):
        for j in range(1,len(str2)):
            if(str1[i] == str2[j]):
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = "m"
            elif(c[i-1][j]>=c[i][j-1]):
                c[i][j] = c[i-1][j]
                b[i][j] = "xnm"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "ynm"
    print("CS:")
    printlcs(b,len(str1)-1,len(str2)-1)
    print("LCS:", maxlcs(str1,str2))

    
def printlcs(b,i,j):
    if(i == 0  or j == 0):
        return b
    if(b[i][j]) == "m":
        printlcs(b,i-1,j-1)
        print(x[i-1])
    elif(b[i][j] == "xnm"):
        printlcs(b,i-1,j)
    else:
        printlcs(b,i,j-1)

def maxlcs(str1,str2):
    str3 = ""
    d = [[0 for i in range (0,len(str2))]for j in range(0,len(str1))]
    l = 0
    p = 0
    for i in range (1,len(str1)):
        for j in range(1,len(str2)):
            if (str1[i]==str2[j]):
                d[i][j] = d[i-1][j-1] +1
                if d[i][j] > l:
                    l = d[i][j]
                    p = i
    for i in range(p-l,p):
        str3 = str3 + x[i]
    return str3




def main():
    lcs(x,y)



if __name__ == "__main__":
    main()