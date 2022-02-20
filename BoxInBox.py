n = int(input("enter size: "))
table = [["  " for i in range(n)] for j in range(n)]
done=False

# adding starts to the table
for i in range(0,n,2):
	if (done):
		break
	for x in range(i,n-i):
		table[i][x]="* "
		table[x][i]="* "
		table[n-i-1][x]="* "
		table[x][n-i-1]="* "
	if(n%2==1 and i == n/2+1):
		table[i][i] = "* "
		done = True

# print the table
print()
for row in table:
	for col in row:
		print(col,end=" ")
	print()
print()



