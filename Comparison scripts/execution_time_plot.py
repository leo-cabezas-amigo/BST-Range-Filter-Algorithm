# -*- coding: utf-8 -*-

# FILE NAME: performance_comparison.py
# AUTHOR: Leo Cabezas Amigo (NIA: 100504261)

# WARNING: Accuracy of results may be influenced by processes being
# executed on the background. For best results, terminate all background
# processes possible before executing this script and don't interact with
# the machine until testing is completed.

# Determines whether solution_classes.py or solution_classes_no_mod.py will be imported
using_no_mod = False

if using_no_mod:
    from solution_classes_no_mod import BSTa
    from solution_classes_no_mod import BSTb
else:
    from solution_classes import BSTa
    from solution_classes import BSTb

import random
import time
import matplotlib.pyplot as plt

def get_exec_times(min_tree_size, max_tree_size, sample_step, elem_sparseness_const):
    # Initializes data lists
    sizes = []
    tree_a_exec_times = []
    tree_b_exec_times = []
    
    # Initializes time measuring variables
    exec_time_a = 0
    exec_time_b = 0
    
    time_a_begin = 0
    time_a_end = 0
    time_b_begin = 0
    time_b_end = 0
    
    # Sets parameters for random tree generation and testing
    min_tree_size = 1
    max_tree_size = 100000
    sample_step = 1000
    elem_sparseness_const = 10
    
    size = min_tree_size
    while size <= max_tree_size + 1:
        # Makes a random choice of tree elements, and of min and max
        random_elems = random.sample(range(elem_sparseness_const * size), size)
        random_num1 = random.choice(random_elems)
        random_num2 = random.choice(random_elems)
        
        if random_num2 < random_num1:
            random_min = random_num2
            random_max = random_num1
        else:
            random_min = random_num1
            random_max = random_num2
        
        # Creates trees to be used in algorithm comparison
        tree_a = BSTa() # This tree uses my algorithm (from class BSTa)
        tree_b = BSTb() # This tree uses your algorithm (from class BSTb)
        
        for elem in random_elems:
            tree_a.insert(elem)
            tree_b.insert(elem)
        
        # Computes execution time and result for my algorithm
        time_a_begin = time.time()
        result_a = tree_a.outsideRange(random_min, random_max)
        time_a_end = time.time()
        
        # Computes execution time and result for your algorithm
        time_b_begin = time.time()
        result_b = tree_b.outsideRange(random_min, random_max)
        time_b_end = time.time()
        
        # Checks if both algorithms yield the same result
        assert(result_a == result_b)
        
        # Calculates execution times for both algorithms
        exec_time_a = time_a_end - time_a_begin
        exec_time_b = time_b_end - time_b_begin
        
        # Updates data lists
        sizes.append(size)
        tree_a_exec_times.append(exec_time_a)
        tree_b_exec_times.append(exec_time_b)
        
        # Prints a progress message to screen
        print("Processed tree size: ", size, "/", max_tree_size + 1)
        
        # Sets tree size for the next iteration
        size += sample_step
    
    exec_time_cmp_list = list()
    for recs_a, recs_b in zip(tree_a_exec_times, tree_b_exec_times):
        if recs_b != 0.0:
            exec_time_cmp_list.append((recs_a / recs_b - 1) * 100)
        else:
            print(recs_a, recs_b)
    
    efficiency_diff = sum(exec_time_cmp_list) / len(exec_time_cmp_list)
    # print(format(efficiency_diff, ".2f") + "%")
    return efficiency_diff
    
    """
    # Plots data from both algorithms using matplotlib
    plt.plot(sizes, tree_a_exec_times, label = "My solution")
    plt.plot(sizes, tree_b_exec_times, label = "Your solution")
    
    plt.xlabel("Tree size")
    plt.ylabel("Execution time (s)")
    
    plt.legend()
    plt.show()
    """
    
if __name__ == '__main__':
    import sys
    
    try:
        tests_performed = int(sys.argv[1])
    except:
        raise Exception("Error: invalid/not enough arguments.")
    
    results = list()
    for i in range(tests_performed):
        results.append(get_exec_times(1, 100000, 1000, 1))
    
    average_effic_diff = sum(results) / len(results)
    print(format(average_effic_diff, ".2f") + "%")