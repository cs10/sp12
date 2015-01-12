class Counter:
	""" A simple class that holds a counter, as well as the total
		number of counters. """
	totalCounters = 0
	def __init__(self):
		self.myCount = 0
		Counter.totalCounters = Counter.totalCounters + 1
	def increment(self):
		self.myCount += 1
	def reset(self):
		self.MyCount = 0
	def currentCount(self):
		return( self.myCount)

c1 = Counter()
print Counter.totalCounters						#	1
c1.currentCount()								#	0
c1.increment()
c1.currentCount()								#	1
c1.increment()
c1.currentCount()								#	2
c2 = Counter()
print Counter.totalCounters						#	2
c2.currentCount()								#	0
c2.increment()
c1.currentCount()								#	2
c2.currentCount()								#	1

c1.__doc__
#	' A simple class that holds a counter, as well as the total\n\t\tnumber of counters. '

print c1.__doc__
#	 A simple class that holds a counter, as well as the total
#			number of counters.

help(Counter)
#
#	Help on class Counter in module __main__:
#
#	class Counter
#	 |	A simple class that holds a counter, as well as the total
#	 |	number of counters.
#	 |
#	 |	Methods defined here:
#	 |
#	 |	__init__(self)
#	 |
#	 |	currentCount(self)
#	 |
#	 |	increment(self)
#	 |
#	 |	reset(self)
#	 |
#	 |	----------------------------------------------------------------------
#	 |	Data and other attributes defined here:
#	 |
#	 |	totalCounters = 2
#	(END)

class NamedCounter:
	""" A simple (standalone) counter class that holds a counter with a name,
		along with the total number of counters. Notice the duplicate code! """
	totalCounters = 0
	def __init__(self,name):
		self.myCount = 0
		self.myName = name
		NamedCounter.totalCounters += 1
	def increment(self):
		self.myCount += 1
	def reset(self):
		self.MyCount = 0
	def __str__(self):
		return( self.myName)
	def currentCount(self):
		return( self.myCount)

nc1=NamedCounter()
#	Traceback (most recent call last):
#	  File "<stdin>", line 1, in <module>
#	TypeError: __init__() takes exactly 2 arguments (1 given)

nc1=NamedCounter("Yay! A named counter!")
print nc1										#	Yay! A named counter!

nc2=NamedCounter("Yay! Another named counter!")
print nc2										#	Yay! Another named counter!

print NamedCounter.totalCounters				#	2

print NamedCounter.__doc__
#	 A simple (standalone) counter class that holds a counter with a name,
#			along with the total number of counters. Notice the duplicate code!

################################################################################

class NamedCounter(Counter):
	""" A simple named class that inherits from the Counter class,
		only overriding what it needs to (e.g., __init__). """
	def __init__(self,name):
		Counter.__init__(self)
		self.myName = name
	def __str__(self):
		return( self.myName)

nc1=NamedCounter("Yay! Inherited named counter!")
nc1.increment()
print nc1.currentCount()						#	1
print nc1.__doc__
#	 A simple named class that inherits from the Counter class,
#			only overriding what it needs to (e.g., __init__)
print NamedCounter.totalCounters				#	3

################################################################################

class Account:
	""" A "parent class" that will be the basis for specialized accounts. """
	numberOfAccounts = 0
	def __init__(self,name,startingBalance=0):
		self.myName = name
		self.myBalance = startingBalance
		Account.numberOfAccounts += 1
	def balance(self):
		return( self.myBalance)
	def deposit(self,amount):
		self.myBalance += amount
	def withdrawl(self,amount):
		if (self.myBalance < amount):
			print "OH NOES! CAN'T OVERDRAW THIS ACCOUNT!"
		else:
			self.myBalance -= amount
	def __str__(self):
		return( "Account (" + self.myName + "):\n\tBalance: $" + str(self.myBalance))

class CheckingAccount(Account):
	""" A "child class" that is a specialized version of Account (checking). """
	def __init__(self,name,startingBalance=0):
		Account.__init__(self,"Checking+"+name,startingBalance)

class FakeInterestCheckingAccount(CheckingAccount):
	""" A "child class" that is further specialized as a "sub-type" of CheckingAccount. """
	def __init__(self,name,interest,startingBalance=0):
		Account.__init__(self,"FakeInterestCheckingAccount+"+name,startingBalance)
		self.myInterest = interest
	def deposit(self,amount):
		Account.deposit(self,amount)
		print "Adding (fake) interest: " + str(amount*self.myInterest)
		Account.deposit(self,amount*self.myInterest)

class SavingsAccount(Account):
	""" A "child class" that is a specialized version of Account (savings). """
	def __init__(self,name,startingBalance=0):
		Account.__init__(self,"Savings+"+name,startingBalance)

class CreditCardAccount(Account):
	""" A "child class" that is a specialized version of Account (credit),
		in which the balance is allowed to go below 0 (you own monies). """
	def __init__(self,name,startingBalance=0):
		Account.__init__(self,"Credit+"+name,startingBalance)
	def withdrawl(self,amount):
		self.myBalance -= amount

myCheckingAccount = CheckingAccount("Glenn's Non-interested",13)
myFICheckingAccount = FakeInterestCheckingAccount("Glenn's interested!",0.10,42)
mySavingsAccount = SavingsAccount("Glenn's Savings",666)
myCreditCardAccount = CreditCardAccount("Glenn's Credit")

print Account.numberOfAccounts					#	4

print myCheckingAccount.balance()				#	13
print myCheckingAccount							#	Account (Checking+Glenn's Non-interested):
												#		Balance: $13
myCheckingAccount.deposit(100)
print myCheckingAccount							#	Account (Checking+Glenn's Non-interested):
												#		Balance: $113

print myFICheckingAccount						#	Account (FakeInterestCheckingAccount+Glenn's interested!):
												#		Balance: $42
myFICheckingAccount.deposit(100)				#	Adding (fake) interest: 10.0
print myFICheckingAccount						#	Account (FakeInterestCheckingAccount+Glenn's interested!):
												#		Balance: $152.0

myCheckingAccount.withdrawl(50)
print myCheckingAccount							#	Account (Checking+Glenn's Non-interested):
												#		Balance: $63
myCheckingAccount.withdrawl(10000)				#	OH NOES! CAN'T OVERDRAW THIS ACCOUNT!
print myCheckingAccount							#	Account (Checking+Glenn's Non-interested):
												#		Balance: $63

print mySavingsAccount							#	Account (Savings+Glenn's Savings):
												#		Balance: $666
mySavingsAccount.withdrawl(10000)				#	OH NOES! CAN'T OVERDRAW THIS ACCOUNT!
print mySavingsAccount							#	Account (Savings+Glenn's Savings):
												#		Balance: $666

print myCreditCardAccount						#	Account (Credit+Glenn's Credit):
												#		Balance: $0
myCreditCardAccount.withdrawl(10000)
print myCreditCardAccount						#	Account (Credit+Glenn's Credit):
												#		Balance: $-10000

isinstance(myCheckingAccount,CheckingAccount)	#	True
isinstance(myCheckingAccount,SavingsAccount)	#	False

issubclass(CheckingAccount,Account)				#	True
issubclass(SavingsAccount,Account)				#	True
issubclass(SavingsAccount,CheckingAccount)		#	False

print Account.__dict__
# {'__module__': '__main__', '__str__': <function __str__ at 0x10059a140>,
#	'deposit': <function deposit at 0x10059a7d0>, 'numberOfAccounts': 5,
#	'balance': <function balance at 0x10059a758>,
#	'__doc__': ' A "parent class" that will be the basis for specialized accounts. ',
#	'__init__': <function __init__ at 0x10059ac08>,
#	'withdrawl': <function withdrawl at 0x10059acf8> }

################################################################################

class Parent:
	""" A parent class that has a variable named 'x' in it. """
	def __init__(self):
		self.x=0
	def getX(self):
		return(self.x)
	def setX(self,newX):
		self.x=newX

class Child(Parent):
	""" A child class that references the parent's variable named 'x'. """
	def __init__(self):
		Parent.__init__(self)
	def getX(self):
		return(Parent.getX(self))
	def setX(self,newX):
		Parent.setX(self,newX)

p=Parent()
c=Child()

print p.getX()									#	0
print p.x										#	0
print c.x										#	0

c.setX(10)

print c.x										#	10
print p.x										#	0

c.getX()										#	10
c.setX(13)
c.getX()										#	13
p.getX()										#	0

class Child(Parent):
	""" A child class that references *it's own local* variable named 'x'. """
	def __init__(self):
		Parent.__init__(self)
		self.x=1								# <==
	def getX(self):
		return(self.x)							# <==
	def setX(self,newX):
		self.x=newX								# <==

p=Parent()
c=Child()

print p.getX()									#	0
print p.x										#	0
print c.x										#	1	<==

c.setX(10)

print c.x										#	10
print p.x										#	0

c.getX()										#	10
c.setX(13)
c.getX()										#	13
p.getX()										#	0

################################################################################

class HasPrivateVariables:
	""" A  class that has two variables, one of them public ('x'), and
		one of them is private ('__x'), which you can't access globally. """
	def __init__(self):
		self.x = 1
		self.__x = 13
	def getMyX(self):
		return self.__x
	def setMyX(self,val):
		self.__x = val

foo = HasPrivateVariables()
print foo.x										#	1
print foo.__x
#	Traceback (most recent call last):
#	  File "<stdin>", line 1, in <module>
#	AttributeError: HasPrivateVariables instance has no attribute '__x'

foo.getMyX()									#	13

foo.setMyX(666)
print foo.x										#	1
print foo.__x
#	Traceback (most recent call last):
#	  File "<stdin>", line 1, in <module>
#	AttributeError: HasPrivateVariables instance has no attribute '__x'

foo.getMyX()									#	666

################################################################################

class A:
	totalCount = 0
	def __init__(self):
		A.totalCount += 1
	def __del__(self):
		A.totalCount -= 1

a1 = A()
print A.totalCount								#	1

a2 = A()
print A.totalCount								#	2

a3 = A()
print A.totalCount								#	3

del a3
print A.totalCount								#	2

b = a1
print A.totalCount								#	2 (didn't increase)

del a1
print A.totalCount								#	2 (didn't decrease!)

del b
print A.totalCount								#	1 (NOW it can delete a1!)

del a2
print A.totalCount								#	0

################################################################################

class Card:
	def __init__(self,suit,faceValue):
		self.mySuit = suit
		self.myFaceValueLetter = faceValue
		if (faceValue == 'A'):
			self.myValue = 1
		elif (faceValue == 'J'):
			self.myValue = 11
		elif (faceValue == 'Q'):
			self.myValue = 12
		elif (faceValue == 'K'):
			self.myValue = 13
		else:
			self.myValue = faceValue
	def __str__(self):
		stringSoFar = str(self.myFaceValueLetter) + " of "
		if (self.mySuit == 'H'):
			return stringSoFar + "hearts"
		elif (self.mySuit == 'S'):
			return stringSoFar + "spades"
		elif (self.mySuit == 'C'):
			return stringSoFar + "clubs"
		else:
			return stringSoFar + "diamonds"

two_of_hearts = Card('H',2)
three_of_hearts = Card('H',3)
king_of_hearts1 = Card('H','K')
king_of_hearts2 = Card('H','K')

hash(two_of_hearts)								#	4300686760
hash(three_of_hearts)							#	4300712776
hash(king_of_hearts1)							#	4300695960
hash(king_of_hearts2)							#	4300712632

print two_of_hearts

print two_of_hearts == two_of_hearts			#	True
print two_of_hearts == three_of_hearts			#	False
print king_of_hearts1 == king_of_hearts2		#	False

myCards = set([two_of_hearts,three_of_hearts,king_of_hearts1,king_of_hearts2])
print myCards
# set([	<__main__.Card instance at 0x10057ab48>,
# 		<__main__.Card instance at 0x10057aea8>,
# 		<__main__.Card instance at 0x10057ae60>,
# 		<__main__.Card instance at 0x10057ae18>	])

class Card:
	def __init__(self,suit,faceValue):
		self.mySuit = suit
		self.myFaceValueLetter = faceValue
		if (faceValue == 'A'):
			self.myValue = 1
		elif (faceValue == 'J'):
			self.myValue = 11
		elif (faceValue == 'Q'):
			self.myValue = 12
		elif (faceValue == 'K'):
			self.myValue = 13
		else:
			self.myValue = faceValue
	def __str__(self):
		stringSoFar = str(self.myFaceValueLetter) + " of "
		if (self.mySuit == 'H'):
			return stringSoFar + "hearts"
		elif (self.mySuit == 'S'):
			return stringSoFar + "spades"
		elif (self.mySuit == 'C'):
			return stringSoFar + "clubs"
		else:
			return stringSoFar + "diamonds"
	def __cmp__(self,other):						#	<==
		return hash(self)-hash(other)				#	<==
	def __hash__(self):								#	<==
		return (ord(self.mySuit)*100+self.myValue)	#	<==

two_of_hearts = Card('H',2)
three_of_hearts = Card('H',3)
king_of_hearts1 = Card('H','K')
king_of_hearts2 = Card('H','K')

hash(two_of_hearts)								#	7202
hash(three_of_hearts)							#	7203
hash(king_of_hearts1)							#	7213
hash(king_of_hearts2)							#	7213

print two_of_hearts == two_of_hearts			#	True
print two_of_hearts == three_of_hearts			#	False
print king_of_hearts1 == king_of_hearts2		#	True	<===

myCards = set([two_of_hearts,three_of_hearts,king_of_hearts1,king_of_hearts2])
print myCards
# set([	<__main__.Card instance at 0x10057a908>,
# 		<__main__.Card instance at 0x10057a998>,
# 		<__main__.Card instance at 0x10057add0>	])
