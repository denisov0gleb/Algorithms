def countdown(n):
	if n <= 0:
		print(0)
		return 0
	else:
		print(n)
		return countdown(n - 1)
	
def countup(n):
    if n <= 0:
        print(0)
        return
    else:
        countup(n - 1)
        print(n)

countup(5) # 0 1 2 3 4 5
print()
countdown(5) # 5 4 3 2 1 0