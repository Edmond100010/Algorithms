class Hash():
    def __init__(self,m):
        self.i = 0
        self.m = m
        self.hash = [[None for i in range (0,3)]for j in range(0,m)]
        self.overflowbucket = [[None for i in range (0,4)]for j in range(0,10030)]
    

    def insertoverflowbucket(self,a,z,c):
        position = 0
        pointer = 0
        duplicate = False
        self.hash[a][2] = True
        for x in range(0,self.i+1):
            if(self.overflowbucket[x][0] == a):
                position = x
                duplicate = True
            elif(self.overflowbucket[x][0] == None):
                self.overflowbucket[x][0] = a
                self.overflowbucket[x][1] = z
                self.overflowbucket[x][2] = c
                pointer = x
        if(duplicate == True):
            self.overflowbucket[position][3] =  pointer
        self.i = self.i + 1

    def insert(self,x,c):
        a = x % self.m
        if( self.hash[a][0] == None):
            self.hash[a][0] = x
            self.hash[a][1] = c
        else:
            self.insertoverflowbucket(a,x,c)

    def search(self,x):
        a = x % self.m
        if(self.hash[a][0]==x):
            return self.hash[a][1]
        else:
            return(self.overflowbucket[self.recursivesearch(a,x,0)][2])
                    
    def recursivesearch(self,a,x,p):
        if( self.overflowbucket[p][0] == a and self.overflowbucket[p][1] == x):
            return p
        elif(self.overflowbucket[p][0] == a):
            return (self.recursivesearch(a,x,self.overflowbucket[p][3]))
        else:
            return (self.recursivesearch(a,x,p+1))

    
    def delete(self,x):
        a = x % self.m
        if(self.hash[a][0] == x and self.hash[a][2] == True):
            for i in range(0,len(self.overflowbucket)):
                if(self.overflowbucket[i][0] == a):
                    if(self.overflowbucket[i][3] == None):
                        self.hash[a] = self.overflowbucket[i][1],self.overflowbucket[i][2],None
                    else:
                        self.hash[a] = self.overflowbucket[i][1],self.overflowbucket[i][2],True
                    for z in range (i,len(self.overflowbucket)):
                        if(self.overflowbucket[z] == [None,None,None,None]):
                            break
                        elif( z + 2> len(self.overflowbucket)):
                            self.overflowbucket[z] = [None,None,None,None]
                        else:
                            self.overflowbucket[z] = self.overflowbucket[z+1]  
                    break
        elif(self.hash[a][0]==x and self.hash[a][2] == None):
            self.hash[a] = [None,None,None]
        else:
            i = self.recursivesearch(a,x,0)
            for z in range (i,len(self.overflowbucket)):
                if(self.overflowbucket[z] == [None,None,None,None]):
                    break
                elif( z + 2> len(self.overflowbucket)):
                    self.overflowbucket[z] = [None,None,None,None]
                else:
                    self.overflowbucket[z] = self.overflowbucket[z+1]    


    def printhashtable(self):
        print(self.hash)
        print(self.overflowbucket)
    

