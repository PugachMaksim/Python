A = int(input())
B = int(input())
def rez(a, b):
    if a < 0:
        if a == 0:
            return b
        return rez(a + 1, b - 1)
    else:
        if a == 0:
            return b
        return rez(a - 1, b + 1)
print(rez(A, B))