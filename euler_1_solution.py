import sys

print("Enter value: ")
def euler(x):
    x = int(input(sys.argv[0]), base = 0)
    ans = 0
    i = 0
    while i < x:
        if i % 3 == 0 or i % 5 == 0:
            ans += i
        i = i + 1

    print(ans)

euler(sys.argv)

