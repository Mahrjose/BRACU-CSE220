# Problem -03


def hocBuilder(height):
    if height == 0:
        return f"0 \nUse common sense! We cannot build house with 0 height!!!"

    if height == 1:
        return 8

    return 5 + hocBuilder(height - 1)


print("\nNo. 2(c)-->")
height = int(input("Enter Height: "))
print(hocBuilder(height))
