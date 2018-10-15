def largestSumOfSubarray(arr):
    max_ending_here = 0
    max_so_far = 0

    for i in arr:
        max_ending_here = max_ending_here + i
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far


def largestSumOfSubarrayBetter(arr):
    curr_max = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

def maxSubArraySum(a,size): 
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 

a = [-2, -3, -4, -1, -2, -1, -5, -3] 
print("Maximum contiguous sum is" , largestSumOfSubarrayBetter(a))
  