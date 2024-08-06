a = bin(int(input()))
count = 0
for i in a:
    if i == '1':
        count = count + 1
    else:
        continue
print(count)