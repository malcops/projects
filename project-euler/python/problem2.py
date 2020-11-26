x1 = 1
x2 = 2
tmp = 0
terms = []

while (x1 < 4000000):
    tmp = x1 + x2
    print(x1)
    if (x1%2 == 0):
        terms.append(x1)
    x1 = x2
    x2 = tmp

print(sum(terms))

