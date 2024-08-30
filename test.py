a = int('1E06079861E79F99FE079861E79F8', 16)
print(a)
b = bin(a)
print(b)

pw = '0011110000001100000011110011000011000011110011110011111100110011111111000000111100110000110000111100111100111111'
l = len(pw)
ratio_01 = []
counts = 1

for i in range(1, len(pw)):
    if pw[i] == pw[i-1]:
        counts += 1
    else:
        ratio_01 += [counts]
        counts = 1
else:
    ratio_01 += [counts]
print(ratio_01)