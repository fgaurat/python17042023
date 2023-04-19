print("Hello")

# TheValueOfTheTp => UpperCamelCase, PascalCase
# theValueOfTheTp => camelCase
# the_value_of_the_tp => snake_case
# the-value-of-the-tp => train-case, spin-case, kebab-case

the_value_of_the_tp = True

if the_value_of_the_tp:
    print("ok")
    # print("ok")


toto = "toto"
titi = "titi"
print(toto+titi)


a = 2
b = 3
print(a+b)
r = "la valeur de a : "+str(a)
print(r)


s = 'L\'orage gronde'
s = "L'orage gronde"
print(s)
# path = "c:\\num\\test"
path = r"c:\num\test"
print(path)


print("-"*50)
print("la suite ..")

s2 = """Ligne 1
Ligne 2
Ligne 3
"""
print(s2)
print("-"*50)
word = "Python"
print(len(word))
print(word[0])
print(word[len(word)-1])
print(word[-1])
print(word[-2])
print(word[1:3])
print(word[3:])
print(word[:3])

s = "toto"
# s[0] = "l"
print(s)

s = "tutu"


a = 2
b = 2

print(id(a))
print(id(b))

print("-"*50)
a = [1,4,9,16,25]
print(a[-1])
a[0] = 1000
print(a[0])
# print(a)
b = a[:]
b[0]=1
print(a)
print(b)
print("-"*50)

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
import copy 
b = copy.deepcopy(a)
print(a[1][1])
a[1][1] = 1000
print("--")
print(a[1][1])
print(b[1][1])

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
    