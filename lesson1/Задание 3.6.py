def int_func(word):
    small_w = word[0]
    big_w = chr(ord(small_w) - ord('a') + ord('A'))
    return big_w + word[1:]
source = input().split()
res = []
for word in source:
    res.append(int_func(word))
print(' '.join(res))




