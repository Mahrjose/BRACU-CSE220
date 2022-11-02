# Problem -02


def alternateArray(arr):

    # Loop through every 2 elements in the array
    for i in range(0, len(arr), 2):

        # check if the first element is positive/negative
        if arr[i] >= 0:
            lastNumPos = True
        else:
            lastNumPos = False

        # After confirming the positive/negative number
        # Loop though the array to find the 2nd pos/neg number
        for j in range(i + 1, len(arr)):

            if lastNumPos:
                if arr[j] < 0:

                    arr[i + 1], arr[j] = arr[j], arr[i + 1]
                    break

                else:
                    continue

            else:
                if arr[j] >= 0:

                    # swap the 1st negative number with the recently
                    # found negative number. Then again swap that number
                    # with the number in front of the positive number
                    arr[i], arr[j] = arr[j], arr[i]
                    arr[i + 1], arr[j] = arr[j], arr[i + 1]
                    break

                else:
                    continue

    return arr


def main():

    # Testing edgecases
    # sampleInput = [[1, 2, 3, -1, -2, -3], [-1, -2, -3, 1, 2, 3]]
    sampleInput = [[1, -5, -9, 2, -6, 8], [-1, -5, 9, -2, 6, 8]]

    for arr in sampleInput:
        print(alternateArray(arr))


if __name__ == "__main__":
    main()
