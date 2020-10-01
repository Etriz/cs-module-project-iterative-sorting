# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # ! Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # ! Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #! Your code here
    # looping over whole array
    for i in range(len(arr)):
        # looping over whole array again
        for j in range(len(arr) - 1):
            # compare numbers
            if arr[j] > arr[i]:
                # swap the two numbers if needed
                arr[j], arr[i] = arr[i], arr[j]

        # if i < len(arr) - 1 and arr[i] > arr[i + 1]:
        #     arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


"""
def insertion_sort(list_to_sort):
    # seperate the first element and think of it as sorted
    # let us say it is the first item in the list

    # for all other items (on the right of the first index)
    # range based starting at index 1
    for i in range(1, len(list_to_sort)):
        # put the current number in to a temporary variable (temp)
        temp = list_to_sort[i]

        # keep track of our current index as j
        j = i

        # keep looking left, until we find where our temp number belongs
        # while j is greater than zero (we are not past the start of the indces)
        # and our temp variable is less than the number to the left of j
        while j > 0 and temp < list_to_sort[j - 1]:
            # as we look left we can shift the items to the right as we iterate
            list_to_sort[j] = list_to_sort[j - 1]
            # decrement j
            j -= 1

        # when left is smaller than temp, or we are at zero, put the item at that spot
        list_to_sort[j] = temp

    # return the list back to the caller
    return list_to_sort
"""

"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
