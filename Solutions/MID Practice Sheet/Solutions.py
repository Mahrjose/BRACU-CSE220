# Problem -01
a = 48
b = 21


def resize(circ, start):
    new_circ = [0] * (len(circ) + 3)

    index = start
    for _ in range(len(circ)):
        new_circ[index] = circ[start]
        index = (index + 1) % len(new_circ)
        start = (start + 1) % len(circ)

    return new_circ


def remove_item_by_rightshift(circ, start, size, itemToRemove):

    for i in range(len(circ)):
        if circ[i] == itemToRemove:
            circ[i] = 0

    print(circ)


def insert(circ, start, size, pos, item):

    if size >= len(circ):
        "\nNo Space in array. Resizing...\n"
        resize(circ, 6)

    last_index = (start + size - 1) % len(circ)

    if pos > last_index and pos < start:
        circ[last_index + 1] = item

    else:
        while last_index != pos - 1:

            if last_index < 0:
                last_index = len(circ) - 1

            indexplusone = (last_index + 1) % len(circ)
            circ[indexplusone] = circ[last_index]

            last_index -= 1

        circ[pos] = item
    print(circ)


def removeByLeftShift(circ, start, size, itemToRemove):

    removeItemIndexList = []
    index = start
    last_index = (start + size - 1) % len(circ)
    while index != last_index:
        if circ[index] == itemToRemove:
            circ[index] = 0
            removeItemIndexList.append(index)

        index = (index + 1) % len(circ)

    for i in removeItemIndexList[::-1]:
        while i != last_index:
            circ[i] = circ[((i + 1) % len(circ))]

            i = (i + 1) % len(circ)

        circ[i] = 0
        size -= 1
        last_index = (start + size - 1) % len(circ)

    print(circ)


def rightRotate(circ, start, size, times):

    for _ in range(times):
        last_index = (start + size - 1) % len(circ)

        endPoint = last_index + 1
        while last_index != endPoint:

            if last_index < 0:
                last_index = len(circ) - 1

            circ[(last_index + 1) % len(circ)] = circ[last_index]
            last_index -= 1

        start = (start + 1) % len(circ)

    print(circ)


def leftRotate(circ, start, times):
    for _ in range(times):

        index = start
        endPoint = index - 1
        while index != endPoint:

            if index - 1 < 0:
                circ[len(circ) - 1] = circ[index]
            else:
                circ[index - 1] = circ[index]

            index = (index + 1) % len(circ)

        start -= 1
        if start < 0:
            start = len(circ) - 1

    print(circ)


circ = [25, a + 15, 52, 25, 0, 0, b + 25, 25, 5, 19, 5 + a, 5, 6 + b]
print("Circular Array:")
print(circ)

# Question 2 - 4
print("\nQuestion 2 - 4: ")
insert(circ, 6, 11, 5, b % 67)
insert(circ, 6, 11, 8, b % 13)
insert(circ, 6, 11, 3, b % 61)

# Question 5 -6
print("\nQuestion 5 - 6: ")
removeByLeftShift(circ, 6, 11, 5)
removeByLeftShift(circ, 6, 11, 52)

# Question 7
print("\nQuestion 7: ")
rightRotate(circ, 6, 11, 3)

# Question 8
print("\nQuestion 8: ")
leftRotate(circ, 6, 4)
