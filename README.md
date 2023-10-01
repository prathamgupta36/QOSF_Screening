# QOSF Cohort 8 Screening

This repository contains my solution to the QOSF Screening Task. 

The tasks are designed to
- find out if you have the skills necessary to succeed in our program.
- be doable with basic QC knowledge
- nothing should be too hard for you to quickly learn. 
- allow you to learn some interesting concepts of QC. 
- give you some choices depending on your interests.

## Introduction
The task I chose is Task 2 which is to find negative values where we are given a list of integer numbers, look for a negative number in the list. Consider an appropriate number of qubits and explain why your proposal is valid for all kinds of numbers in case.

# Find Negative Numbers in a List with Quantum Computing

This Python function, `find_negative_numbers`, is designed to identify the presence of negative numbers in an integer list. It returns `True` if any negative numbers are found and `False` otherwise.

## Function Signature

```python
def find_negative_numbers(list_number: List[int]) -> bool:
    """
    Identify the presence of negative numbers in an integer list.
    
    Parameters:
    - list_number (List[int]): List of integers to check for negatives.

    Returns:
    - bool: True if any negative numbers are found, False otherwise.
    """

```

# Example usage:
A = find_negative_numbers([1, -3, 2, 15])
print(A)  # Output: True



