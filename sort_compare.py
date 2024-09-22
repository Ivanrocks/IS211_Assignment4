import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end_time = time.time()
    return end_time - start_time

def shellSort(alist):
    start_time = time.time()
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        #print("After increments of size", sublistcount, "The list is",alist)

        sublistcount = sublistcount // 2
    end_time = time.time()
    return end_time - start_time

def gapInsertionSort(alist, start, gap):
    start_time = time.time()
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue
    end_time = time.time()
    return end_time - start_time

def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    start_time = time.time()
    mylist =  sorted(a_list)
    end_time = time.time()
    return end_time - start_time
def main():
    list_sizes = [500, 1000, 5000]

    # the_size = list_sizes[0]
    sort_dict = {
        "InsertionSort": 0,
        "ShellSort": 0,
        "pythonSort": 0
    }
    for the_size in list_sizes:

        print("#" * 50)
        print("Size of list:", the_size, )

        for i in range(100):
            mylist500 = get_me_random_list(the_size)

            time_spent = python_sort(mylist500)
            sort_dict["pythonSort"] += time_spent

            time_spent = shellSort(mylist500)
            sort_dict["InsertionSort"] += time_spent

            time_spent = shellSort(mylist500)
            sort_dict["ShellSort"] += time_spent

        avg_time = sort_dict["pythonSort"] / the_size
        print(f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        avg_time = sort_dict["InsertionSort"] / the_size
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        avg_time = sort_dict["ShellSort"] / the_size
        print(f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        print("#" * 50)
        print()


if __name__ == "__main__":
    """Main entry point"""
    main()
