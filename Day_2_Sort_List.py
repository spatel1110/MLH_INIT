arr = []


def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
n = int(input("Enter how many number you want to add in list.\n"))
for x in range(1, n + 1):
    m = int(input(f"Enter {x} Number :"))
    arr.append(m)

bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i]),
