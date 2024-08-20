def f2(d, c):       # d = 30
    return c - d    # c = 10

# c와 d 데이터가 f2로 넘어감


def f1(b, a):        # b = 10  10은 그대로 있고 b 인자가 먼저 들어왔으므로 순서가 b = 10
    c = a + b        # a = 20  20은 그대로 있고 a 인자가 후에 들어왔으므로 순서가 a = 20
    d = 10           # c = 30  데이터는 그대로 있고 인자가 바뀌는 형태
    return f2(c, d)  # d = 10

# a와 b 데이터가 f1로 넘어감


a = 10               # a = 10
b = 20               # b = 20
print(f1(a, b))

"""
def f2(c, d):       # c = 30
    return c - d    # d = 10
    
# c와 d 데이터가 f2로 넘어감
                                
                                
def f1(a, b):        # a = 10
    c = a + b        # b = 20
    d = 10           # c = 30
    return f2(c, d)  # d = 10 

# a와 b 데이터가 f1로 넘어감


a = 10               # a = 10
b = 20               # b = 20
print(f1(a, b))
"""