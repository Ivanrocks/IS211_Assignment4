import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    """
    uses the sequential search algorith to search the item in a list.
    The list does not have to be sorted.
    :param a_list: The list used to search the item
    :param item: the item to search in a_list
    :return: found , end_time - start_time
    """
    start_time = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end_time = time.time()
    return found, end_time - start_time


def ordered_sequential_search(a_list, item):
    """
    uses the ordered sequential search algorithm to search an item in a list
    a_list have to be sorted before calling this function
    :param a_list: The list used to search the item
    :param item: the item to search in a_list
    :return: found , end_time - start_time
    """
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end_time = time.time()
    return found, end_time - start_time


def binary_search_iterative(a_list,item):
    """
        uses binary search algorithm to search an item in a list
        a_list have to be sorted before calling this function
        :param a_list: The list used to search the item
        :param item: the item to search in a_list
        :return: found , end_time - start_time
    """
    start_time = time.time()

    first = 0

    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()

    return found, end_time - start_time
    
    
def binary_search_recursive(a_list,item):
    """
        uses the binary search recursive algorithm to search an item in a list
        a_list have to be sorted before calling this function
        :param a_list: The list used to search the item
        :param item: the item to search in a_list
        :return: found , end_time - start_time
        """
    start_time = time.time()

    if len(a_list) == 0:
        end_time = time.time()
        return False, end_time - start_time
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end_time = time.time()
            return True, end_time - start_time
        else:
            if item < a_list[midpoint]:

                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

def main():
    """
    Main function that drives the main flow of the program.
    Will collect the average time a function needs to search or sort an item in a randomly generated list.
    It will print out the total of calling each algorithm 500,1000, 5000 times
    :return:
    """
    the_size = [500, 1000, 5000]
    search_dict = {
        "BinarySearchIterative": 0,
        "BinarySearchRecursive": 0,
        "OrderedSequentialSearch": 0,
        "SequentialSearch": 0

    }

    total_time = 0

    for size in the_size:
        print("#" * 50)
        print("Size of list:", size, )

        for i in range(100):
            mylist = get_me_random_list(size)
            # sorting is not needed for sequential search.
            found, time_spent = ordered_sequential_search(mylist, 99999999)
            search_dict["SequentialSearch"] += time_spent

            mylist = sorted(mylist)

            found, time_spent = binary_search_iterative(mylist, 99999999)
            search_dict["BinarySearchIterative"] += time_spent

            found, time_spent = binary_search_recursive(mylist, 99999999)
            search_dict["BinarySearchRecursive"] += time_spent

            found, time_spent = ordered_sequential_search(mylist, 99999999)
            search_dict["OrderedSequentialSearch"] += time_spent

        avg_time = search_dict["SequentialSearch"] / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run.")

        avg_time = search_dict["BinarySearchIterative"] / 100
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds to run.")

        avg_time = search_dict["BinarySearchRecursive"] / 100
        print(f"Binary Search recursive took {avg_time:10.7f} seconds to run.")

        avg_time = search_dict["OrderedSequentialSearch"] / 100
        print(
            f"Ordered Sequential Search took {avg_time:10.7f} seconds to run.")

        print("#" * 50)
if __name__ == "__main__":
    """Main entry point"""
    main()
