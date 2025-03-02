def multi(n):
	i=1
	while i<=n:
		print("[", end="")
		j=1
		while j<n:
			print(i*j,", ",end="")
			j = j+1
		print(n*i,end="")
		i = i+1
		print("]")
			

n = int(input())
multi(n)

