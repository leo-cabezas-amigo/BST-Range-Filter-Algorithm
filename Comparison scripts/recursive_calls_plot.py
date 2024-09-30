# -*- coding: utf-8 -*-

# FILE NAME: performance_comparison.py
# AUTHOR: Leo Cabezas Amigo (NIA: 100504261)

# Determines whether solution_classes.py or solution_classes_no_mod.py will be imported
using_no_mod = False

if using_no_mod:
    from solution_classes_no_mod import BSTa
    from solution_classes_no_mod import BSTb
else:
    from solution_classes import BSTa
    from solution_classes import BSTb

import random
import matplotlib.pyplot as plt

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
        print("Processed tree size: ", size, "/", max_tree_size + 1)
        
        # Sets tree size for the next iteration
        size += sample_step
    
    rec_call_cmp_list = [(recs_a / recs_b - 1) * 100 for recs_a, recs_b in zip(tree_a_recursions, tree_b_recursions)]
    print(format(sum(rec_call_cmp_list) / len(rec_call_cmp_list), ".2f") + "%")
    
    # Plots data from both algorithms using matplotlib
    plt.plot(sizes, tree_a_recursions, label = "My solution")
    plt.plot(sizes, tree_b_recursions, label = "Your solution")
    
    plt.xlabel("Tree size")
    plt.ylabel("# of recursive calls")
    
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    recursive_calls_cmp(1, 10000, 10, 10)