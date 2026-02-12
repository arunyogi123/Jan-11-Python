def six(*n):
    p = list(n)
    for i in p:
        p[0] = i + 6
        break
    return tuple(p)


print(six())


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n + fact(n - 1)


print(fact(5))


def fact(n):
    if len(n) == 0:
        return 0
    else:
        return 1 + fact(n[1:])


print(fact([4]))

# def  six(*n):
#     p=list(n)
#     if len(p)==0:
#         return "pass any args in six function"
#     p[0]=p[0]+6
#     return tuple(p)

# print(six(2,3,4,5))
# print(six(9,8))
# print(six())


# pass any args in six function


def six(*n):
    p = list(n)
    for i in p:
        p[0] = i + 6
        break
    return tuple(p)


def test():
    print(" i am test func ")
    test()


# test()


# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result = result*i
#     print(result)
#     return result

# fact(5)


def fact(n):
    
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


def add(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n + add(n - 1)


print(add(2))

# Write a recursive function to count digits in a number.
