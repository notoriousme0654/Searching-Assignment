def BinarySearch(a, val):
    low = 0
    high = len(a) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if a[mid] == val:
            return mid
        elif a[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1

a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20, 23, 67, 98, 133, 789]
val = int(input("Enter an element to search for : "))

result = BinarySearch(a, val)

if result != -1:
    print(f"Required element {val} found at index {result}.")
else:
    print(f"Required element {val} not found in the list.")
