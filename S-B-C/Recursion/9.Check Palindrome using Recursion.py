def reverse_num(n, rev):
    if n == 0:
        return rev
    rev = rev * 10 + n % 10
    return reverse_num(n // 10, rev)
n = int(input())
ori = n
reversed_num = reverse_num(n, 0)
if ori == reversed_num:
    print(True)
else:
    print(False)