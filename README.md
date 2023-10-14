# QOSF Cohort 8 Screening

This repository contains my solution to the QOSF Screening Task. 

## NOTE
### The solution for task 2 can be found in both [Jupyter Notebook](./Task2.ipynb) and [Python](./task2_sol.py) format. 
The solution in the Jupyter Notebook format contains the explanation and for the Python format, you can refer to [Solution Explanation](#solution) as that does not contain my full explanation.

The tasks are designed to
- find out if you have the skills necessary to succeed in our program.
- be doable with basic QC knowledge
- nothing should be too hard for you to quickly learn. 
- allow you to learn some interesting concepts of QC. 
- give you some choices depending on your interests.

## Introduction
The task I chose is Task 2 which is to find negative values where we are given a list of integer numbers, and look for a negative number in the list. Consider an appropriate number of qubits and explain why your proposal is valid for all kinds of numbers in case.

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

<a name="solution"></a>
# Solution Explanation

The code utilizes a quantum circuit to identify negative numbers within a given list. The quantum circuit operates as follows:

1. For each number in the list, a qubit is created.
2. All qubits are placed in a superposition state.
3. For each number in the list, if the number is negative, a Z gate is applied to the corresponding qubit.
4. All qubits are returned to a superposition state.
5. The qubits are measured.
6. If all measurement results are 0, there are no negative numbers in the list. Otherwise, there is at least one negative number in the list.

## Correctness

The quantum circuit's correctness is based on the properties of the Z gate:

- Z |0⟩ = |1⟩
- Z |1⟩ = |0⟩

This implies that the Z gate flips the state of a qubit.

In the quantum circuit, a Z gate is applied to a qubit if the corresponding number in the list is negative. This means that if there is at least one negative number in the list, then at least one qubit will be flipped after the Z gates are applied.

When we measure the qubits, we will obtain at least one measurement result of 1 if there is at least one negative number in the list. Otherwise, we will receive all measurement results as 0.

Therefore, the quantum circuit accurately identifies whether there is a negative number in the list.

## Validity for All Kinds of Numbers

The quantum circuit is valid for all types of numbers because the Z gate's behavior is independent of the value of the number. The Z gate simply flips the state of the qubit, regardless of the numerical value.

Hence, the quantum circuit can be employed to identify negative numbers in a list containing any kind of numbers, including integers, floating-point numbers, and complex numbers.

