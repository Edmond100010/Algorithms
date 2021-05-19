'''
Date:05-19-2021
Random

'''

import random

def randompermute(a):
    n = len(a)
    for i in range(0,n):
        x = a[random.randint(0,i)]
        temp = a[i]
        a[i] = a[x]
        a[x] = temp
    return a


def factorial(k):
    if(k == 1):
        return k
    else:
        return k*factorial(k-1)







def main():
    seqnum = [4,8,2,7,5,6,9,3,1,-30,1.5,100]
    seqnumguess = [1,2,3,4,5,6,7,8,9,10]
    randompermute(seqnum)
    print(seqnum)
if __name__ == "__main__":
    main()