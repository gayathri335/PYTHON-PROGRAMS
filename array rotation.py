def rotate_array(arr, k):
    """
    Function to rotate the array to the right by k positions.
    
    Parameters:
    arr (list): The input array.
    k (int): The number of positions to rotate.
    
    Returns:
    list: The rotated array.
    """
    n = len(arr)
    k = k % n  # To handle cases where k > n
    return arr[-k:] + arr[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = int(input("enter the target to rotate:"))
rotated_arr = rotate_array(arr, k)
print("Original Array:", arr)
print("Rotated Array:", rotated_arr)
