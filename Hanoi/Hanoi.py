import Show
show=Show.Show()

A = []
B = []
C = []




def RecHanoi (num, From=A, To=C, Help=B): #basic rec solution
	if num==1:
		show.MakeAMove(From, To, A, B, C)
	else:
		RecHanoi(num-1, From, Help, To)
		show.MakeAMove(From, To, A, B, C)
		RecHanoi(num-1, Help, To, From)

class task:  #tasks to be make in loop 
	def __init__(self, num, From, To, Help):
		self.From=From;
		self.To=To;
		self.Help=Help;
		self.num=num;

def NonrecHanoi (num):
	stackOfTasks = []
	stackOfTasks.append(task(num, A, C, B))
	while stackOfTasks !=[]:
		x=stackOfTasks.pop()
		if x.num==1:
			show.MakeAMove(x.From, x.To, A, B, C)
		else:
			stackOfTasks.append(task(x.num-1, x.Help, x.To, x.From))
			stackOfTasks.append(task(1, x.From, x.To, x.Help))
			stackOfTasks.append(task(x.num-1, x.From, x.Help, x.To))


	
def hanoi (a):  #comment one
	NonrecHanoi(a)
	#RecHanoi(a)       
	
a = int(input('Enter amount of blocks:'))
for i in range(a, 0, -1): #initialize Stack
	A.append(i)
show.ShowHanoi(A, B, C)
(hanoi(a))
