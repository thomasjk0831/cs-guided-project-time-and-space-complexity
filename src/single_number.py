"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice 
except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2

- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
    s = set()
    # how could we save data to write a implementation that is more efficient? 
    # for any given number, we'd like to know if we've seen this number already 
    # can we somehow save each number we've seen in such a way that when we see 
    # the next copy of it, we can access this quickly 

    # loop through nums 
    for num in nums: # O(n)
        # check if the num is in our set 
        # if it is
        if num in s: # O(1)
            # remove it from our set 
            s.remove(num) # O(1)
        # if it isn't
        else:
            # add it to the set 
            s.add(num) # O(1)
        
    # the only thing left in the set should be our odd-number-out 
    # the only way to grab the odd-element-out from our set is to 
    # turn it into a list and access it via its index 
    return s.pop() # O(1) since our set should always only have 1 element 

    # O(n^2)
    # we could use nested for loops to check 
    # if every element has another copy of itself 
    # in the list 
        # the odd-number-out will not find a copy of itself 
        # so that would be our answer 
