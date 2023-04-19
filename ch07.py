



def main():
    a=2
    b=3
    c=a/b
    result = f"résultat de {a} / {b}  = {c:30.2%}"
    print(result)

    s = "toto"
    print(f"|{s:>30}|")
    
    result = f"résultat de {a=} / {b=}  = {c:30.2%}"
    print(result)

    a=2
    b=3
    c=a/b
    
    s = "a:{}/b:{} = c:{:0.2%}".format(a,b,c)
    print(s)

    s = "{0}/{1} = {2:0.2%}".format(a,b,c)
    print(s)

    l = [1,2,3]
    s = "{0} {1} {2}".format(*l)
    # s = "{0} {1} {2}".format(1,2,3)
    print(s)

    s = "{name} {firstname}".format(name="GAURAT",firstname="Fred")
    print(s)
    
    d = {
        "name":"GAURAT",
        "firstname":"Fred"
    }
    # "name"="GAURAT","firstname"="Fred"
    s = "{name} {firstname}".format(**d)
    print(s)


if __name__ == '__main__':
    main()