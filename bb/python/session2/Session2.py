# Python Session #2
# Data Structures
# Code to accompany the slides

# Typing and Variables (4&5)

a=1
b="Glenn"

type(a)                             # <type 'int'>
type(b)                             # <type 'str'>

# Weak (or dynamic) typing (4)

a="Sugden"

type(a)                             # (Now a) <type 'str'>(!)

c=1.0

type(c)                             # type <'float'>

d=complex(3,4)
print d                             # 3+4j
type(d)                             # type <'complex'>

type(type(1))                       # <type 'type'>

b,c=3,4
print b                             # 3
print c                             # 4

# Looping and Conditionals (6)

x = 0
while(x<10):
    print x                         # 0 1 2 3 4 5 6 7 8 9 (on each line)
    x=x+1

a=3*5+6
print a                             # 21

a=3*(5+6)
print a                             # 33

True or False                       # True
True and False                      # False
not False                           # True
a=1
b=2
c=3
d=2
a<b                                 # True
b<=d                                # True
b<=a                                # False
c>b                                 # True
b>=d                                # True
a==b                                # False
b==d                                # True
a=c                                 # (nothing printed) but a=3 now!
type(a) is type(d)                  # True
type(c) is not type(b)              # False

if (b>d):
    print "b is greater than d"
else:
    print "b is not greater than d"
                                    # b is not greater than d"

if (a>c):
    print "a is greater than c"
elif (a==c):
    print "a equals c"
else:
    print "a is less than c"
                                    # "a equals c"

for x in range(0,10):
    print x                         # 0 1 2 3 4 5 6 7 8 9 (on each line)

# Functions (7)

def func(x):
    print x

func(10)                            # (10 is printed, evaluated func())

def func(a):
    a=3

x=4
func(x)                             # (x is still 4)
print x                             # 4

def func(a):                        # (a is unused)
    global x
    x=3

func(x)
print x                             # 3

def sum(a,b):
    return a+b

print sum(4,5)                      # 9

def sumAndProduct(a,b):
    sum = a+b
    prod = a*b
    return sum, prod                # (note the comma)

x=5
y=7
g,h = sumAndProduct(x,y)
print g                             # 12
print h                             # 35

# Recursion (8)

def factorial(n):
    if (n==0):
        return 1
    else:
        return n * factorial(n-1)

print factorial(10)                 # 3628800

# Sequences (overview) (9)

a = "Hello, World!"                 # String
a = U"I love "                     # Unicode String
a = R"This isn't a \newline"        # Raw string
a = "This has a \newline"           # This has a
print a                             # ewline
b = (0,1,2,3)                       # List
c = (4,5,6,7)                       # Tuple
d = range(0,10)                     # List from 0-9
print d                             # (0,1,2,3,4,5,6,7,8,9)

# String and String Operators (slide 11)

a = " 'this is single quoted' "     # "Quoted" string:
print a                             #  'this is single quoted'
print """this has
multiple
lines"""                            # this has
                                    # multiple
                                    # lines
print '"This is double quoted"'     # "This is double quoted"

a = "Bad"
b = "Kitty!"
c = a + " " + b
print c                             # Bad Kitty!

print "%d University Ave." % 1122   # 1122 University Ave.
print "%s is about %f"%("pi",3.14)  # pi is about 3.140000
print "%1.2f"%3.14159               # 3.14

len(c)                              # 10

print c[0]                          # B
print c[1]                          # a
print c[0:3]                        # Bad
print c[:3]                         # Bad
print c[3:]                         #  Kitty!
print c[7:8]                        # t
print c[-4]                         # i
print c[-4:-2]                      # it
print c[::2]                        # BdKty
print c[1:8:2]                      # a it

# Lists [12]

a=[2,1,0]
print a                             # [2,1,0]
b=[a,a,a]
print b                             # [[2,1,0],[2,1,0],[2,1,0]]
print a[1]                          # 1
print b[1]                          # [2,1,0]
print b[1][2]                       # 0
a[1]=3
print a                             # [2,3,0]
print b                             # [[2,3,0],[2,3,0],[2,3,0]]
b[1][2]=4
print b                             # [[0, 3, 4], [0, 3, 4], [0, 3, 4]]
c=['a','b','c','d','e','f']
print c[1]                          # b
print c[1:3]                        # ['b','c']
c[1:3]=5                            # ERROR
c[1:3]=[5]
print c                             # ['a',5,'d','e','f']
c[-2]                               # ['e']
c.append('boo!')
print c                             # ['a', 5, 'd', 'e', 'f', 'boo!']
c.insert(1,'wow!')
print c                             # ['a', 'wow!', 5, 'd', 'e', 'f', 'boo!']
c.append(5)
c.append(5)
print c.count(5)                    # 3
d=[5,4,3,2,1]
d.sort()
print d                             # [1,2,3,4,5]

# Tuples (13)

a=(2,1,0)
print a                             # (2,1,0)
b=(a,a,a)
print b                             # ((2,1,0),(2,1,0),(2,1,0))
print a[1]                          # 1
print b[1]                          # (2,1,0)
print b[1][2]                       # 0
a[1]=3                              # ERROR
print a                             # (2,1,0)
print b                             # ((2,1,0),(2,1,0),(2,1,0))
b[1][2]=4                           # ERROR
print b                             # ((2,1,0),(2,1,0),(2,1,0))
c=('a','b','c','d','e','f')
print c[1]                          # b
print c[1:3]                        # ('b','c')
c[1:3]=5                            # ERROR
c[1:3]=(5)                          # ERROR
c[1:3]=[5]                          # ERROR
print c                             # ('a','b','c','d','e','f')
c[-2]                               # ('e')
c.append('boo!')                    # ERROR
print c                             # ('a','b','c','d','e','f')
c.insert(1,'wow!')                  # ERROR
print c                             # ('a','b','c','d','e','f')
c.append(5)                         # ERROR
c.append(5)                         # ERROR
print c.count(5)                    # 0
d=(5,4,3,2,1)
d.sort()                            # ERROR
print d                             # (5,4,3,2,1)

a=(0,1,2,3,4,5,6,7,8,9)
b=(10,11,12,13,14,15,16)
c=(100,101,102,103,104)
d={a:"single",b:"double",c:"triple"}
print d[a]                          # single

# Ranges (and xRanges) [15]

a=range(0,10)
print a                             # [0,1,2,3,4,5,6,7,8,9]
a=range(0,10,2)
print a                             # [0,2,4,6,8]

b=xrange(0,100)
print b                             # xrange(100)
for i in xrange(0,10,2):
    print i                         # 0, 2, 4, 6, 8 (on each line)

# Iterators [16]

b=xrange(0,100)
it=iter(b)
print i                             # <rangeiterator object at 0x######>
it.next()                           # 0
it.next()                           # 1
it.next()                           # 2
it.next()                           # 3

# Sequence (general) Operators [17]

a=[0,1,2,3,4,5,6]

print 4 in a                        # True
print 8 in a                        # False
print 4 not in a                    # False
print 8 not in a                    # True

b=[7,8,9]
print a+b                           # [0,1,2,3,4,5,6,7,8,9]

c=[1,2]
d=c*4
print d                             # [1,2,1,2,1,2,1,2]

len(d)                              # 8

min(a)                              # 0
max(a)                              # 6

# Sets [18]

a=[0,1,2,3,1,2,3,4,5,6]
print a                             # [0, 1, 2, 3, 1, 2, 3, 4, 5, 6]
s=set(a)
print s                             # set([0, 1, 2, 3, 4, 5, 6])
print s[0]                          # ERROR
b=set("blah")
print b                             # set(['a', 'h', 'B', 'l'])
print 0 in s                        # True

# Set Operations [19]

a=set([0,1,2,3,4,5,6])
b=set([3,4,5,6,7,8,9])
print len(a)                        # 7

b.add(10)
print b                             # set([3, 4, 5, 6, 7, 8, 9, 10])

2 in a                              # True
2 in b                              # False

a.remove(5)
print a                             # set([0, 1, 2, 3, 4, 6])

a.pop()                             # 0
print a                             # set([1, 2, 3, 4, 6])

a=a-set([1,2])
print a                             # set([3, 4, 6])

it=iter(a)
it.next()                           # 3
it.next()                           # 4
it.next()                           # 6

print a.union(b)                    # set([3, 4, 5, 6, 7, 8, 9, 10])
print a.intersection(b)             # set([3, 4, 6])

# Dictionaries [20]

a={}
print a                             # {}
type(a)                             # <type 'dict'>

a['foo']=4

print a                             # {'foo': 4} (foo is key, 4 is value)

print a['foo']                      # 4

a['bar']=5
a['glug']='a string'
a['blork']=[3,4,5]
print a       # {'glug': 'a string', 'foo': 4, 'bar': 5, 'blork': [3, 4, 5]}
print a.keys()                      # ['glug', 'foo', 'bar', 'blork']

a.has_key('foo')                    # True
a.has_key('blah')                   # False
'foo' in a                          # True
'blah' in a                         # False

it=iter(a)
print it.next()                     # glug
print it.next()                     # foo
for key in a:
    print "key="+str(key)
    print "value="+str(a[key])
                                    # key=glug
                                    # value=a string
                                    # key=foo
                                    # value=4
                                    # key=bar
                                    # value=5
                                    # key=blork
                                    # value=[3, 4, 5]
