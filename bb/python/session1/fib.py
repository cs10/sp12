# Beyond Blocks : Python : Session #1 by Glenn Sugden is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

def fib( n ):
	if ( n == 0 ):
		return 0
	elif ( n == 1 ):
		return 1
	else:
		return fib( n -2 ) + fib( n - 1)

print fib(10)
print fib(20)
