def rod_cutting(arr):
    r = [0] * (len(arr))
    s = [0] * (len(arr))
    r[0] = 0

    for i in range(1,len(arr)):
        q = -10000
        for j in range(0,i+1):              #Tricky i need +1, if no first loop will not be conduct because range (0,0)
            if(q < arr[j] + r[i-j]):
                q = arr[j] + r[i-j]
                s[i] = j
            r[i] = q
    return s

def main():
    seqprice = [0,1,5,8,9,10,17,17,20,24,30]
    print(rod_cutting(seqprice))

if __name__ == "__main__":
    main()