#Find the Second-Largest Number in given array

nums=[10,20,109,4,55,99,77]
largest = nums[0]
second_largest = nums[0]
#before Loop Start
print(largest)
print(second_largest)
#After Loop Start
for i in nums:
    if i>largest:
        print("First Iteration value of I")
        print(largest)
        print("After If condition Execution value")
        second_largest=largest
        largest=i
        print("Second value",second_largest)
        print("First",largest)
    elif i>second_largest and i!=largest:
        second_largest=i
print(largest)
print("Second Largest value",second_largest)