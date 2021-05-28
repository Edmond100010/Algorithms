from Day3_Tree import Tree
def length(str):
    return len(str)




def main():
    test = (1111000100010110001011000000)
    morsecodetxt = open("morsecode.txt","r")


    morsecodetxtlist = []
    morsecodeLlist = []
    morsecodeRlist = []
    for i in morsecodetxt:
        morsecodetxtlist.append(i.rstrip())

    morsecodetxtlist.sort(key = length )

    morsecodetree = Tree(" ")
    morsecodetree.insertR(1)
    morsecodetree.insertR(2)
    '''
    for i in morsecodetxtlist:
        if(i[2]=='.'):
            morsecodeLlist.append(i)
        else:
            morsecodeRlist.append(i)

    for i in morsecodeLlist:
        level = len(i) - 1
        if(i[level]=='.'):
            morsecodetree.insertL(i)
        else:

            morsecodetree.insertR(i)
    



    L = morsecodetree.getLChild()
    R = morsecodetree.getRChild()
    morsecodetree.printTree(L)
    print(morsecodetree.search(morsecodetree,"...."))
    #morsecodetree.search(L)
    #morsecodetree.search(morsecodetree,"...."
'''




    

if __name__ == "__main__":
    main()