# Problem -01


def pairSumFound(arr, sum):

    for i in arr:
        for j in arr:

            if i == j:
                continue

            pairSum = i + j
            if sum == pairSum:
                output = f"True -> Pair({i},{j})"
                return output

    return False


def main():

    # Don't want to manually input these :3
    inputDict = {
        "Input01": [[1, 5, 9, 2, 6, 8], 16],
        "Input02": [[1, 5, 9, 2, 6, 8], 15],
        "Input03": [[10, 3, 19, 2, 45, 81, 55], 100],
    }

    for inputNum, input in inputDict.items():

        arr = input[0]  # Returns the array
        sum = input[1]  # Returns the number/sum

        print(pairSumFound(arr, sum))


if __name__ == "__main__":
    main()
