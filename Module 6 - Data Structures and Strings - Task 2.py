list1 = [1,2,3,4,5,6,7,8,9,10]
#       0 1 2 3 4 5 6 7 8 9
print("Original list:", list1)
def returnfiveorless(n):
    if n<=5:
        return n

retrievedList = list(filter(returnfiveorless, list1))
rl = list(retrievedList)

print("Extracted first five elements:",rl)
rl.reverse()
print("Reversed extracted elements:", rl)