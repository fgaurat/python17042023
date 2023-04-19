
l = [3,4,1,10]
print(l)
l2 = sorted(l)
print(l)
print(l2)
# print(l)
# last = l.pop()
# print(l)
# print(last)
l = [3,4,1,10]

l.insert(0,1000)
print(l)
first = l.pop(0)
print(first)
print(l)

from collections import deque

l = [3,4,1,10]
queue = deque(l)

queue.append(500)
last = queue.pop()
queue.appendleft(1000)
first = queue.popleft()
print(queue)

l = []

for i in range(10):
    l.append(i*2)

print(l)

l = list(map(lambda i:i*2,range(10)))
print(l)

l = [i*2 for i in range(10)]
print(l)
l = ["   toto   ","    tutu","tata    ","titi"]
clean_l = [s.strip() for s in l]
print(l)
print(clean_l)
del clean_l[-1]
print(clean_l)

print(50*"-")
l = [1,2,3,4,5]
print(l)
d = {'k1':'v1','k2':'v2'}
print(d)
t = 12,3
print(t)
a,b=0,1
# a[0]= 100
a=0,1
print(a)
a,b,*c=0,1,2,3,4
print(a,b,c)

def f():
    return 1,2

a,b = f()
print(50*"-")

s = {"value 01","value 05","value 01","value 02","value 06"}


s1={"value 01"}
s2 = s - s1
# for item in s:
#     if item != "value 01":
#         s1.add(item)

print(s)
print(s1)
print(s2)
print(50*'-')

# d = {"user":"root","password":"12345","projects":['project 01','project 02','project 03']}
d = {"user":"root","password":"12345"}

print(d)
print(d['user'])
d['user'] = "admin"
print(d)

for k in d:
    print(k,d[k])

l = ["value 01","value 05","value 01","value 02","value 06"]

for i,v in enumerate(l):
    print(i,v)

for k,v in d.items():
    print(k,v)


d = {"user":"root","password":"12345"}
d = dict(
    [
    ("user",'root'),
    ("password","12345")
    ]
)
