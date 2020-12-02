"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:         
- two_sum(nums = [2,5,9,13], target = 18) -> [1,3]
- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""

# how can we write this with only a single for loop that 
# still gives us the same answer? 
def two_sum(nums, target):
    # we need to reduce redundancy by saving some data in a data structure
    # how do we want to save our data? 
    # because this problem needs us to return the index associated with each 
    # number, we'll need to store each number with its corresponding index 
    d = {}

    # O(n + n) == O(2 * n) ~ O(n)

    # populate our dictionary with the key value pairs 
    for index, num in enumerate(nums): # O(n)
        d[num] = index # O(1)

    # loop over all of the nums again 
    for index, num in enumerate(nums): # O(n)
        diff = target - num # O(1)
        # if diff in l: # O(n)
        if diff in d: # O(1)
			if diff == num:
            	return [index, d[diff]]

    return [-1, -1]


print(two_sum([2,5,9,13], 18))

# def two_sum(nums, target):
#     # Your code here
#     # using nested for loops, we can iterate 
#     # over the nums
#         # iterate over all the other nums 
#         # if the two numbers sum up to our target
#         # return their indices 

#     # O(n * n) == O(n^2)
#     for i in range(len(nums)): # O(n)
#         for j in range(len(nums)): # O(n)
#             # add a check to make sure the indices are different 
#             if i == j: # O(1)
#                 continue 
#             # O(1) + O(1) == O(2) ~ O(1)
#             if nums[i] + nums[j] == target:
#                 return [i, j]

#     # we'll only get outside this for loop if we don't find an answer 
#     return [-1, -1]
