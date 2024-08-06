n = input()
code = []
for i in n:
    if i != '<':
        code.append(i)
    else:
        code.pop()
judge = [0,0,0,0,0]
if len(code) >= 8:
    judge[0] = 1
for i in code:
    if 'A' <= i <= 'Z':
        judge[1] = 1
    elif 'a' <= i <= 'z':
        judge[2] = 1
    elif '0' <= i <= '9':
        judge[3] = 1
    else:               #其余情况全是特殊字符
        judge[4] = 1
if not 0 in judge:
    code.append(',true')
else:
    code.append(',false')
print(''.join(code))