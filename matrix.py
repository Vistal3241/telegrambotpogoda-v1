n=int(input("n="))
if n==3:
	a=[[0,0,0],[0,0,0],[0,0,0]]
	b=[0,0,0]
	for i in range(3):
		for j in range(3):
			a[i][j]=int(input("Enter number(a["+str(i+1)+"]["+str(j+1)+"]): "))
	for i in range(3):
		for j in range(3):
			b[j]=a[i][j]
		print(b)
	c=a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[1][0]*a[2][1]*a[0][2]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[1][2]*a[2][1]*a[0][0]
	print(c)
elif n==2:
	a=[[0,0],[0,0]]
	b=[0,0]
	for i in range(2):
		for j in range(2):
			a[i][j]=int(input("Enter number(a["+str(i+1)+"]["+str(j+1)+"]): "))
	for i in range(2):
		for j in range(2):
			b[j]=a[i][j]
		print(b)
	print(a)
	c=a[0][0]*a[1][1]-a[0][1]*a[1][0]
	print(c)
