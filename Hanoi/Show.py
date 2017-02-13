class Show(object):    
    def ShowHanoi (self, A, B, C): #"graphical" representation
        print("A: ", end='')
        for i in range(0,len(A)):
            print (repr(A[i]).rjust(3), end='')
        print("")
        print("B: ", end='')
        for i in range(0,len(B)):
            print (repr(B[i]).rjust(3), end='')
        print("")
        print("C: ", end='')
        for i in range(0,len(C)):
            print (repr(C[i]).rjust(3), end='')
        print("")
        print

    def MakeAMove (self, From, To, A, B, C):
        To.append(From.pop()) #making an essential move and showing it above
        print ("    " + ("A" if From==A else ("B" if From==B else "C")) + " -> " + ("A" if To==A else ("B" if To==B else "C")) )
        self.ShowHanoi (A, B, C)



