# &
print(50*'-')

values = ['valeur 01','valeur 02','valeur 03','valeur 04']


for value in values:
    print(value)


for i in range(12):
    print(i)

# 0 valeur 01
# 1 valeur 02
# 2 valeur 03
print(50*"-")
for i in range(len(values)):
    print(str(i)+" "+values[i])
    print(i,values[i])


print(list(range(10)))


values = [2,3,5,6]

result = 0
for i in values:
    result += i # result = result+i

print(result)
print(50*"-")
values = [2,3,5,6,10,5]
for v in values:
    if v == 6:
        print("ok")    
        continue
    print(v)
else:
    print("pas trouvé")



print(50*"-")
def fib(n:int=12):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n. Et c'est vraiment bien !"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n:int)->list:    # Return Fibonacci series up to n
    """Return  a Fibonacci series up to n."""
    r = []
    a, b = 0, 1
    while a < n:
        r.append(a)
        a, b = b, a+b
    return r

# Now call the function we just defined:
fib(2000)
r = fib2(200)
print(r) # => [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]


print(50*'-')
fib(10000)
print(50*'-')
fib(n=10000)
print(50*'-')


def add(*the_list):
    print(the_list)
    result = 0
    for i in the_list:
        result += i # result = result+i
    return result

a = [1,2,3,4]

# b = add(*a)  
b = add(1,2,3,4,45,76,34)  
print(b) # 10


def hello(**kwargs):
    print(kwargs)
    print("Bonjour",kwargs['name'],kwargs['firstname'])


hello(firstname="Frédéric",name="GAURAT",age=46,job="dev")




print(50*"-")

l = [1,2,3,4,5]

def mult2(i):
    return i*2

# l2 = list(map(mult2,l))
l2 = list(map(lambda i: i*2,l))

print(l2)
