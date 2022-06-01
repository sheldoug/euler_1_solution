import sys

def euler(x):
    x = len(sys.argv)
    ans = 0
    i = 0
    while i < x:
        if i % 3 == 0 or i % 5 == 0:
            ans += i
        i = i + 1

    print(ans)

euler(sys.argv[0])

