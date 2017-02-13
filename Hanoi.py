A = []
B = []
C = []
	
	

a = int(input('Enter amount of blocks:'))
for i in range(a, 0, -1): #initialize Stack
	A.append(i)
ShowHanoi()
(hanoi(a))

def hanoi (a):  #comment one
	NonrecHanoi(a)
	#RecHanoi         

def RecHanoi (num, From=A, To=C, Help=B): #basic rec solution
	if num==1:
		MakeAMove(From, To)
	else:
		RecHanoi(num-1, From, Help, To)
		MakeAMove(From, To)
		RecHanoi(num-1, Help, To, From)

def NonrecHanoi (num):
	stackOfTasks = []
	stackOfTasks.append(task(num, A, C, B))
	while stackOfTasks !=[]:
		x=stackOfTasks.pop()
		if x.num==1:
			MakeAMove(x.From, x.To)
		else:
			stackOfTasks.append(task(x.num-1, x.Help, x.To, x.From))
			stackOfTasks.append(task(1, x.From, x.To, x.Help))
			stackOfTasks.append(task(x.num-1, x.From, x.Help, x.To))

class task:  #tasks to be make in loop 
	def __init__(self, num, From, To, Help):
		self.From=From;
		self.To=To;
		self.Help=Help;
		self.num=num;

def ShowHanoi (): #"graphical" representation
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
	print("")
		
def MakeAMove (From, To):
	To.append(From.pop()) #making an essential move and showing it above
	print ("    " + ("A" if From==A else ("B" if From==B else "C")) + " -> " + ("A" if To==A else ("B" if To==B else "C")) )
	ShowHanoi ()




