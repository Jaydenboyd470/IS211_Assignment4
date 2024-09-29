import time
import random

# Helper function to generate random list
def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

# Sequential Search
def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

# Ordered Sequential Search (requires sorted list)
def ordered_sequential_search(a_list, item):
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
    return found

# Binary Search Iterative
def binary_search_iterative(a_list, item):
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
    return found

# Binary Search Recursive
def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

# Main function to compare search algorithms
def main():
    list_sizes = [500, 1000, 5000]
    num_trials = 100
    search_value = 99999999  # Worst-case scenario (item not in list)

    for size in list_sizes:
        print(f"\nFor list size {size}:")

        # Sequential Search
        total_time = 0
        for _ in range(num_trials):
            mylist = get_me_random_list(size)
            start = time.time()
            sequential_search(mylist, search_value)
            total_time += time.time() - start
        avg_time = total_time / num_trials
        print(f"Sequential Search took {avg_time:10.7f} seconds on average.")

        # Ordered Sequential Search (sorted list)
        total_time = 0
        for _ in range(num_trials):
            mylist = sorted(get_me_random_list(size))
            start = time.time()
            ordered_sequential_search(mylist, search_value)
            total_time += time.time() - start
        avg_time = total_time / num_trials
        print(f"Ordered Sequential Search took {avg_time:10.7f} seconds on average.")

        # Binary Search Iterative (sorted list)
        total_time = 0
        for _ in range(num_trials):
            mylist = sorted(get_me_random_list(size))
            start = time.time()
            binary_search_iterative(mylist, search_value)
            total_time += time.time() - start
        avg_time = total_time / num_trials
        print(f"Binary Search Iterative took {avg_time:10.7f} seconds on average.")

        # Binary Search Recursive (sorted list)
        total_time = 0
        for _ in range(num_trials):
            mylist = sorted(get_me_random_list(size))
            start = time.time()
            binary_search_recursive(mylist, search_value)
            total_time += time.time() - start
        avg_time = total_time / num_trials
        print(f"Binary Search Recursive took {avg_time:10.7f} seconds on average.")

if __name__ == "__main__":
    main()
