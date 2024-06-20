def LinearSearch(a, val):
    for i in range(len(a)):
        if a[i] == val:
            return i
    return -1

a = [1,2,56,324,73,23,34,987,12,122,2345,42,9]
val = int(input("Enter the element you want to search for : ")) 

result = LinearSearch(a,val)

if result != -1:
    print(f"{val} was found at index {result}")
else:
    print(f"{val} is not present in the list")    

