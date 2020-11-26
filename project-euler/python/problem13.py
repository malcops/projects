
sum = 0

with open("problem13.txt", "r") as f:
    for line in f:
        sum += int(line)

answer = str(sum)
answer = answer[0:10]
print(answer)

