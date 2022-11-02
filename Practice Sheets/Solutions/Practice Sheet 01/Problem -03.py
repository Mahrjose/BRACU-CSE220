# Problem -03


def squareArray(arr):

    prevLast = arr[len(arr) - 2]

    for i in range(1, len(arr)):

        arr[i - 1] = arr[i] ** 2

        if i == len(arr) - 1:
            arr[i] = prevLast**2

    return arr


def main():
    sampleInput = [[1, 2, 3, 4, 5, 6], [5, 9, 1, 8, 2, 4, 6, 3, 5]]

    for arr in sampleInput:
        print(squareArray(arr))


if __name__ == "__main__":
    main()
