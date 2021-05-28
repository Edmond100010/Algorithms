def max(arr):
    if(len(arr)<2):
            return arr
    mid = len(arr)/2
    max_l  = max(arr[:mid])
    max_r  = max(arr[mid:])
    if max_l > max_r:
        return max_l
    else: 
        return max_r

def min(arr):
    if(len(arr)<2):
        return arr
    mid = len(arr)/2
    min_l  = min(arr[:mid])
    min_r  = min(arr[mid:])
    if min_l < min_r:
        return min_l
    else: 
        return min_r

def countingsort(arr):                                  #amazing
    b =  [0] * len(arr)
    maximum = int(max(arr)[0]) + 1
    minimum = int(min(arr)[0])
    c1 = [0 for i in range(minimum,maximum)]
    for i in range(0,len(arr)):
        c1[arr[i] - minimum] = c1[arr[i]- minimum] +1
    for i in range(1,len(c1)):
        c1[i] = c1[i] + c1[i-1]
    for j in range((len(arr))-1,-1,-1):                 #new
        b[c1[arr[j] - minimum]-1] = arr[j]
        c1[arr[j]- minimum] = c1[arr[j]- minimum] - 1
    return b

def main():
    seqnum = [4,8,2,7,5,6,9,3,1,-30,1,100]
    seqnumguess = [1,2,3,4,5,6,7,8,9,10,1.5]

    print(countingsort(seqnum))

    

if __name__ == "__main__":
    main()