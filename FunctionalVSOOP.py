#sort array of 0s, 1s and 2s

class Solution:
    def sort012(self, arr, n):
        # Reference variables for zeros low, ones mid, and twos high. We name them like this instead of
        #zeros ones and twos because we need to sort position not face value and it gets confusing
        low = 0
        mid = 0
        #two is n-1 because a list or array starts with 0
        high = n - 1
        
        # Use a while loop to go through the list array until mid hits or crosses high
        while mid <= high:
            # If value is 0, switch it with the value at the low reference
            # (This moves 0s to the left)
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            # If value is 1, increment or continue moving across the array they should already be in
            #correct position at this point
            elif arr[mid] == 1:
                mid += 1
            # Similar to first if statement, check value and swap to move 2s to right
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

#Make an instance of Solution class so the sort012 method can be called below to check the code
solution = Solution()

#Check code
arr1 = [0, 2, 1, 2, 0]
n1 = len(arr1)
solution.sort012(arr1, n1)
print(arr1)





#Binary Search
class Solution:
    def binarysearch(self, arr, n, k):
        # Variables for left and right of the array (n is the length of the array like in the 1st exercise)
        left = 0
        right = n - 1

        # Loop through array while left is <= right
        while left <= right:
            #find the middle index of the array use integer division to make sure an integer is returned
            mid = left + (right - left) // 2

            # Then check if k is the mid of array
            if arr[mid] == k:
                return mid  # Return mid/index if k is equal to

            # If k is greater than the element at mid, ignore left half, keep incrementing to right
            elif arr[mid] < k:
                left = mid + 1

            # If k is smaller than the element at mid, ignore right half increment to left
            else:
                right = mid - 1

        # Return -1 if k is not found
        return -1
    
    #Check code with sample array and print results
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16]
    n = len(arr)
    k = 10

    #Instance of the Solution class to call binarysearch method
    solution = Solution()
    test_index = solution.binarysearch(arr, n, k)

    # Check if the element was found
    if test_index != -1:
        print("found")
    else:
        print("not found")