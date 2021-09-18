# Python program to print largest contiguous array using Kadane’s Algorithm

from sys import maxsize

# Function to find the maximum contiguous subarray
# and print its array
def maxSubArray(arr):

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, len(arr)):

        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    longest_array = arr[start: end+1]

    # print ("Maximum contiguous sum is %d"%(max_so_far))
    # print ("Starting Index %d"%(start))
    # print ("Ending Index %d"%(end))

    return longest_array





# Alternative method

def longest_subarray(arr):
    # This function returns the longest subarray given an arr
    max_value = arr[0]
    new_array = [arr[0]]

    for i in range(len(arr)-1):
        curr_value = arr[i]
        for j in range(len(arr)-1):
            if j + 1 > i:
                curr_value += arr[j+1] 
                # print('curr value', curr_value)
                # print('max value', max_value)

                if curr_value > max_value:
                    max_value = curr_value
                    new_array = arr[i:j+2]
                    
                    
                else:
                        new_array = new_array
                        # print('new arr', new_array)
    return new_array

if __name__ == '__main__':

    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print('maxSubArray')
    print(maxSubArray(arr))

    # print('max fun', max( arr))
    print(longest_subarray(arr))

