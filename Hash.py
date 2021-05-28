from Hash_Class import Hash

def main():
    x = 0
    test = {'1':"SID:1 Name: Chan man",'23':"SID:23 Name: Chan man",'11':"SID:11 Name: Chan man",'132':"SID:132 Name: Chan man",'14':"SID:14 Name: Chan man"}
    testarr = [[0 for i in range (0,2)] for j in range(0,10030)]
    for i in testarr:
        i[0] = x + 1
        i[1] = pow(x,2) + 1
        x = x + 1 
    b = Hash(200)
    for i in testarr:
        b.insert(i[0],i[1])
    print(b.search(2934))

    '''
        a = Hash(2)
    for i in test:
        a.insert(int(i),test[i])
    '''

if __name__ == "__main__":
    main()