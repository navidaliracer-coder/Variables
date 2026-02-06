#Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)
class pair_elements:

    def twosum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

value = int(input("Enter the sum you want to search for :"))
print("index1=%d, " % pair_elements().twosum(10, 20, 30, 40, 50, 60, 70), value)