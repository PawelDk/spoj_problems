# 34652, FUCT_FOR_ARROW - Right arrow

size = int(input())
if size <= 2 or size > 100:
    print("accept positive integer greater than 2 only!")
else:
    # top
    for x in range(1, size + 1):
        print("* ", end='')
    print()

    # upper part
    for x in range(1, int(size / 2)):
        for y in range(1, x + 1):
            print("  ", end='')
        print("*", end='')
        for y in range(1, (size - 2) + 1):
            print("  ", end='')
        print(" *")

        # bottom part
    for x in range(int(size / 2) + 2, size + 1):
        for y in range(0, (size - x) + 1):
            print("  ", end='')
        print("*", end='')
        for y in range(1, (size - 2) + 1):
            print("  ", end='')
        print(" *")

    # bottom
    for x in range(1, size + 1):
        print("* ", end='')
