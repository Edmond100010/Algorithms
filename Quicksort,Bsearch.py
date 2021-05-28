'''
Date:05-19-2021
Bsearch Version1 (error):
def bsearch(arr,p,r,x):
    if p == r:
        if arr[p] == x:
            return p
        else:
            return None
    else:
        q = (p + r ) /2
        if x <= arr[q]:
            bsearch(arr,p,q,x)
        else:
            bsearch(arr,q+1,r,x)
Reason: First return P is correct. However, the second result will be nothing
then the final return always be None.
~Be careful the return about recursion!!

quicksort amazing!

'''



def insertion(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j=j-1
    return arr

def startbsearch(arr,x):
    arr = insertion(arr)
    result = bsearch(arr,0,len(arr)-1,x)
    if result != None:
        return result + 1
    else:
        return None


def bsearch(arr,p,r,x):
    if p == r:
        if arr[p] == x:
            return p
        else:
            return None
    else:
        q = (p + r ) /2
        if x <= arr[q]:
            p = bsearch(arr,p,q,x)
            return p
        else:
            p = bsearch(arr,q+1,r,x)
            return p 

def partition(A,p,r):
    i = p - 1
    x = A[r]
    for j in range (p, r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]                 #New knowledge
    
    temp = A[i + 1]                               #Before
    A[i + 1] = A[r]
    A[r] = temp
    
    return i + 1

def quicksort(a,p,r):
    if p >=r:
        return a
    else:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q +1,r)


def start_quicksort(a):
    quicksort(a,0,len(a)-1)



def main():
    seqnum = [4,8,2,7,5,6,9,3,1,-30,1.5,100]
    seqnumguess = [1,2,3,4,5,6,7,8,9,10,1.5]
    #print(startbsearch(seqnum,101))
    hsi = [line.strip() for line in open("HSI.txt", 'r')]
    print(len(hsi))
    

if __name__ == "__main__":
    main()



