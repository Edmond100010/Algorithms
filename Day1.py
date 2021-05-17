def insertion(arr): #best case:O(n) worst:O(n^2) average:O(n^2)
    print("Insertion sort:") 
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j=j-1
    return arr

def selection(arr):
    print("Selection sort:")
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def wildguess(arr):
    print("Wild-Guess sort:")
    guess = True
    for i in range(len(arr)):
        if(guess == False):
            break
        for j in range(i + 1, len(arr)):
            if (arr[i]>arr[j]):
                print("Guess is Wrong")
                guess = False
            elif ( guess == False):
                insertion(arr)
                return arr
    if(guess == True):
        print("Guess is True")
        return arr

def mergesort(arr):     #Amazing Algorithm
    if len(arr) < 2:
        return arr
    merge = []
    mid = int(len(arr)/2)
    L = arr[:mid]
    R = arr[mid:]
    #print("BL:", L)
    #print("BR:", R)
    L = mergesort(L)
    R = mergesort(R)                                          
    #print("AL:", L)
    #print("AR:", R)
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merge.append(L[i])
            i += 1
        else:
            merge.append(R[j])
            j += 1
    while i < len(L): 
        merge.append(L[i]) 
        i += 1
    while j < len(R): 
        merge.append(R[j]) 
        j += 1
    #print(merge)
    return merge




def main():
    seqnum = [4,8,2,7,5,6,9,3,1,-30,1.5]
    seqnumguess = [1,2,3,4,5,6,7,8,9]
    print(mergesort(seqnum));

if __name__ == "__main__":
    main()