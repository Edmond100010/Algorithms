'''
Date: (22-23)-05-2021
.=1
-=111
space between . and - = 0
space between letter  = 000
space between word = 0000000
'''

morsecodebinarylist = [None] *63

def startmorsecodelist():
    x = open("morsecode.txt","r")
    for i in x:
        str1 = i.rstrip()
        str2 = ''
        for y in range (2,len(str1)):
            if(i[y]=='.'):
                str2 = str2 + '0'
            else:
                str2 = str2 + '1'
        position = pow(2,len(str2)) + binary(str2) -1
        morsecodebinarylist[position] = i[0]+" " + str2

def length(str):
    return len(str)

def binary(str):
    x = 0
    for i in range(0,len(str)):
        x = x + int(str[i])*pow(2,len(str)-1 - i)
    return x


def decode(str):
    count = 0
    countspace = 0
    str1 = ''
    answer = ''
    for i in range(0,len(str)):
        if( str[i] == '1'):
            count = count + 1
        if( str[i] == '0'):
            if(count==1):
                str1 = str1 + '0'
                count = 0
                countspace=0
            elif(count==3):
                str1 = str1 + '1'
                count = 0
                countspace=0
            else:
                countspace = countspace + 1
        if(i == len(str)-1):
            str1 = str1 + str[i]
            position = pow(2,len(str1)) + binary(str1) -1
            answer = answer + morsecodebinarylist[position][0]
            str1 = ''
            countspace = 0
        if(countspace==6):
            position = pow(2,len(str1)) + binary(str1) -1
            if(position==0):
                answer = answer + ' '
            else:
                answer = answer + morsecodebinarylist[position][0] + ' '
            str1 = ''
            countspace = 0
        if(countspace==2 and str[i+1] != '0'):
            position = pow(2,len(str1)) + binary(str1) -1
            answer = answer + morsecodebinarylist[position][0]
            str1 = ''
            countspace = 0
    return answer

def searchmorsecode(x):
    if(x == ' '):
        return 
    else:
        x = x.upper()
    for i in morsecodebinarylist:
        if(i!=None):
            if(i[0] == x):
                return(i[2:len(i)])


def encoder(str):
    str1 = str.upper().rstrip()
    str2 = ''
    for i in range(0,len(str1)):
        if(str1[i] ==' '):
            str2 = str2 + "0000000"
        else:
            str3 = searchmorsecode(str1[i])
            if(searchmorsecode(str1[i])==None):
                return None
            elif(str3 ==' '):
                str2 = str2 + "0000000"
            else:
                for y in range(0,len(str3)):
                    if(str3[y] == '0'):
                        str2 = str2 + '10'
                    if(str3[y] == '1'):
                        str2 = str2 + '1110'
                    if(y==len(str3)-1):
                        str2 = str2 + '00'
                    if(i == len(str1)-1 and y == len(str3) -1):   
                        str2 = str2[0:len(str2) -4]
    return str2



def switch():
    x = input('1:Encoder\n2:Decoder\n3:End\nYour Choice:')
    if(x == '1'):
        a = input('Encoder(String):')
        print(encoder(a))
        switch()
    elif(x == '2'):
        a = input('Decoder(String):')
        print(decode(a))
        switch()
    elif(x == '3'):
        return 0
    else:
        switch()

def main():
    startmorsecodelist()
    switch()

if __name__ == "__main__":
    main()