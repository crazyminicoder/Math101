def nextPermutation(num):
    i = len(num)-2
    while i >= 0 and num[i] >= num[i+1]:
        i -= 1

    if i == -1:
        return num[::-1]
    j = len(num)-1
    while num[j] <= num[i]:
        j -= 1

    num[i], num[j] = num[j], num[i]

    num[i+1:] = reversed(num[i+1:])

    return num


number = [3, 2, 1]
res = nextPermutation(number)
print(res)
