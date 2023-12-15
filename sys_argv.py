import sys

if len(sys.argv) == 2:
    n = int(sys.argv[1])
    for _ in range(n):
        print("meow")
else:
    print("usage: meow.py")
