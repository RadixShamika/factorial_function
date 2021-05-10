#N!

def factorial():
	n = int(input("Enter number :- "))
	sum = n
	x = 1
	while (x < n):
		fact = n - x
		sum = sum + fact
		x = x + 1
        print(sum)
factorial()
