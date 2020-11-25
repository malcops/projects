import pytest


index = 1
fibonacci = [1, 1]
while True:
    fibonacci.append(fibonacci[index] + fibonacci[index-1])
    index += 1
    print(fibonacci[index])
    if len(str(fibonacci[index])) == 1000:
        print(index)
        break

# index of fibonacci array is offset by 1
# fibonnaci[0] = F1
print("answer: {}".format(index + 1))

