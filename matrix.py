n=int(input("n="))
def func(a):
	c=a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[1][0]*a[2][1]*a[0][2]-a[0][2]*a[1][1]*a[2][0]-a[0][1]*a[1][0]*a[2][2]-a[1][2]*a[2][1]*a[0][0]
	return c
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
	c=func(a)
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
elif n==4:
	a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	b=[0,0,0,0]
	c=[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(4):
		for j in range(4):
			a[i][j]=int(input("Enter number(a["+str(i+1)+"]["+str(j+1)+"]): "))
	for i in range(4):
		for j in range(4):
			b[j]=a[i][j]
		print(b)
	for i in range(3):
		for j in range(3):
			c[i][j]=a[i+1][j+1]
	a1=a[0][0]
	b1=func(c)
	for i in range(3):
		for j in range(3):
			c[i][j]=a[i+1][j-2]
	a2=a[0][1]
	b2=func(c)
	for i in range(3):
		for j in range(3):
			c[i][j]=a[i+1][j-1]
	a3=a[0][2]
	b3=func(c)
	for i in range(3):
		for j in range(3):
			c[i][j]=a[i+1][j]
	a4=a[0][3]
	b4=func(c)
	d=a1*b1+a2*(-1)*b2+a3*b3+a4*(-1)*b4
	print(d)
