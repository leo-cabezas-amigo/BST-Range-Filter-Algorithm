# -*- coding: utf-8 -*-

# FILE NAME: performance_comparison.py
# AUTHOR: Leo Cabezas Amigo

# Determines whether solution_classes.py or solution_classes_no_mod.py will be imported

using_no_mod = False

from classes.solution_classes import BSTa
from classes.solution_classes import BSTb

import random
# import matplotlib.pyplot as plt

def get_recursive_call_count(min_tree_size, max_tree_size, sample_step, elem_sparseness_const):
    # Initializes data lists
    sizes = []
    tree_a_recursions = []
    tree_b_recursions = []
    
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
        
        # Computes results for both algorithms
        result_a = tree_a.outsideRange(random_min, random_max)
        result_b = tree_b.outsideRange(random_min, random_max)
        
        # Checks if both algorithms yield the same result
        assert(result_a == result_b)
        
        # Updates data lists
        sizes.append(size)
        tree_a_recursions.append(tree_a.recursions)
        tree_b_recursions.append(tree_b.recursions)
        
        # Prints a progress message to screen
        print("Processed tree size =", size, "; End size =", max_tree_size + 1)
        
        # Sets tree size for the next iteration
        size += sample_step
    
    exec_rec_cmp_list = list()
    for recs_a, recs_b in zip(tree_a_recursions, tree_b_recursions):
        if recs_b != 0.0:
            exec_rec_cmp_list.append((recs_a / recs_b - 1) * 100)
        else:
            exec_rec_cmp_list.append((recs_a / 0.00000001 - 1) * 100)
    
    efficiency_diff = sum(exec_rec_cmp_list) / len(exec_rec_cmp_list)
    # print(format(efficiency_diff, ".2f") + "%")
    return efficiency_diff
    
    """
    # Plots data from both algorithms using matplotlib
    plt.plot(sizes, tree_a_recursions, label = "My solution")
    plt.plot(sizes, tree_b_recursions, label = "Your solution")
    
    plt.xlabel("Tree size")
    plt.ylabel("# of recursive calls")
    
    plt.legend()
    plt.show()
    """
    
if __name__ == '__main__':
    import sys
    
    try:
        tests_performed = int(sys.argv[1])
    except:
        tests_performed = 3
    
    results = list()
    for i in range(tests_performed):
        print()
        results.append(get_recursive_call_count(1, 100000, 1000, 1))
        print(f"\n ==============TEST #{i + 1} COMPLETED==============")
    
    average_effic_diff = sum(results) / len(results)
    print("Recursive calls reduction (%) =", format(average_effic_diff, ".2f") + "%")