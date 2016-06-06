#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # Move through the list the same number of times as there are items less one
    for count in range(len(lst) - 1):
    swap_occurred = False
        # Move through each item in list, but stop before the final item and the
        # final "count" number of items because those will already be sorted.
        for index in range(len(lst) - 1 - count):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
                swap_occurred = True
        if not swap_occurred:
            # If nothing swapped, list is already sorted
            break



def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    sorted_list = []
    while list1 or list2:
        if not list1:
            sorted_list.extend(list2)
        if not list2:
            sorted_list.extend(list1)
        if list1[0] < list2[0]:
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))

    return sorted_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    pass




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print